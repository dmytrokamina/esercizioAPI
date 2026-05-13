import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

st.title("Streamlit")

user_prompt = st.text_input("La tua domanda:", "Ciao! Quale fiume è piu lungo in Italia.")

if st.button("Send"):
    with st.spinner("Collegamento..."):
        try:
            
            api_key = os.getenv("OPENROUTER_API_KEY")
            
            
            if not api_key:
                st.error("Errore")
                st.stop()

            
            client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=api_key,
            )

            # Запит до безкоштовної моделі
            completion = client.chat.completions.create(
                model="google/gemini-2.5-flash:free",
                messages=[{"role": "user", "content": user_prompt}]
            )

            st.success("d:")
            st.write(completion.choices.message.content)

        except Exception as e:
            st.error(f"Errore: {e}")