import os
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

device = "cuda" if torch.cuda.is_available() else "cpu"

def load_model(model_name="tiiuae/falcon-7b-instruct"):
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=HF_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32, use_auth_token=HF_TOKEN)
    return pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

generator = load_model()

def generate_mcqs(subject: str, num_questions: int = 5):
    prompt = f"""
Generate {num_questions} MCQs for students on the topic of "{subject}". 
Each question should include:
- Question
- 4 options (A, B, C, D)
- Correct Answer at the end in this format: Correct Answer: <option letter>
"""
    output = generator(prompt, max_new_tokens=700)
    return output[0]["generated_text"]
