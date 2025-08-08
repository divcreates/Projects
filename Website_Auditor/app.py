import gradio as gr 
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import os
import re
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Website Scraper Function
def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        return {
            'title': soup.title.string.strip() if soup.title else 'No title',
            'description': soup.find('meta', {'name': 'description'}).get('content').strip() if soup.find('meta', {'name': 'description'}) else 'No description',
            'h1_count': len(soup.find_all('h1')),
            'img_without_alt': len([img for img in soup.find_all('img') if not img.get('alt')])
        }
    except Exception as e:
        print(f"[Scrape Error] {e}")
        return None

# GPT-4o Analysis Function
def analyze_with_ai(data):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    prompt = f"""
Act as a professional SEO auditor. Analyze this website data and produce a structured report.

Title: {data['title']}
Description: {data['description'][:500]}...
H1 tags: {data['h1_count']}
Images missing alt: {data['img_without_alt']}

Format:

OVERALL SCORE: [score]/100

CATEGORY SCORES:
• SEO: [score]/100
• Accessibility: [score]/100
• Performance: [score]/100

KEY FINDINGS:
• [finding 1]
• [finding 2]
• [finding 3]

TOP RECOMMENDATIONS:
🔴 HIGH PRIORITY: ...
🟡 MEDIUM PRIORITY: ...
🔵 LOW PRIORITY: ...
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Format output as HTML
def format_analysis(analysis):
    if not analysis:
        return "No analysis available."

    formatted = analysis.replace('\n\n', '<br><br>').replace('\n', '<br>')
    formatted = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', formatted)

    # Styled section headers
    formatted = re.sub(r'OVERALL SCORE:', '<h2 style="color: #4CAF50;">🎯 OVERALL SCORE:</h2>', formatted)
    formatted = re.sub(r'CATEGORY SCORES:', '<h3 style="color: #2196F3;">📊 CATEGORY SCORES:</h3>', formatted)
    formatted = re.sub(r'KEY FINDINGS:', '<h3 style="color: #FF9800;">🔍 KEY FINDINGS:</h3>', formatted)
    formatted = re.sub(r'TOP RECOMMENDATIONS:', '<h3 style="color: #9C27B0;">💡 TOP RECOMMENDATIONS:</h3>', formatted)

    return f'''
<div style="font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; background: #121212; color: #F5F5F5; border-radius: 10px;">
    {formatted}
</div>
'''

# Full Workflow
def audit_website(url):
    if not url.strip():
        return "Please enter a website URL."
    if not url.startswith('http'):
        url = 'https://' + url

    yield "🔄 Scraping website content..."
    data = scrape_website(url)
    if not data:
        yield "❌ Failed to scrape website. Please check the URL."
        return

    yield "🤖 Analyzing with GPT-4o..."
    try:
        analysis = analyze_with_ai(data)
        yield format_analysis(analysis)
    except Exception as e:
        yield f"❌ Error during AI analysis: {str(e)}"

# Custom CSS (Fix double scrollbar + improve visuals)
css = """
#component-1 {
    overflow: visible !important;
    max-height: none !important;
}
body {
    scroll-behavior: smooth;
}
h1 {
    text-align: center;
}
"""

# Gradio Interface
with gr.Blocks(css=css) as interface:
    gr.HTML("<h1 style='text-align: center; color: white;'>🤖 AI Website Auditor – Built By Div ❤️</h1>")
    gr.Markdown("Enter any website to audit **SEO**, **accessibility**, and **performance** using GPT-4o.")

    with gr.Row():
        url_input = gr.Textbox(label="🌐 Website URL", placeholder="example.com", lines=1)
    
    result_output = gr.HTML(label="📋 Analysis Results", elem_id="component-1")

    submit_btn = gr.Button("🚀 Run Audit")

    submit_btn.click(fn=audit_website, inputs=url_input, outputs=result_output)

    gr.Examples(
        [["google.com"], ["wikipedia.org"], ["bbc.com"]],
        inputs=url_input
    )

interface.queue()

if __name__ == "__main__":
    print("Launching AI Website Auditor...")
    print("Visit the interface at http://localhost:7860")
    print("Press Ctrl+C to stop the server.")
    print("Built with ❤️  - By Div")
    interface.launch()
