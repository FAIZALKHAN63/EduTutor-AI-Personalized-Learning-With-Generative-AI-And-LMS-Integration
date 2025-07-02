import streamlit as st
import random
import requests
import os

# Import question sets
try:
    from questions import ai_questions, ml_questions, genai_questions, math_questions
except ImportError:
    st.error("❌ Could not import question sets. Please ensure 'questions.py' exists and is error-free.")
    st.stop()

# ======================== Configuration ======================== #
HF_API_TOKEN = os.getenv("HF_TOKEN")
if not HF_API_TOKEN or not HF_API_TOKEN.startswith("hf_"):
    st.warning("⚠️ Hugging Face API token not set or invalid. Set the HF_TOKEN environment variable for production use.")
    HF_API_TOKEN = "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"  # Placeholder for development
HF_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xl"

# ======================== Utility Functions ======================== #
def get_question_set(subject):
    """
    Retrieve the set of questions for the specified subject.

    Args:
        subject (str): The subject for which to retrieve questions.

    Returns:
        list: A list of questions for the specified subject.
    """
    question_bank = {
        "Artificial Intelligence": ai_questions,
        "Machine Learning": ml_questions,
        "Generative AI": genai_questions,
        "Mathematics": math_questions
    }
    return question_bank.get(subject, [])

def ask_huggingface_question(question):
    """
    Send a question to the Hugging Face API and retrieve the answer.

    Args:
        question (str): The question to ask.

    Returns:
        str: The response from the Hugging Face API.
    """
    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = { "inputs": f"Answer this clearly: {question}" }

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()

        # Process the response from Hugging Face
        if isinstance(result, list) and result:
            return result[0].get("generated_text") or result[0].get("summary_text") or "⚠️ No answer returned."
        elif isinstance(result, dict):
            return result.get("generated_text") or result.get("summary_text") or "⚠️ No answer returned."
        else:
            return "⚠️ Unexpected response format."
    except requests.exceptions.RequestException as e:
        return f"⚠️ Request error: {e}"
    except Exception as e:
        return f"⚠️ Unexpected error: {e}"

# ======================== UI Components ======================== #
def render_quiz_panel():
    """
    Render the quiz panel for students to take a quiz.
    """
    subject = st.selectbox("Choose Subject", ["Artificial Intelligence", "Machine Learning", "Generative AI", "Mathematics"])
    questions = get_question_set(subject)
    if not questions:
        st.warning("⚠️ No questions available for the selected subject.")
        return

    questions_sample = random.sample(questions, min(10, len(questions)))
    score = 0
    user_answers = {}

    with st.form("quiz_form"):
        for i, q in enumerate(questions_sample):
            st.markdown(f"**Q{i+1}: {q['question']}**")
            user_answers[q['question']] = st.radio("", q['options'], key=f"q_{i}")
        submitted = st.form_submit_button("Submit Quiz")

    if submitted:
        for q in questions_sample:
            if user_answers.get(q['question']) == q['answer']:
                score += 1
        st.success(f"✅ You scored {score}/{len(questions_sample)}")

def render_ask_question_panel():
    """
    Render the panel for students to ask questions and receive answers from the AI.
    """
    if "qa_history" not in st.session_state:
        st.session_state.qa_history = []

    st.markdown("### 🤖 Ask a Question (powered by Hugging Face)")
    user_question = st.text_input("Ask your question:")
    if st.button("Get Answer") and user_question.strip():
        with st.spinner("Getting answer..."):
            answer = ask_huggingface_question(user_question)
            st.session_state.qa_history.append({"question": user_question, "answer": answer})
            st.success("Answer:")
            st.write(answer)

    if st.session_state.qa_history:
        st.markdown("### 🧾 Your Question & Answer Dashboard")
        for i, entry in enumerate(reversed(st.session_state.qa_history)):
            st.markdown(f"**Q{i+1}:** {entry['question']}")
            st.markdown(f"🧠 **A:** {entry['answer']}")
            st.markdown("---")

def render_student_panel():
    """
    Render the student panel with quiz and question functionalities.
    """
    tab1, tab2, tab3 = st.tabs(["📚 Take Quiz", "📊 Quiz History", "❓ Ask a Question"])
    with tab1:
        render_quiz_panel()
    with tab2:
        st.info("📌 Quiz history will be available after backend integration.")
    with tab3:
        render_ask_question_panel()

def render_educator_panel():
    """
    Render the educator dashboard for monitoring student engagement.
    """
    st.header("📊 Educator Dashboard")
    st.markdown("Monitor student engagement and quiz performance.")
    st.info("🚧 More analytics features coming soon!")

# ======================== Main UI ======================== #
st.set_page_config(page_title="EduTutor AI", layout="centered")
st.title("🎓 EduTutor AI")
st.markdown("Welcome to your personalized AI learning assistant!")

panel_choice = st.sidebar.selectbox("Select Panel", ["Student Panel", "Educator Panel"])
if panel_choice == "Student Panel":
    render_student_panel()
else:
    render_educator_panel()