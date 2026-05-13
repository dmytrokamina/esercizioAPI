import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Завантаження змінних з файлу .env в оточення ОС
load_dotenv()

st.title("🤖 Стрімліт + OpenRouter через .env")

user_prompt = st.text_input("Ваше запитання до ШІ:", "Привіт! Напиши один рядок коду на Python.")

if st.button("Надіслати запит"):
    with st.spinner("З'єднання з сервером..."):
        try:
            # Зчитування ключа з системних змінних, куди його завантажив dotenv
            api_key = os.getenv("OPENROUTER_API_KEY")
            
            # Перевірка наявності ключа перед відправкою
            if not api_key:
                st.error("Помилка: Ключ OPENROUTER_API_KEY не знайдено у файлі .env")
                st.stop()

            # Ініціалізація клієнта
            client = OpenAI(
                base_url="openrouter.ai",
                api_key=api_key,
            )

            # Запит до безкоштовної моделі
            completion = client.chat.completions.create(
                model="google/gemini-2.5-flash:free",
                messages=[{"role": "user", "content": user_prompt}]
            )

            st.success("Відповідь отримана:")
            st.write(completion.choices.message.content)

        except Exception as e:
            st.error(f"Виникла помилка: {e}")