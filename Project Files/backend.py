import gradio as gr
from model_engine import generate_mcqs

def run_quiz(subject, count):
    return generate_mcqs(subject, int(count))

demo = gr.Interface(
    fn=run_quiz,
    inputs=[
        gr.Dropdown(["Artificial Intelligence", "Machine Learning", "Generative AI", "Mathematics"], label="Subject"),
        gr.Slider(1, 15, step=1, label="Number of Questions")
    ],
    outputs=gr.Textbox(label="Generated Quiz"),
    title="EduTutor AI - Quiz Generator"
)

if __name__ == "__main__":
    demo.launch()
