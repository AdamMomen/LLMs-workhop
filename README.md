## WTF is this?
This is a Coding workshop where we build LLM chatbot for setting up weather application in Canggu, Bali.

### Requirements
1. Functioning body and mind
2. Computer
3. OPENAI [api-key](https://platform.openai.com/account/api-keys) (I'm broke :( )

### Getting Started

#### Env Setup
1. Make setup.sh executable by running `chmod +x setup.sh`
2. Run the setup script `./setup.sh`
3. Let it do the magic, basically it will:
    -  Install pyenv by running `curl https://pyenv.run] | $SHELL`
    -  Install pythonversoin 3.11.0 `pyenv install 3.11.0`
    -  Linux: `apt install virtualenv tmux` | Mac: `brew install virtualenv`
    -  Run `virtualenv venv -p $PYENV_ROOT/shims/python3.11`
    -  Run `source ./venv/bin/activate`
    -  Install python dependencies `pip install -r rqeuirements.txt`


#### Building Blocks
### Tasks

- [ ] Set up the OpenAI chat agent.
- [ ] Create an interactive chat interface with Streamlit.
- [ ] Modify the system prompt.
- [ ] Build a Flask-based weather server.
- [ ] Integrate the weather server with the agent.
- [ ] Bonus: Index messages from the [Bali Nomad Coders WhatsApp group](https://chat.whatsapp.com/InC6F7Z8qrdH5wIxXLjWnm).
- [ ] Bonus: Execute RAG (Retrieval-Augmented Generation) on indexed documents and enable ChatGPT to interact.



#### Links:
- [llamaindex](https://www.llamaindex.ai/)
- [Llama Hub](https://llamahub.ai/)
- [Streamlit](https://streamlit.io/)

