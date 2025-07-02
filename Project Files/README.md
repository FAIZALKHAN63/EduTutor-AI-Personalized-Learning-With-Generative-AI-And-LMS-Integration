🎓 EduTutor AI
EduTutor AI is an advanced, intelligent, and user-friendly educational assistant designed to enhance online learning using cutting-edge AI models. It empowers students and educators through interactive quizzes, personalized Q&A support, and insights into student performance — all through a clean, web-based interface built with Streamlit and powered by Hugging Face Transformers.

💡 What is EduTutor AI?
EduTutor AI bridges the gap between traditional education and AI-powered adaptive learning. Whether you're a student needing quick clarity on a complex topic or an educator assessing class understanding, EduTutor AI offers intelligent assistance on demand.

🚀 Features Overview
🎒 Student Panel
📚 Subject-Based MCQ Quizzes
Take topic-specific quizzes in:

Artificial Intelligence

Machine Learning

Generative AI

Mathematics

🧠 Ask Questions via AI
Type any academic or general knowledge question and get real-time, AI-generated answers using powerful NLP models like flan-t5-xl.

🧾 History Dashboard
View your previous questions and AI responses in a neatly formatted Q&A dashboard for future reference and revision.

👩‍🏫 Educator Panel
📊 Performance Insights (Basic)
Visualize and monitor student performance from quiz results (dashboard features extensible for deeper analytics).

🧠 AI Models and Technology
Component	Description
Primary Model	google/flan-t5-xl — Open-source, instruction-tuned model for Q&A
Fallback Models	gpt2, ibm/granite-3b-instruct (optionally integrated)
Local Inference	Supported via Transformers pipeline + CUDA (if available)
Hosted Inference	Hugging Face Inference API used when local acceleration isn’t available
Frontend	Streamlit for web interface
Backend	Python (3.8+), transformers, torch, requests, sympy, etc.

📦 System Requirements
Python 3.8 or newer

Hugging Face token (for API usage)

Optional GPU (NVIDIA CUDA-enabled for performance boost)

Internet connection (for API access and model downloads)

🔧 Setup and Installation (Windows / Linux / Mac)
1️⃣ Clone the Project
bash
Copy
Edit
git clone https://github.com/yourusername/edututor-ai.git
cd edututor-ai
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If torch==2.1.0 fails, install a newer or CPU-compatible version:

bash
Copy
Edit
pip install torch==2.7.1+cpu --index-url https://download.pytorch.org/whl/cpu
3️⃣ Configure Hugging Face Token
Sign up at https://huggingface.co and get your API token. Then set it as:

bash
Copy
Edit
# Windows
set HF_TOKEN=your_token_here

# Linux/macOS
export HF_TOKEN=your_token_here
4️⃣ Run the App
bash
Copy
Edit
streamlit run app.py
The app will open automatically in your browser at:

text
Copy
Edit
http://localhost:8501
📁 Project Structure
graphql
Copy
Edit
EduTutor-AI/
│
├── app.py                # Streamlit application with panels and logic
├── questions.py          # Contains subject-wise MCQ question sets
├── load_flan_model.py    # Script to locally load flan-t5-xl
├── requirements.txt      # Python dependencies
└── README.md             # Project overview and instructions
✅ Supported Subjects
Artificial Intelligence: Logic, neural nets, applications

Machine Learning: Algorithms, types, regression, etc.

Generative AI: LLMs, transformers, applications

Mathematics: Algebra, probability, logic, word problems

🛠 Future Roadmap & Enhancements
🔐 User Login/Authentication System

🧑‍💼 Admin Dashboard to Upload/Modify Questions

🧪 Detailed Quiz Analytics (Time taken, Category-wise scores)

🌐 Multi-language Support (Telugu, Hindi, English, etc.)

🗣️ Voice Input and Text-to-Speech Output (via Gradio or Web APIs)

☁️ Database Integration: Firebase or Supabase for storing quiz data

🧠 Model Switching Interface: Choose between multiple AI models

📊 Live Leaderboards & Progress Tracking

🙏 Credits and Acknowledgments
🤗 Hugging Face for providing state-of-the-art open models

🧪 Google for flan-t5-xl

🖥 IBM Research for the Granite model family (optional extension)

💻 Streamlit for rapid, beautiful web UI development

🎓 Community-driven question datasets (or your own custom ones)
