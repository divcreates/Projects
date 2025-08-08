# 🧠 WikiBuilder – Your AI-Powered Wikipedia Article Generator

WikiBuilder is an intelligent multi-agent app built with **CrewAI** and **Streamlit** that takes a user prompt and generates a clean, well-structured Wikipedia-style article with images, formatted sections, and live logging.

**Built By Div ❤️**  
**3rd Year Internship Project – SBSSU x IIT Jammu (Summer 2025)**

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
  → Data Extractor limits web searches  
  → Summarizer consolidates info  
  → Formatter produces polished Markdown in Wikipedia-style.

- **Inbuilt CrewAI WebSearchTool:**  
  → No external SDKs – self-contained and efficient.

- **Sidebar TOC & Metadata:**  
  → Clean Table of Contents using anchors, real-time generation stats.

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
├── main.py              # Streamlit frontend
├── test_system.py       # CLI-based agent pipeline test
├── requirements.txt
├── .env                 # API key config (ignored)
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone this Repository

```bash
git clone https://github.com/divcreates/Projects.git
cd Projects/Wiki-Builder
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add OpenAI API Key

Create a `.env` file:

```
OPENAI_API_KEY=your-secret-key-here
```

### 5. Run the App

```bash
streamlit run main.py
```

---

## 🧪 Optional: Run Agents in Terminal

```bash
python test_system.py
```

Use this to test the full Crew pipeline before launching UI.

---

## 🧠 Notes

- **Missing images?** → Wikipedia sometimes lacks image metadata  
- **Slow output?** → Consider async agent execution  
- **Terminal errors?** → Ignore benign dependency warnings

---

## ❤️ Built By Div
