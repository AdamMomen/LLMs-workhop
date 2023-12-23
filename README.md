## WTF is this?
Welcome to our Coding Workshop in Canggu, Bali, where we're building a state-of-the-art Language Learning Model (LLM) chatbot. This chatbot is designed to handle weather-related queries and tasks, making it a perfect fit for anyone interested in integrating AI into weather applications.

### Requirements
To participate in this workshop, you'll need:
1. A functioning body and mind, ready for learning.
2. A computer capable of handling programming tasks.
3. An OPENAI API key. Please obtain one from [OpenAI](https://platform.openai.com/account/api-keys).

### Getting Started

#### Setup
Follow these steps to set up your development environment:

1. Make the setup script executable by running `chmod +x setup.sh` in your terminal.
2. Execute the setup script with `./setup.sh` allow the script to work its magic, which includes:
    - Installing pyenv using `curl https://pyenv.run | $SHELL`.
    - Installing Python version 3.11.0 with `pyenv install 3.11.0`.
    - For Linux: Installing virtualenv and tmux using `apt install virtualenv tmux`.
    - For Mac: Installing virtualenv using `brew install virtualenv`.
    - Creating a virtual environment with `virtualenv venv -p $PYENV_ROOT/shims/python3.11`.
    - Activating the virtual environment using `source ./venv/bin/activate`.
    - Installing required Python dependencies with `pip install -r requirements.txt`.

#### Running The Code
To run the script you will have to run `streamlit run main.py`

###  Tasks
We will be covering the following tasks:
- [ ] Setting up the OpenAI chat agent.
- [ ] Creating an interactive chat interface using Streamlit.
- [ ] Modifying the system prompt for personalized interactions.
- [ ] Building a robust Flask-based weather server.
- [ ] Integrating the weather server with the chat agent for real-time responses.
- [ ] Bonus Task: Indexing messages from the [Bali Nomad Coders WhatsApp group](https://chat.whatsapp.com/InC6F7Z8qrdH5wIxXLjWnm) for coding.
- [ ] Bonus Task: Implementing RAG (Retrieval-Augmented Generation) on indexed documents and enabling ChatGPT to perform contextual conversations.

### Useful Links
Here are some resources to help you along the way:
- [Llama Index](https://www.llamaindex.ai/): A tool for indexing and searching through large datasets.
- [Llama Hub](https://llamahub.ai/): A platform for exploring various LLM applications.
- [Streamlit](https://streamlit.io/): Our go-to toolkit for creating interactive and beautiful web apps for machine learning and data science.

### Community
Join our vibrant [community](https://chat.whatsapp.com/InC6F7Z8qrdH5wIxXLjWnm) of learners and experts. Share your progress, ask questions, and collaborate on exciting projects.

### Support
If you encounter any issues or have questions, don't hesitate to reach out through our community WA group or directly to the workshop organizers.

Happy Coding, and let's build something coool together!
