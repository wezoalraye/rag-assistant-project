import streamlit as st
from api_client import query

st.set_page_config(
    page_title="ML Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
    }
    .title {
        text-align: center;
        color: #00d4ff;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        color: #888;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    .source-box {
        background-color: #1e2130;
        border-left: 3px solid #00d4ff;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="title">🤖 ML Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ask anything about Machine Learning</p>', unsafe_allow_html=True)
st.divider()

# Sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/TensorFlowLogo.svg/1200px-TensorFlowLogo.svg.png", width=100)
    st.title("📚 About")
    st.write("This assistant answers ML questions from:")
    st.write("- Bishop PRML")
    st.write("- Intro to ML with Python")
    st.write("- Understanding ML")
    st.divider()
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if "sources" in message:
            st.markdown(f'<div class="source-box">📚 <b>Sources:</b> {message["sources"]}</div>', unsafe_allow_html=True)

if prompt := st.chat_input("Ask a question about ML..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🔍 Searching documents..."):
            result = query(prompt)
            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                st.write(result["answer"])
                sources = ', '.join(result['sources'])
                st.markdown(f'<div class="source-box">📚 <b>Sources:</b> {sources}</div>', unsafe_allow_html=True)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": result["answer"],
                    "sources": sources
                })