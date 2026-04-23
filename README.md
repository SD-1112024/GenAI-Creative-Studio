# [cite_start]Multi-Agent Collaborative Framework for Automated Narrative and Visual Content Generation [cite: 9]

## 👨‍💻 Authors
- [cite_start]**Sonika D** (USN: ENG23AM0187) [cite: 10]
- [cite_start]**Saumyaa Priyadarshinee** (USN: ENG23AM0187) [cite: 11]
**Academic Year:** 2025-2026 | [cite_start]Dayananda Sagar University [cite: 12]

## 📖 Project Overview
[cite_start]The **GenAI Creative Studio** is a resilient, multi-agent orchestration framework designed to bridge the gap between autonomous text generation and visual synchronization[cite: 21, 25]. [cite_start]Manual storyboarding is often inconsistent; this system automates the end-to-end workflow—from initial theme to final PDF report—ensuring that every generated image is semantically aligned with the narrative context[cite: 21].

## 🎯 Project Aim & Objectives
- [cite_start]**Narrative-Visual Sync:** A system where a primary Narrative Agent writes a story and a specialized Visual Agent "reads" it to generate matching imagery[cite: 21].
- [cite_start]**Model-Agnostic Resilience:** An intelligent failover layer with rotation to mitigate API rate limits and 429 errors[cite: 22, 26].
- [cite_start]**Automated Asset Persistence:** Instantly saves all AI-generated text and images into a local SQLite database for PDF report compilation[cite: 23, 41].

## 🏗️ Technical Architecture
[cite_start]The system follows a modular **Five-Phase Agentic Pipeline**:
1. [cite_start]**User Input Phase:** Accepts a Theme and Genre through a FastAPI interface[cite: 34].
2. [cite_start]**Narrative Agent (Groq / Llama 3.3):** The "Brain" that generates high-fidelity, 1000-word creative prose[cite: 35, 36].
3. [cite_start]**Visual Agent (Hugging Face / FLUX.1):** Performs real-time Information Extraction (IE) to identify scenes and character traits[cite: 30, 38].
4. [cite_start]**Resilience Layer:** Automatically rotates models if a primary provider hits a rate limit, ensuring 100% uptime[cite: 40].
5. [cite_start]**PDF Engine (FPDF2):** Pulls all metadata and imagery into a final formatted report[cite: 42].



## 🌟 Key Technical Features
- [cite_start]**Prompt Engineering as Data:** Our "dataset" consists of high-fidelity world-building constraints injected into the LLM[cite: 29].
- [cite_start]**Consistency Mapping:** Character metadata (e.g., "Jax’s neon-orange mohawk") is persisted across agents to maintain visual identity[cite: 32, 45].
- [cite_start]**JSON Structured Output:** Uses JSON mode for 100% accuracy in metadata extraction for character profiles[cite: 47].

## 📊 Result Analysis
- [cite_start]**Execution Efficiency:** Total pipeline execution (Narrative → Storyboard → PDF) completes in under **60 seconds**[cite: 46].
- [cite_start]**Synchronization Accuracy:** Achieved 100% alignment between story events and generated imagery[cite: 44].
- [cite_start]**Character Persistence:** Successfully maintained identifiers like Vesper’s "red visor" across multiple generated scenes[cite: 45].