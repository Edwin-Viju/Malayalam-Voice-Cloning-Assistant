import gradio as gr
from gradio_client import Client, file

# 🔗 Remote IndicF5 Space URL
SPACE_URL = "https://ai4bharat-indicf5.hf.space/"

print(f"Connecting to {SPACE_URL} ...")
client = Client(SPACE_URL)
print("✅ Connected to IndicF5 Space!")


def clone_voice(ref_audio_path, ref_text, target_text):
    if ref_audio_path is None:
        return None, "❌ Please upload a reference audio file."

    if not target_text or not target_text.strip():
        return None, "❌ Please enter Malayalam text to generate."

    if ref_text is None:
        ref_text = ""
    ref_text = ref_text.strip()

    try:
        result_audio = client.predict(
            target_text,                # text
            file(ref_audio_path),       # reference audio
            ref_text,                   # reference text
            api_name="/synthesize_speech"
        )
        return result_audio, "✅ Done! Voice cloned successfully."

    except Exception as e:
        return None, f"❌ API Error: {e}"


# ---------- UI ----------
with gr.Blocks(title="Malayalam Voice Cloner - Edwin Viju") as demo:

    gr.Markdown(
        """
        <h1 style="text-align: center; color: #1976D2;">
            🗣 MalaClony (IndicF5)
        </h1>

        <h3 style="text-align: center;">
            Create natural Malayalam speech in your own voice!
        </h3>

        <p style="text-align: center; font-size: 16px;">
            Upload a reference audio → give reference text → write new Malayalam → Clone! 😎
        </p>
        """
    )

    with gr.Row():
        with gr.Column():
            ref_audio = gr.Audio(
                label="1️⃣ Reference Audio (റഫറൻസ് ഓഡിയോ)",
                type="filepath"
            )
            ref_text = gr.Textbox(
                label="2️⃣ Text spoken in reference audio (ഓഡിയോയിൽ പറഞ്ഞ വാചകം)",
                placeholder="ഉദാ: ഞാൻ ഇന്നലെ കൊച്ചിയിലേക്ക് പോയി...",
                lines=2
            )
            gen_text = gr.Textbox(
                label="3️⃣ New Malayalam text to generate (പുതിയ വാചകം)",
                placeholder="ഇവിടെ പുതിയ മലയാളം ടെക്സ്റ്റ് ടൈപ്പ് ചെയ്യുക...",
                lines=3
            )
            run_btn = gr.Button("🚀 Generate Voice", variant="primary")

        with gr.Column():
            out_audio = gr.Audio(
                label="🔊 Output (ജനറേറ്റഡ് ഓഡിയോ)",
                type="filepath"
            )
            status = gr.Label(label="Status / നില")

    run_btn.click(
        fn=clone_voice,
        inputs=[ref_audio, ref_text, gen_text],
        outputs=[out_audio, status],
    )

    gr.Markdown(
        """
        <br><hr>
        <p style="text-align: center; font-weight: bold; font-size: 18px;">
            Created by <span style="color: #D32F2F;">Edwin Viju</span> ✨
        </p>

        <p style="text-align: center; font-size: 14px; color: gray;">
            Version 1.0 — Powered by IndicF5 🇮🇳
        </p>
        """
    )


if __name__ == "__main__":
    demo.launch(inbrowser=True)
