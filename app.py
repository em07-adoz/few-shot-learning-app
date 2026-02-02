import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="🧠 Gemini Prompt Lab", layout="centered")
st.title("💬 Few-shot learning app - Prompt Playground")

# Input API key
api_key = st.text_input("🔑 Enter your Gemini API key", type="password")

if api_key:
    genai.configure(api_key=api_key)

    # Session state to store past interactions
    if "history" not in st.session_state:
        st.session_state.history = []

    # Get available models
    try:
        available_models = [m.name.replace('models/', '') for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # st.info(f"📋 Available models: {', '.join(available_models)}")
        selected_model = st.selectbox("Select Model", available_models, index=0)
    except Exception as e:
        st.error(f"Could not fetch available models: {e}")
        selected_model = "gemini-pro"

    # Prompt input
    st.subheader("📝 Enter a prompt:")
    user_prompt = st.text_area("Prompt", placeholder="Type something like 'Text generation...'")

    # Parameters
    with st.expander("⚙️ Generation Settings"):
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
        top_p = st.slider("Top-p", 0.0, 1.0, 0.9)
        top_k = st.slider("Top-k", 0, 100, 40)
        max_tokens = st.slider("Max Output Tokens", 10, 2048, 512)

    # Submit button
    if st.button("🚀 Generate Response") and user_prompt.strip():
        with st.spinner("Generating..."):
            try:
                model = genai.GenerativeModel(selected_model)
                response = model.generate_content(
                    user_prompt,
                    generation_config={
                        "temperature": temperature,
                        "top_p": top_p,
                        "top_k": top_k,
                        "max_output_tokens": max_tokens,
                    },
                    safety_settings=[
                        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": 4},
                        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": 4},
                        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": 4},
                        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": 4},
                    ]
                )
                answer = response.text.strip()
                st.session_state.history.append((user_prompt, answer))  # save in history
            except Exception as e:
                error_msg = str(e)
                if "quota" in error_msg.lower() or "429" in error_msg:
                    st.error(f"❌ **Quota Exceeded**: You've hit the free tier limit. Please:\n1. Wait until tomorrow for daily limits to reset\n2. Upgrade to a paid plan at [ai.google.com](https://ai.google.com)\n\nDetails: {e}")
                else:
                    st.error(f"❌ Error: {e}")

    # Display chat history
    if st.session_state.history:
        st.subheader("🧾 Past Prompts and Responses")
        for idx, (prompt, reply) in enumerate(reversed(st.session_state.history), 1):
            with st.expander(f"🟦 Prompt {len(st.session_state.history) - idx + 1}"):
                st.markdown(f"**📝 Prompt:**\n\n{prompt}")
                st.markdown(f"**💡 Response:**\n\n{reply}")