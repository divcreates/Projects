# 🧠 WikiBuilder - Your AI-Powered Wikipedia Article Generator

WikiBuilder is an intelligent multi-agent app built with CrewAI and Streamlit that takes a user prompt and generates a clean, well-structured Wikipedia-style article with images, formatted sections, and live logging.

---

## 🚀 Features

- ✅ Minimal, distraction-free Streamlit UI
- ✅ Auto-generated Wikipedia-style article with lead image
- ✅ Real-time logging in terminal
- ✅ Clickable Table of Contents in sidebar
- ✅ Metadata (image, time taken, word count)
- ✅ Built-in WebSearchTool – no external API needed
- ✅ You can Test the multi-agent Wikipedia builder system directly from the terminal: python test_system.py (Use this to verify your setup before launching the Streamlit app.)


---

## 🛠 How It Works

- **Agent Collaboration:** Data Extractor limits web searches; Summarizer consolidates info; Formatter produces polished Markdown in WikiPedia-Style.
- **Inbuilt CrewAI WebSearchTool:** No external search SDK required, improving integration and control.
- **Clickable Sidebar TOC:** Uses `st.header(…, anchor=…)` and sidebar anchor links.
- **Images:** Inline display of Wikipedia lead images with graceful fallback.
- **Performance Measurement:** Measures generation time precisely between start and end of the multi-agent process.

---

## 🔧 Customization & Extensions

- Modify agent prompts or increase/decrease search query limits in `agents/data_extractor.py` prompt.
- Adjust UI styling in `main.py` CSS.
- Add fallback images if Wikipedia images are missing.
- Extend CrewAI pipeline with custom agents or tools.

-----

## 📂 Project Structure

```
Wiki-Builder/
│
├── 📂 agents/
│   ├── 📄 __init__.py
│   ├── 📄 data_extractor.py
│   ├── 📄 summarizer.py
│   └── 📄 page_formatter.py
│
├── 📄 crew.py
├── 📄 main.py
├── 📄 requirements.txt
├── 📄 .env
└── 📄 README.md
```

---

## ⚙️ Setup & Installation

Follow these steps to get the project running on your local machine.

### **Prerequisites**

-   Python **3.12** (recommended)
-   An OpenAI API Key

### **Step 1: Clone or Set Up the Project**

Create the project directory and files as described in the project structure.

### **Step 2: Create a Virtual Environment**

It's highly recommended to use a virtual environment to manage dependencies.

```
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### **Step 3: Install Dependencies**

Install all the necessary packages from the `requirements.txt` file.

```
pip install -r requirements.txt
```

### **Step 4: Add Your OpenAI API Key**

Create a file named `.env` in the root of your project directory and add your OpenAI API key to it.

```
OPENAI_API_KEY=your-secret-api-key-here
```
> **Note:** The `.env` file is included in `.gitignore` by default in many projects to prevent accidentally committing secret keys.

### **Step 5: Run the Application**

Once the setup is complete, you can run the Streamlit application.

```
streamlit run main.py
```

The application will open in your default web browser. Enter a topic, and watch the multi-agent system create a Wikipedia article for you!

---

## ⚠️ Troubleshooting

- Missing images indicate Wikipedia data absence, not an error.
- Slow performance? Enable async execution and streaming in CrewAI agents.
- Pydantic warnings? They are from dependencies and can be safely ignored or fixed by updating packages.

---

## ❤️ Built By Div
```
