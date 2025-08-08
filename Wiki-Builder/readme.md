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

---

## 🛠 How It Works

- **Agent Collaboration:**  
  Data Extractor limits web searches → Summarizer consolidates info → Formatter produces polished Markdown in Wikipedia-style.

- **Inbuilt CrewAI WebSearchTool:**  
  No external search SDK required, improving integration and control.

- **Clickable Sidebar TOC:**  
  Uses `st.header(…, anchor=…)` and sidebar anchor links.

- **Images:**  
  Inline display of Wikipedia lead images with graceful fallback.

- **Performance Measurement:**  
  Measures generation time precisely between start and end of the multi-agent process.

---

## 🧪 Test Script

Before launching the Streamlit UI, you can run `test_system.py` to test the full agent pipeline in the terminal.

```bash
python test_system.py
```

This will:
- ✅ Run all agents (extractor, summarizer, formatter)  
- ✅ Print the final article to console  
- ✅ Help debug before using the UI

---

## 🔧 Customization & Extensions

- Modify agent prompts or increase/decrease search query limits in `agents/data_extractor.py` prompt.  
- Adjust UI styling in `main.py` CSS.  
- Add fallback images if Wikipedia images are missing.  
- Extend CrewAI pipeline with custom agents or tools.

---

## 📂 Project Structure

```
Wiki-Builder/
│
├── agents/
│   ├── __init__.py
│   ├── data_extractor.py
│   ├── summarizer.py
│   └── page_formatter.py
│
├── crew.py
├── main.py                  # Streamlit frontend
├── test_system.py           # Test full pipeline (CLI-based)
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup & Installation

Follow these steps to get the project running on your local machine.

### **Prerequisites**

- Python **3.12** (recommended)  
- An OpenAI API Key  

### **Step 1: Clone or Set Up the Project**

Create the project directory and files as described in the project structure.

### **Step 2: Create a Virtual Environment**

Use a virtual environment to manage dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### **Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 4: Add Your OpenAI API Key**

Create a file named `.env` in the root of your project directory and add your key:

```env
OPENAI_API_KEY=your-secret-api-key-here
```

> ✅ Tip: The `.env` file is usually in `.gitignore` to avoid accidentally exposing your key.

### **Step 5: Run the Application**

```bash
streamlit run main.py
```

The app will open in your browser. Enter a topic and let the AI generate your Wikipedia-style article!

---

## ⚠️ Troubleshooting

- **Missing images?**  
  Some topics may lack Wikipedia images — this isn’t an error.

- **Slow generation?**  
  Enable async execution and streaming in CrewAI agent config.

- **Pydantic warnings?**  
  These are dependency-related. Can be ignored or resolved by upgrading packages.

---

## ❤️ Built By Div
