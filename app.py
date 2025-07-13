import streamlit as st
from model_handler import get_model_response
from logger import log_interaction
import time

st.set_page_config(page_title="Lexiq", page_icon="🧠", layout="centered")

st.markdown("""
    <style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&family=Fira+Code:wght@400&display=swap');

html, body {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
    font-family: 'Poppins', sans-serif;
}

.main {
    padding-top: 30px;
    animation: fadeIn 1s ease-in;
}

h1, h2 {
    text-align: center;
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
}

textarea, .stTextInput input {
    background-color: #1e1e2f !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 10px !important;
    font-size: 16px !important;
    font-family: 'Poppins', sans-serif;
}

.stButton > button {
    background: linear-gradient(to right, #4e54c8, #8f94fb);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.75em 2em;
    font-size: 16px;
    font-weight: bold;
    font-family: 'Poppins', sans-serif;
    transition: all 0.3s ease;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
}

.stButton > button:hover {
    background: linear-gradient(to right, #8f94fb, #4e54c8);
    transform: scale(1.05);
    box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.4);
}

.glassbox {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    padding: 30px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    margin: 0 auto;
    max-width: 700px;
}

.response-box {
    background-color: #1e1e2f;
    padding: 20px;
    border-radius: 10px;
    margin-top: 10px;
    color: white;
    animation: fadeIn 1s ease-in-out;
    font-family: 'Fira Code', monospace;
    font-size: 15px;
    line-height: 1.6;
}

@keyframes fadeIn {
    0% { opacity: 0; transform: translateY(-10px); }
    100% { opacity: 1; transform: translateY(0); }
}
</style>

""", unsafe_allow_html=True)

st.markdown(
    "<div class='main'><h1>Lexiq</h1><h4>Experience the power of custom LLMs in a sleek playground</h4></div>",

    unsafe_allow_html=True
)


with st.form("prompt_form"):
    prompt = st.text_area(
        "Enter your prompt",
        height=150,
        placeholder="Start with something like: What's the future of AI?"
    )
    model = st.selectbox("Select a language model", ["mistral", "mixtral"])
    submitted = st.form_submit_button("Generate Response")
    st.markdown("</div>", unsafe_allow_html=True)

if submitted and prompt.strip():
    with st.spinner("Processing your request..."):
        start = time.time()
        response, token_count = get_model_response(prompt, model)
        latency = time.time() - start
        log_interaction(prompt, model, latency, token_count)

    
    st.markdown("### Response")
    st.markdown(f"""
    <div class="response-box">
        {response}
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown(f"""
    <br><div style="font-size: 14px; color: #ccc;">
        Response time: <b>{round(latency, 2)} seconds</b> &nbsp;&nbsp; | &nbsp;&nbsp; Token count: <b>{token_count}</b>
    </div>
    """, unsafe_allow_html=True)

elif submitted:
    st.error("Please enter a prompt to get started.")
