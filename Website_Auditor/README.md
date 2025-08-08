# 🤖 AI Website Auditor

An AI-powered website analysis tool that scrapes a site’s content and delivers SEO, accessibility, and performance recommendations using OpenAI’s GPT-4o model.

**Built By Div ❤️**  
**3rd Year Internship Project – SBSSU x IIT Jammu (Summer 2025)**

---

## 📋 Project Overview
This project demonstrates how to combine web scraping, large language models (LLMs), and a modern Python UI to create a real-world AI tool.

The app:

1. Scrapes the raw HTML of a given website.  
2. Extracts basic SEO and accessibility signals (title, meta description, headers, image alt tags).  
3. Sends the data to OpenAI GPT-4o for analysis.  
4. Displays a structured report using a sleek Gradio interface.

---

## 🔑 Key Features
- 🧠 **AI-Driven Audit** – Powered by OpenAI GPT-4o  
- 🧰 **No Browser Needed** – Uses `requests` + `BeautifulSoup` (lightweight & fast)  
- 🎯 **Overall + Category Scores** – SEO, accessibility, and performance  
- ⚡ **Live Feedback** – Users see scraping + AI analysis in real time  
- 🧼 **Minimal Setup** – Single-file, Gradio-based interface  

---

## 🛠 Tech Stack

| Layer        | Technology              |
|--------------|--------------------------|
| Frontend UI  | Gradio                   |
| Backend      | Python 3.8+              |
| Scraping     | Requests, BeautifulSoup4 |
| AI Model     | OpenAI GPT-4o            |
| Config Mgmt  | python-dotenv            |

---

## 📂 Project Structure

```
ai-website-auditor/
├── app.py              # Main application script (UI + logic)
├── requirements.txt    # Python dependencies
├── .env                # API key config (not committed)
└── README.md           # You're here
```

---

## 🚀 Quick Start

### 1. Clone this repository
```bash
git clone https://github.com/divcreates/ai-website-auditor.git
cd ai-website-auditor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API key  
Create a `.env` file:
```
OPENAI_API_KEY=sk-your-openai-key-here
```

### 4. Run the application
```bash
python app.py
```

Then open [http://127.0.0.1:7860](http://127.0.0.1:7860) in your browser.

---

## 🧠 How It Works

1. **Scrape:**  
   → `requests` downloads the HTML, `BeautifulSoup` parses it.

2. **Extract:**  
   → Title, meta description, number of `<h1>` tags, and image alt text.

3. **Analyze:**  
   → A GPT-4o prompt is crafted and sent to OpenAI.

4. **Render:**  
   → GPT’s response is styled with HTML and displayed using Gradio.

---

## 📌 Example Audit

- 🔍 **SEO Score:** 85/100  
- 🧩 **Accessibility Score:** 90/100  
- 🚀 **Performance Score:** 78/100  

✅ Recommendations and findings appear in clear, color-coded sections.

---

## 🤝 Credits

- [OpenAI](https://openai.com/) – for the GPT-4o API  
- [Gradio](https://www.gradio.app/) – for interactive Python UIs  
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) – for clean HTML parsing  

---

**🧑‍💻 Internship Project by Div**  
**SBSSU Gurdaspur · Summer 2025 @ IIT Jammu**

_“Learning by Building.”_
