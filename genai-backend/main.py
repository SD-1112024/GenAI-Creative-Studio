import sqlite3, json, os, io
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fpdf import FPDF
from PyPDF2 import PdfReader
from engine import run_creative_pipeline, call_api

app = FastAPI()

class StoryRequest(BaseModel):
    theme: str
    genre: str
    mode: str
    num_scenes: int = 7 

def init_db():
    conn = sqlite3.connect('studio.db')
    # Added title column
    conn.execute('''CREATE TABLE IF NOT EXISTS projects 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, theme TEXT, story TEXT, scenes TEXT, characters TEXT)''')
    conn.commit(); conn.close()

init_db()

@app.post("/generate_all")
async def generate_all(request: StoryRequest):
    data = run_creative_pipeline(request.theme, request.genre, request.mode, request.num_scenes)
    conn = sqlite3.connect('studio.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projects (title, theme, story, scenes, characters) VALUES (?, ?, ?, ?, ?)",
                   (data["title"], request.theme, data["story"], json.dumps(data["scenes"]), json.dumps(data["characters"])))
    conn.commit(); p_id = cursor.lastrowid; conn.close()
    
    return {"status": "Success", "project_id": p_id, "data": data}

@app.get("/download_pdf/{p_id}")
async def download_pdf(p_id: int):
    conn = sqlite3.connect('studio.db'); conn.row_factory = sqlite3.Row
    row = conn.cursor().execute("SELECT * FROM projects WHERE id = ?", (p_id,)).fetchone()
    conn.close()
    if not row: raise HTTPException(status_code=404, detail="Project not found")

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # 1. Narrative Page (Now uses the PROPER TITLE)
    pdf.add_page(); pdf.set_font("Arial", 'B', 16)
    title_text = row['title'].encode('latin-1', 'ignore').decode('latin-1')
    pdf.cell(0, 10, title_text, 0, 1, 'C'); pdf.ln(5)
    
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, row['story'].encode('latin-1', 'ignore').decode('latin-1'))
    
    # 2. Visual Storyboard (Now prints the ELABORATE 4-5 sentence explanation)
    scenes = json.loads(row['scenes'])
    for i, scene in enumerate(scenes):
        pdf.add_page()
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, f"Scene {i+1}", 0, 1, 'L')
        
        pdf.set_font("Arial", 'I', 11)
        scene_text = scene.get('text', '').encode('latin-1', 'ignore').decode('latin-1')
        pdf.multi_cell(0, 8, scene_text)
        pdf.ln(5)
        
        img_path = scene.get('image')
        if img_path and os.path.exists(img_path):
            pdf.image(img_path, w=180)

    # 3. Character Gallery
    characters = json.loads(row['characters'])
    pdf.add_page(); pdf.set_font("Arial", 'B', 18)
    pdf.cell(0, 15, "Character Profiles", 0, 1, 'C'); pdf.ln(10)

    for char in characters:
        pdf.set_font("Arial", 'B', 13)
        pdf.cell(0, 10, f"NAME: {char.get('name')}", 0, 1, 'L')
        pdf.set_font("Arial", 'I', 10)
        app_text = char.get('appearance', '').encode('latin-1', 'ignore').decode('latin-1')
        pdf.multi_cell(0, 7, f"APPEARANCE: {app_text}")
        
        if char.get('avatar') and os.path.exists(char['avatar']):
            pdf.image(char['avatar'], w=55)
        pdf.ln(15)

    report = f"Final_Report_{p_id}.pdf"
    pdf.output(report)
    return FileResponse(path=report, filename=report, media_type='application/pdf',
                        headers={"Content-Disposition": f"attachment; filename={report}"})

# ---------------------------------------------------------
# NEW ENDPOINT: Upload PDF and Edit Story
# ---------------------------------------------------------
@app.post("/edit_pdf_story")
async def edit_pdf_story(file: UploadFile = File(...), instruction: str = Form(...)):
    """Upload a generated PDF and provide an instruction to modify the story."""
    try:
        # Read the PDF file
        file_bytes = await file.read()
        pdf_reader = PdfReader(io.BytesIO(file_bytes))
        extracted_text = ""
        
        for page in pdf_reader.pages:
            extracted_text += page.extract_text() + "\n"
            
        # Send the extracted text and the instruction to the LLM
        prompt = (
            f"Here is a story and text extracted from a generated PDF report:\n\n"
            f"--- START PDF TEXT ---\n{extracted_text}\n--- END PDF TEXT ---\n\n"
            f"INSTRUCTION FROM USER: {instruction}\n\n"
            "Rewrite the story portion to perfectly match the user's instruction. "
            "Return ONLY the newly rewritten story text without any extra conversational filler."
        )
        
        new_story = call_api(prompt)
        
        return {
            "status": "Success", 
            "message": "Story successfully edited based on instruction.",
            "edited_story": new_story
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))