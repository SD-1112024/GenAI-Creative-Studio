Multi-Agent Collaborative Framework for Automated Narrative and Visual Content Generation
👨‍💻 Authors

Sonika D (USN: ENG23AM0197) 


Saumyaa Priyadarshinee (USN: ENG23AM0187) 


Department: Computer Science and Engineering (AI & ML) 


Institution: Dayananda Sagar University, Bengaluru 


Academic Year: 2025-2026 (Even Semester)

📖 Project OverviewThe GenAI Creative Studio is a resilient, multi-agent orchestration framework designed to automate the end-to-end workflow of storytelling and visual storyboarding. Manual content creation often lacks synchronization between narrative text and visual assets; this system bridges that gap by ensuring every generated image is semantically aligned with the narrative context.Core AimTo create an autonomous system where a primary Narrative Agent generates a story and a specialized Visual Agent "reads" the prose to generate matching imagery.To provide a model-agnostic architecture capable of switching between different Generative AI models (e.g., Llama and Stable Diffusion) to ensure system uptime during API failures or rate limits.📂 Folder StructurePlaintextGenAI/
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
🏗️ Technical Architecture & Methodology
The system follows a modular Five-Phase Agentic Pipeline:User Input Phase: Accepts a Theme and Genre through an asynchronous FastAPI interface.Narrative Agent (Groq / Llama 3.3): Acts as the system "Brain" to generate high-fidelity, 1000-word creative prose.Visual Agent (Hugging Face / FLUX.1):Extraction: Performs real-time Information Extraction (IE) to identify character traits and environmental cues.Synthesis: Transforms narrative data into structured "Visual Captions" for image generation.Resilience Layer (Failover Logic): An intelligent layer designed to rotate between models if a primary provider hits a 429 (Rate Limit) error, ensuring 100% system reliability.PDF Engine (FPDF2): Pulls all generated metadata, text, and imagery into a formatted, professional storyboard report.🌟 Key Technical FeaturesPrompt Engineering as Data: Unlike traditional ML, the "dataset" consists of high-fidelity world-building constraints injected into the LLM.Consistency Mapping: Character metadata (e.g., Jax’s "neon-orange mohawk") is persisted across agents to ensure the visual identity remains unchanged across different scenes.JSON Structured Output: Utilizes JSON mode to ensure 100% accuracy in metadata extraction for the character profile sections of the reports.
📊 Result Analysis
Synchronization Accuracy: Achieved 100% alignment between story events and generated imagery through context-aware prompting.Identity Persistence: Successfully maintained complex character identifiers (e.g., Vesper’s "red visor") across multiple storyboard scenes.Execution Efficiency: The total pipeline—from narrative generation to PDF export—completes in under 60 seconds.
🛠️ Installation & SetupClone the Repository:
Bashgit clone https://github.com/SD-1112024/GenAI-Creative-Studio.git
Initialize Virtual Environment:Bashpython -m venv venv
.\venv\Scripts\activate
Install Dependencies:Bashpip install fastapi uvicorn requests python-dotenv fpdf2 PyPDF2
Environment Configuration:Create a .env file in the genai-backend/ folder and add your credentials:PlaintextGROQ_API_KEY=your_key_here
HF_TOKEN=your_token_here
📚 References[1] D. B. Acharya et al., "Agentic AI: Autonomous Intelligence for Complex Goals – A Comprehensive Survey," IEEE Access, vol. 13, 2025.[2] M. Trigka and E. Dritsas, "The Evolution of Generative AI: Trends and Applications," IEEE Access, 2025.[3] L. Zhou et al., "Semantic Information Extraction and Multi-Agent Communication Optimization Based on GPT," IEEE Transactions, 2024.
