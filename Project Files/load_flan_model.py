# First, ensure transformers is installed in your local environment
# Open Command Prompt (not in code) and run:
# pip install -U transformers

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load the tokenizer and model
print("Loading model, please wait...")

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-xl")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-xl")

# Create a pipeline for text-to-text generation
pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

# Test the model
question = "What is artificial intelligence?"
result = pipe(question, max_length=100, do_sample=True)

print("\nQuestion:", question)
print("Answer:", result[0]['generated_text'])
