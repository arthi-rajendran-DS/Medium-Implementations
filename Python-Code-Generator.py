import streamlit as st
import openai

# Set the OpenAI API key
openai.api_key = "Your_API_Key" #Modify with your API key

# Create a function to generate Python code from English text
def generate_code(prompt):
  completions = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=4024,
      n=1,
      stop=None,
      temperature=0.5,
  )

  message = completions.choices[0].text
  return message

# Create the Streamlit app UI
st.title("Python Code Generator")

# Get the English prompt from the user
prompt = st.text_input("Enter the logic/Name of the Algorithm prompt:")

# Generate the Python code and display it
if prompt:
  prompt = "Write a Python code to implement" + prompt
  code = generate_code(prompt)
  st.code(code)
