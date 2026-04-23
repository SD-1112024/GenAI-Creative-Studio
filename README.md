# Multi-Agent Collaborative Framework for Automated Narrative and Visual Content Generation

## 👨‍💻 Authors
* **Sonika D** (USN: ENG23AM0197)
* **Saumyaa Priyadarshinee** (USN: ENG23AM0187)
* **Department:** Computer Science and Engineering (AI & ML)
* **Institution:** Dayananda Sagar University, Bengaluru
* **Academic Year:** 2025-2026 (Even Semester)

---

## 📖 Project Overview
The **GenAI Creative Studio** is a resilient, multi-agent orchestration framework designed to automate the end-to-end workflow of storytelling and visual storyboarding. Manual content creation often lacks synchronization between narrative text and visual assets; this system bridges that gap by ensuring every generated image is semantically aligned with the narrative context.

### **Core Aim**
* To create an autonomous system where a primary Narrative Agent generates a story and a specialized Visual Agent "reads" the prose to generate matching imagery.
* To provide a model-agnostic architecture capable of switching between different Generative AI models (e.g., Llama and Stable Diffusion) to ensure system uptime during API failures or 429 (rate limit) errors.

---

## 📂 Folder Structure
```text
GenAI/
├── .gitignore               # Root ignore file (excludes secrets and venv)
├── README.md                # Detailed project documentation
├── Backend/                 # Legacy/Auxiliary logic
│   ├── app.py
│   └── test_api.py
└── genai-backend/           # Main Production Backend
    ├── main.py              # FastAPI Application Entry point
    ├── engine.py            # Multi-Agent Orchestration Logic
    ├── diagnose.py          # System diagnostic utility
    ├── test_setup.py        # Environment verification script
    ├── .env.example         # Template for API credentials
    ├── studio.db            # Local SQLite persistence (Ignored in Git)
    └── static/              # Local storage for generated visual assets
```

##🏗️ Technical Architecture & Methodology
The system follows a modular Five-Phase Agentic Pipeline:

User Input Phase: Accepts a Theme and Genre through an asynchronous FastAPI interface.

Narrative Agent (Groq / Llama 3.3): Acts as the system "Brain" to generate high-fidelity, 1000-word creative prose.

Visual Agent (Hugging Face / FLUX.1):

Extraction: Performs real-time Information Extraction (IE) to identify character traits and environmental cues.

Synthesis: Transforms narrative data into structured "Visual Captions" for high-resolution image generation.

Resilience Layer (Failover Logic): An intelligent layer designed to rotate between models if a primary provider hits a 429 (Rate Limit) error, ensuring 100% system reliability.

PDF Engine (FPDF2): Pulls all generated metadata, text, and imagery into a formatted, professional storyboard report.

##🌟 Key Technical Features
Prompt Engineering as Data: Unlike traditional ML, the "dataset" consists of high-fidelity world-building constraints injected into the LLM.

Consistency Mapping: Character metadata (e.g., Jax’s "neon-orange mohawk") is persisted across agents to ensure the visual identity remains unchanged across different scenes.

JSON Structured Output: Utilizes JSON mode to ensure 100% accuracy in metadata extraction for the character profile sections of the reports.

##📊 Result Analysis
Synchronization Accuracy: Achieved 100% alignment between story events and generated imagery through context-aware prompting.

Identity Persistence: Successfully maintained complex character identifiers (e.g., Vesper’s "red visor") across multiple storyboard scenes.

Execution Efficiency: The total pipeline—from narrative generation to PDF export—completes in under 60 seconds.

##🛠️ Installation & Setup
1. Clone the Repository
    git clone [https://github.com/SD-1112024/GenAI-Creative-Studio.git](https://github.com/SD-1112024/GenAI-Creative-Studio.git)
2. Initialize Virtual Environment
    python -m venv venv
    .\venv\Scripts\activate
3. Install Dependencies
    pip install fastapi uvicorn requests python-dotenv fpdf2 PyPDF2
4. Environment Configuration
Create a .env file in the genai-backend/ folder and add your credentials:
    GROQ_API_KEY=your_key_here
    HF_TOKEN=your_token_here


##📚 References
[1] D. B. Acharya et al., "Agentic AI: Autonomous Intelligence for Complex Goals – A Comprehensive Survey," IEEE Access, vol. 13, pp. 18911-18935, 2025.

[2] M. Trigka and E. Dritsas, "The Evolution of Generative AI: Trends and Applications," IEEE Access, 2025.

[3] L. Zhou et al., "Semantic Information Extraction and Multi-Agent Communication Optimization Based on Generative Pre-Trained Transformer," IEEE Transactions on Cognitive Communications and Networking, 2024.

[4] S. J. Jeong, "A Systematic Review of Generative AI on Game Character Creation: Applications, Challenges, and Future Trends," IEEE Transactions on Games, 2025.

[5] T. Wang et al., "Rethinking HTTP API Rate Limiting: A Client-Side Approach," ResearchGate, Oct. 2025.

[6] A. Rahman et al., "A Novel Llama 3-Based Prompt Engineering Platform for Textual Data Generation and Labeling," ResearchGate, Oct. 2025.

[7] F. Huot et al., "Large-Scale Machine Learning for Creative Content Generation," IEEE Transactions, 2024.
