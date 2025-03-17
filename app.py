import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="★")
st.title("🧠 Growth Mindset Challenge: Web App with Streamlit")

st.header("✨ Welcome to Your Growth Journey")
st.write("An interactive web application built with Streamlit in Python that empowers users to cultivate a growth mindset through daily challenges, motivational quotes, and self-reflection exercises")

st.header("🚀 Today's Growth Mindset Quote")
st.write("Embrace challenges, learn from failures, and grow every day. Your mindset is the key to unlocking endless possibilities")

st.header("What Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"You're facing: {user_input}. Keep pushing yourself!")
else:
    st.warning("Tell us about your challenge to get started")

st.header("Self-Reflection Exercise")
reflection = st.text_area("Write your project outcome here:")

if reflection:
    st.success(f"🎯 Great Insight! Your project outcome: {reflection}")
else:
    st.info("✍️ Take a moment to reflect on your progress and achievements. Your thoughts matter!")

st.header("🎉 Celebrate Your Acheivements!")
acheivement = st.text_input("Share something you've recently acheived:")

if acheivement:
    st.success(f"💫 Great! You acheived: {acheivement}")
else:
    st.info("Big or small, every acheivement counts! Share one now ❤️️")

st.write("_ _ _")
st.write("Every step you take towards learning and growth brings you closer to the best version of yourself 😊")
st.write("©️ Created by UmmeFizza")
