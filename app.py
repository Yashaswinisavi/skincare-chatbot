import streamlit as st
from utils.rag import load_data, search
from utils.web_search import search_web
from models.llm import generate_response

# 🎨 UI
st.set_page_config(page_title="Skincare Assistant", layout="centered")

st.markdown("""
<h1 style='text-align:center;'>🧴 AI Skincare Assistant 💖</h1>
""", unsafe_allow_html=True)

st.markdown("✨ Your personal skincare bestie 💅💖")

# LOAD RAG DATA
load_data()

# MODE
mode = st.radio("✨ Select Mode:", ["⚡ Concise", "📖 Detailed"])

# ---------------- SKIN ANALYZER ----------------
st.markdown("## 🧴 Skin Analyzer 💖")

skin_type = st.selectbox("Skin Type:", ["Oily", "Dry", "Combination"])
concern = st.selectbox("Concern:", ["Acne", "Dark spots", "Dull skin"])

if st.button("✨ Get Routine"):

    if skin_type == "Oily" and concern == "Acne":
        st.success("""
💖 Routine for Oily Skin with Acne

🌞 Morning:
• Dot & Key Salicylic Cleanser  
• Niacinamide Serum (Derma Co)  
• Oil-free moisturizer  
• Sunscreen SPF 50  

🌙 Night:
• Cleanser  
• Salicylic treatment  
• Moisturizer  

✨ Tips:
• Avoid touching face  
• Stay consistent  
""")

    elif skin_type == "Dry":
        st.success("""
💖 Routine for Dry Skin

🌞 Morning:
• Gentle cleanser  
• Hyaluronic acid serum  
• Thick moisturizer  
• Sunscreen  

🌙 Night:
• Cleanser  
• Moisturizer  

✨ Tips:
• Avoid hot water  
""")

    else:
        st.success("""
💖 Basic Routine

🌞 Morning:
• Cleanser  
• Moisturizer  
• Sunscreen  

🌙 Night:
• Cleanser  
• Moisturizer  
""")

# ---------------- CHATBOT ----------------
st.markdown("## 💬 Ask your skincare question")

query = st.text_input("Type here:", key="q1")

if query:
    try:
        # 🔹 RAG
        results = search(query)

        if results:
            context = " ".join(results)
            source = "📚 Local Data"
        else:
            # 🔹 WEB
            context = search_web(query)
            source = "🌐 Web Search"

        # 🔹 MODE
        if mode == "⚡ Concise":
            output = "Give short answer: " + context
        else:
            output = "Give detailed answer: " + context

        # 🔹 AI RESPONSE
        answer = generate_response(output)

        st.markdown(f"### 💖 Skincare Plan ({source})")
        st.write(answer)

    except Exception as e:
        st.error("Something went wrong")