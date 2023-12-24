import openai
from llama_index.agent import OpenAIAgent
import streamlit as st
from llama_hub.tools.requests import RequestsToolSpec

openai_api_key = "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"
domain_headers = {
    "api.openai.com": {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json"
    },
    "127.0.0.1": {
        "Content-Type": "application/json"
    }
}

weather_agent = RequestsToolSpec(domain_headers=domain_headers).to_tool_list()
openai.api_key = openai_api_key

url = "http://127.0.0.1:5000/weather"
system_prompt = f"You're WeatherGPT, you goal is to answer me the weather prompts based on the user input, when a user prompts for the weather you make a GET API request to {url}?country=[TWO_DIGITS_COUNTRY_CODE]&city=[CITY] e.i {url}?country=FR&city=Paris"
agent = OpenAIAgent.from_tools(
    llm=openai.OpenAI(model="gpt-4", temperature=0.5, system_prompt=system_prompt),
    tools=weather_agent,
                               system_prompt=system_prompt)


# agent.chat_repl()
st.title("LLM Cool Chat UI")


# loads the chat agent
if "agent" not in st.session_state:
    st.session_state.agent = agent

# load messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Ask me something"
        }
    ]


if prompt := st.chat_input("Your prompt"):
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })


# load all messages from the messages array
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get a completion if the user entered a prompt
# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.agent.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            # Add response to message history
            st.session_state.messages.append(message)
