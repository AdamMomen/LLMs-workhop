from llama_index.agent import OpenAIAgent
from llama_hub.tools.requests import RequestsToolSpec
import openai
import streamlit as st

openai.api_key = "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"


tool_spec = RequestsToolSpec(
    domain_headers={
        'api.openai.com': {
            "Authorization": "Bearer sk-your-key",
            "Content-Type": "application/json",
        },
        '127.0.0.1': {
            "Content-Type": "application/json",
        }
    }
)


agent = OpenAIAgent.from_tools(
    tool_spec.to_tool_list(),
    system_prompt="You're WeatherGPT, When a user asks for the weather in spciefic city and country make a GET api request to http://127.0.0.1:5000/weather with the following paramas: city=[CITY]and country=[2-digits-Country-Code]."
)
# agent.chat_repl()


st.set_page_config()
st.title("")


if "agent" not in st.session_state:
    st.session_state.agent = agent


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me about the weather of any city"}
    ]

if prompt := st.chat_input("Your Prompt"):
    st.session_state.messages.append({"role": "user", "content": prompt})

for m in st.session_state.messages:
    with st.chat_message(m['role']):
        st.write(m['content'])


if st.session_state.messages[-1]["role"] != "assistant":
    with st.spinner(""):
        with st.chat_message("assistant"):
            response = st.session_state.agent.chat(prompt)

            message = {"role": "assistant", "content": response.response}
            st.write(response.response)
            st.session_state.messages.append(message)
