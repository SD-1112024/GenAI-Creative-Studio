import os, requests, time, json, re
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(api_key=HF_TOKEN)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

def get_image(prompt, filename):
    img_path = os.path.join(STATIC_DIR, f"{filename}.png")
    os.makedirs(STATIC_DIR, exist_ok=True)
    
    try:
        print(f"  > Generating via HF FLUX.1-schnell...")
        image = client.text_to_image(prompt, model="black-forest-labs/FLUX.1-schnell")
        image.save(img_path)
        
        time.sleep(0.5)
        if os.path.exists(img_path) and os.path.getsize(img_path) > 1000:
            print(f"    [Success] Image saved via HF FLUX!")
            return img_path
    except Exception as e:
        print(f"    [Error] HF FLUX failed or busy: {e}")

    print(f"    [Fallback] Using Placeholder to prevent system crash...")
    placeholder_url = "https://placehold.co/1024x768/1a1a1a/00ffcc.png?text=AI+Server+Busy%5CnImage+Pending"
    try:
        img_data = requests.get(placeholder_url, timeout=10).content
        with open(img_path, 'wb') as f:
            f.write(img_data)
        return img_path
    except:
        return None

def call_api(prompt, json_mode=False):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}]
    }
    if json_mode: payload["response_format"] = {"type": "json_object"}
    try:
        response = requests.post(url, json=payload, headers=headers).json()
        content = response['choices'][0]['message']['content']
        return json.loads(content) if json_mode else content
    except: return {} if json_mode else None

def run_creative_pipeline(theme, genre, mode, num_scenes):
    print(f"\n[1/5] Generating Narrative...")
    story = call_api(f"Write a 1000-word prose narrative in {genre} about {theme}. Style: {mode}.")
    
    print("[2/5] Generating Title...")
    title = call_api(f"Generate a catchy, professional title for this story. Return ONLY the title text without quotes.\n\nStory: {story[:1000]}")
    title = title.replace('"', '').strip()
    
    print("[3/5] Extracting 3 Characters (JSON Mode)...")
    char_prompt = (
        "Return a JSON object with key 'characters' containing exactly 3 main characters. "
        "Appearance MUST be a plain string. If fewer than 3 characters, invent a side character.\n\n"
        f"Story: {story[:1500]}"
    )
    char_data = call_api(char_prompt, json_mode=True)
    characters_raw = char_data.get("characters", [])
    
    characters = []
    for c in characters_raw:
        app = c.get('appearance', 'Not specified')
        if isinstance(app, dict):
            app = ", ".join([f"{k.capitalize()}: {v}" for k, v in app.items()])
        characters.append({"name": c.get('name', 'Unknown'), "appearance": app})

    master_ref = " | ".join([f"{c['name']}: {c['appearance']}" for c in characters])

    print(f"[4/5] Generating {num_scenes}-Scene Storyboard (Elaborate JSON Mode)...")
    # CRITICAL FIX: We ask for a short image prompt AND an elaborate 5-sentence explanation
    scene_prompt = (
        f"Return a JSON object with a key 'scenes' containing exactly {num_scenes} scenes in chronological order based on the story. "
        "For each scene, provide two keys:\n"
        "1. 'image_prompt': A short 1-sentence visual description for an AI image generator.\n"
        "2. 'explanation': A vivid, highly elaborate 4-5 sentence cinematic paragraph explaining the action, the environment, and the characters' emotions.\n\n"
        f"Story: {story[:2000]}"
    )
    scene_data_raw = call_api(scene_prompt, json_mode=True)
    extracted_scenes = scene_data_raw.get("scenes", [])
    
    scene_data = []
    for i, sc in enumerate(extracted_scenes[:num_scenes]):
        print(f"  > Drawing Scene {i+1}/{num_scenes}...")
        img_prompt = f"{sc.get('image_prompt', '')}. Visual Ref: {master_ref}. Style: {genre} {mode}."
        img_path = get_image(img_prompt, f"scene_{int(time.time())}_{i}")
        
        # Save the ELABORATE text for the PDF
        scene_data.append({"text": sc.get('explanation', ''), "image": img_path})

    print("[5/5] Creating Character Portraits...")
    char_gallery = []
    for i, char in enumerate(characters):
        print(f"  > Portrait: {char['name']}...")
        p_prompt = f"Portrait of {char['name']}, {char['appearance']}. Style: {genre} {mode}."
        path = get_image(p_prompt, f"char_{int(time.time())}_{i}")
        char_gallery.append({"name": char['name'], "appearance": char['appearance'], "avatar": path})

    return {"title": title, "story": story, "scenes": scene_data, "characters": char_gallery}