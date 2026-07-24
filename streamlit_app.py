import streamlit as st
from chatbot import ask
import time

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="MiniGPT",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# LOAD CSS
# =====================================================

with open("styles/style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =====================================================
# SESSION STATE
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.image("assets/logo.png", use_container_width=True)

    st.markdown(
        """
        <div style="text-align:center;margin-top:-15px;">
            <p style="color:gray;">Your Personal AI Assistant</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


    user_messages = len(
        [m for m in st.session_state.messages if m["role"] == "user"]
    )

    ai_messages = len(
        [m for m in st.session_state.messages if m["role"] == "assistant"]
    )

    total_messages = len(st.session_state.messages)

    col1, col2 = st.columns(2)

    col1.metric("User", user_messages)
    col2.metric("AI", ai_messages)

    st.metric("Total", total_messages)

    st.markdown("---")

    if st.button("🗑 New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    # Export Chat

    chat_text = ""

    for msg in st.session_state.messages:

        chat_text += (
            f"{msg['role'].upper()}\n"
            f"{msg['content']}\n\n"
        )

    st.download_button(
        "💾 Export Chat",
        data=chat_text,
        file_name="MiniGPT_Chat.txt",
        mime="text/plain",
        use_container_width=True
    )

    st.markdown("---")

# =====================================================
# HEADER
# =====================================================

col1, col2, col3 = st.columns([1,2,1])

st.markdown(
    """
<div class="main-title">
🤖 MiniGPT
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="subtitle">
Powered by Gemini 3.5 Flash Lite
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# =====================================================
# WELCOME SCREEN
# =====================================================

if len(st.session_state.messages) == 0:

    st.markdown(
        """
        <h2 style='text-align:center;'>
        👋 Welcome 
        </h2>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p style='text-align:center;font-size:18px;color:#BDBDBD'>
        Your AI assistant is ready.
        Try one of the suggestions below.
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("💻 Explain Python", use_container_width=True):
            st.session_state.prompt = "Explain Python for beginners."

        if st.button("📧 Write Email", use_container_width=True):
            st.session_state.prompt = "Write a professional email."

    with col2:

        if st.button("🧠 Explain AI", use_container_width=True):
            st.session_state.prompt = "Explain Artificial Intelligence."

        if st.button("🚀 Startup Idea", use_container_width=True):
            st.session_state.prompt = "Give me a startup idea."

    st.write("")
    st.divider()

# =====================================================
# DISPLAY CHAT
# =====================================================

for message in st.session_state.messages:

    avatar = "👤"

    if message["role"] == "assistant":
        avatar = "🤖"

    with st.chat_message(message["role"], avatar=avatar):

        st.markdown(message["content"])

# =====================================================
# CHAT INPUT
# =====================================================

prompt = st.chat_input("Ask me anything broo...")

# Use suggested prompt if clicked
if "prompt" in st.session_state:
    prompt = st.session_state.prompt
    del st.session_state.prompt

# =====================================================
# PROCESS USER INPUT
# =====================================================

if prompt:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Show user message
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # AI Response
    with st.chat_message("assistant", avatar="🤖"):

        start_time = time.time()

        with st.spinner("MiniGPT is thinking..."):

            try:

                response = ask(prompt)

            except Exception as e:

                response = f"❌ Error:\n\n{e}"

        end_time = time.time()

        response_time = round(end_time - start_time, 2)

        st.markdown(response)

        st.caption(f"⚡ Response generated in {response_time} sec")

    # Save AI message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    st.rerun()

# =====================================================
# FOOTER
# =====================================================

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.caption("🤖 MiniGPT v1.0")

with col2:
    st.caption("Powered by Gemini 3.5 Flash Lite")

with col3:
    st.caption("Built with ❤️ by Ganesh")
