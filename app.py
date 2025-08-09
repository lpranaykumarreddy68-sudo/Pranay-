import streamlit as st
import openai

# 🔐 Set your OpenAI API key here
openai.api_key = "your-api-key"

# 🌟 Function to generate prompt using OpenAI API
def generate_prompt(topic, temperature=0.7):
    prompt = f"Give me a creative idea and prompt related to {topic}."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=temperature,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"❌ Error: {str(e)}"

# 🖼️ Streamlit App UI
st.set_page_config(page_title="AI Prompt Generator", layout="centered")
st.title("🧠 AI Prompt Generator")
st.write("Enter a topic and get a creative idea and writing prompt!")

# 🚪 Input
topic = st.text_input("Enter a topic:", placeholder="e.g., futuristic farming")

temperature = st.slider("Creativity level", 0.0, 1.0, 0.7)

# ▶️ Button to generate
if st.button("Generate Prompt"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating..."):
            output = generate_prompt(topic, temperature)
        st.markdown("### ✨ Result:")
        st.success(output)