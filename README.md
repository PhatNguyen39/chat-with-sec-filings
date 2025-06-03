# chat-with-sec-filings
# 💬 Chat with SEC Filings (Powered by Mistral + Ollama)

A lightweight local LLM-powered Streamlit app that allows you to **chat with U.S. SEC filings (10-K, 10-Q, etc.)** using **Mistral** via [Ollama](https://ollama.com). Upload a filing, ask questions, and get contextual answers — all running **entirely on your Mac**.

---

## 🧠 Features

- ✅ Ask natural language questions about SEC filings
- ✅ Locally run LLM (Mistral) using Ollama
- ✅ Embedding and retrieval of long documents
- ✅ Clean, interactive Streamlit interface
- ✅ Fully offline, private, and free to use

---

## 🚀 Quickstart (Mac with M1/M2)

### 1. Clone the repo

### 2. Create a Conda environment
``` bash
conda create -n secchat python=3.10 -y
conda activate secchat
```
### 3. Install dependencies
``` bash
pip install -r requirements.txt
```

### 4. Install and start Ollama (Mistral model)
Install via Homebrew:
``` bash
brew install ollama
```
Start the Ollama service:
``` bash
ollama serve
```
Then pull and run Mistral:
``` bash
ollama run mistral
```
Leave it running in the background.

###5. Run the Streamlit app
In a new terminal tab:
``` bash
conda activate secchat
streamlit run app.py
```

Optional: Share with Friends
Want to share your app over the internet? Use ngrok:

``` bash
brew install ngrok
ngrok config add-authtoken YOUR_AUTHTOKEN
ngrok http 8501
```
📜 License
MIT License – free to use and modify!

🙋‍♀️ Author
Built with ❤️ by Phat Nguyen
