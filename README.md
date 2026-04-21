# 🎙️ MalaClony: Malayalam Voice Cloning Assistant

**Natural Malayalam speech synthesis powered by AI, delivered through a lightweight, API-driven architecture.**

MalaClony is a practical AI tool that clones specific voices in Malayalam using reference audio. While many voice cloning models require high-end GPUs and complex local setups, MalaClony is engineered for efficiency, utilizing remote inference to make high-quality speech synthesis accessible on standard desktop systems.

---

## 💡 The Problem
State-of-the-art voice cloning models, such as **IndicF5**, present several barriers for individual developers:
* **Hardware Intensive:** High GPU and VRAM requirements for local execution.
* **Access Barriers:** Gated model weights and restrictive access permissions.
* **Technical Complexity:** Issues like meta-tensor errors and environment conflicts during local loading.

## 🚀 The Solution
MalaClony bypasses these hurdles by utilizing a **remote inference architecture**. By connecting a custom **Gradio** interface to **Hugging Face Spaces**, the app performs heavy-duty voice synthesis in the cloud while maintaining a seamless, local user experience.

### Key Features
* **🎤 High-Fidelity Voice Cloning:** Generate speech in any specific voice using a short reference audio sample.
* **📝 Malayalam-Specific TTS:** Optimized for the nuances of Malayalam phonetics using the IndicF5 model.
* **⚡ Lightweight & Fast:** Runs smoothly on low-end systems without local GPU dependency.
* **🖥️ Personal Productivity Tool:** Includes a desktop-friendly launcher for quick access.
* **🔄 Reusable Profiles:** Use the same reference voice multiple times for consistent content creation.

## 🛠️ System Architecture

1.  **User Input:** Malayalam text + Reference Audio + Reference Text.
2.  **Frontend:** A clean, intuitive **Gradio UI** handles the data collection.
3.  **Bridge:** The `gradio_client` API transmits data to the remote model.
4.  **Inference:** The **IndicF5** model on Hugging Face Spaces processes the voice characteristics and synthesizes the speech.
5.  **Output:** The generated Malayalam audio is returned and played instantly.

## 💻 Tech Stack
* **AI Engine:** IndicF5 (via AI4Bharat)
* **Backend:** Python, Hugging Face API
* **UI Framework:** Gradio
* **Deployment:** Hugging Face Spaces / Local Desktop Shortcut
-------------------------------------
