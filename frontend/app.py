import time
import streamlit as st
import json
import random
from streamlit_autorefresh import st_autorefresh

from backend.evaluator import evaluate_answer
from backend.database import init_db, save_interview

# Webcam confidence (optional)
confidence_check = None
try:
    from webcam.confidence import confidence_check
except ModuleNotFoundError:
    pass


# 🔽 DATABASE INIT (YAHIN)
init_db()

st.set_page_config(page_title="InterVueX", layout="centered")
st.title("🎤 AI Interview Bot – InterVueX")

# Load data
with open("roles/roles.json") as f:
    roles = json.load(f)

with open("data/questions.json") as f:
    questions = json.load(f)

with open("data/ideal_answers.json") as f:
    ideal_answers = json.load(f)

# Session state init
if "started" not in st.session_state:
    st.session_state.started = False
if "start_time" not in st.session_state:
    st.session_state.start_time = 0
if "question" not in st.session_state:
    st.session_state.question = ""
if "time_limit" not in st.session_state:
    st.session_state.time_limit = 0
if "answer" not in st.session_state:
    st.session_state.answer = ""

# Role selection
role = st.selectbox("Select Interview Role", roles.keys())

if st.button("Start Interview"):
    role_data = roles[role]
    topic = random.choice(role_data["topics"])
    st.session_state.question = random.choice(questions[topic])
    st.session_state.time_limit = role_data["time_limit"]
    st.session_state.start_time = time.time()
    st.session_state.started = True
    st.session_state.answer = ""

# ================= INTERVIEW SCREEN =================
if st.session_state.started:
    st.subheader("Interview in Progress")
    st.info(st.session_state.question)

    # 🔄 Auto refresh every 1 second (SAFE TIMER)
    st_autorefresh(interval=1000, key="timer_refresh")

    elapsed = int(time.time() - st.session_state.start_time)
    remaining = st.session_state.time_limit - elapsed

    if remaining > 0:
        st.warning(f"⏱️ Time Remaining: {remaining} seconds")

        st.session_state.answer = st.text_area(
            "Your Answer",
            value=st.session_state.answer,
            height=180
        )

        if st.button("Submit Answer"):
            ideal = ideal_answers.get(st.session_state.question, "")
            score, feedback = evaluate_answer(st.session_state.answer, ideal)

            save_interview(
                role=role,
                question=st.session_state.question,
                answer=st.session_state.answer,
                score=score
            )

            st.session_state.started = False
            st.success("✅ Answer submitted")
            st.metric("AI Score", score)
            st.info(feedback)

    else:
        st.error("⏰ Time is up! Answer locked.")

        ideal = ideal_answers.get(st.session_state.question, "")
        score, feedback = evaluate_answer(st.session_state.answer, ideal)

        save_interview(
            role=role,
            question=st.session_state.question,
            answer=st.session_state.answer,
            score=score
        )

        st.session_state.started = False
        st.metric("AI Score", score)
        st.info(feedback)
