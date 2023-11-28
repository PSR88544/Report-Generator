import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

st.title("Report Generator App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def report(problem_statement, Requirements, Code, Suggestion):
    # Instantiate LLM model
    llm = OpenAI(model_name="text-davinci-003", openai_api_key=openai_api_key)
    # Prompt
    template = """Assuming You are a student, Write a report for following Problem Statement ,using the given information:
                  Problem Statement:{problem_statement}
                  Code:{Code}
                  Requirements:{Requirements} 
                  Sugestions:{Suggestion}"""
    prompt = PromptTemplate(input_variables=[
                            "problem_statement", "Requirements", "Code", "Suggestion"], template=template)
    prompt_query = prompt.format(problem_statement=problem_statement,
                                 Requirements=Requirements, Code=Code, Suggestion=Suggestion)
    # Run LLM model
    response = llm(prompt_query)
    # Print results
    return st.info(response)


with st.form("myform"):

    topic_text = st.text_input("Enter Problem Statement:", "")
    Requirements = st.text_input("Enter any special Requirements:", "")
    Suggestion = st.text_input("Any Suggestions:", "")
    Code = st.text_input("Enter the code Commands:",
                         "Don't Add or use any code")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Add your OpenAI API key to continue.")
    elif submitted:
        report(topic_text, Requirements, Code, Suggestion)
