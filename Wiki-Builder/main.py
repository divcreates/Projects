import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv
import requests
import re
from crew import run_crew

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Wikipedia Builder", page_icon="📖", layout="wide", initial_sidebar_state="expanded")

# Session state
for key in ("result", "sections", "headings", "image_url", "generated_time", "topic"):
    if key not in st.session_state:
        if key in ("sections", "headings"):
            st.session_state[key] = []
        else:
            st.session_state[key] = None

# CSS
st.markdown("""
<style>
.stApp { background-color:#0e1117; color:#fafafa; }
.main .block-container { padding-top:2rem; padding-bottom:2rem; max-width:1200px; }
.sidebar-footer { position:fixed; bottom:15px; left:15px; font-size:0.9rem; color:#8b949e; z-index:999; }
.sidebar-content { padding:1rem; color:#fafafa; }
.toc-heading { font-weight:bold; font-size:1.1rem; margin-bottom:0.5rem; }
.toc-item { margin:0.25rem 0; padding-left:0.5rem; }
.toc-item a { color:#58a6ff; text-decoration:none; }
.toc-item a:hover { text-decoration:underline; }
</style>
""", unsafe_allow_html=True)

def fetch_image(topic):
    try:
        r = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}", timeout=5)
        return r.json().get('thumbnail', {}).get('source')
    except:
        return None

def parse_sections(md):
    sections = []
    current = None
    for line in md.splitlines():
        m = re.match(r"^(#{1,3})\s+(.*)", line)
        if m:
            if current:
                sections.append(current)
            hashes = m.group(1)
            heading = m.group(2).strip()
            anchor = re.sub(r'[\s\W]+','-', heading.lower())
            level = {1: 'h1', 2: 'h2', 3: 'h3'}[len(hashes)]
            current = {'level': level, 'anchor': anchor, 'heading': heading, 'content': ''}
        else:
            if current:
                current['content'] += line + "\n"
    if current:
        sections.append(current)
    return sections

# Page header & form
st.markdown(
    '<div style="text-align:center;">'
    '<h1>📖 Wikipedia Builder 📖</h1>'
    '<p style="color:#8b949e;">Generate detailed Wikipedia-style articles using AI agents</p>'
    '</div>',
    unsafe_allow_html=True
)
with st.form("wiki_form"):
    keyword = st.text_input("Enter a topic:", placeholder="e.g., Ancient Rome, Quantum Physics...")
    submitted = st.form_submit_button("🚀 Generate Wikipedia Article")

# Article generation (with proper timing)
if submitted and keyword:
    start_time = datetime.now()
    with st.spinner("Generating article…"):
        raw = run_crew(keyword.strip())
        sections = parse_sections(raw)
        headings = [(s['level'], s['heading'], s['anchor']) for s in sections]
        st.session_state.result = raw
        st.session_state.sections = sections
        st.session_state.headings = headings
        st.session_state.image_url = fetch_image(keyword)
        st.session_state.topic = keyword.strip()
    end_time = datetime.now()
    st.session_state.generated_time = round((end_time - start_time).total_seconds(), 2)
    st.success(f"✅ Done in {st.session_state.generated_time} seconds")

# Sidebar TOC (always built from st.session_state.headings)
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.markdown('<div class="toc-heading">📋 Table of Contents</div>', unsafe_allow_html=True)
    if st.session_state.headings:
        for level, heading, anchor in st.session_state.headings:
            indent = 'margin-left:1em;' if level == 'h3' else ''
            st.markdown(
                f'<div class="toc-item" style="{indent}"><a href="#{anchor}">🔗 {heading}</a></div>',
                unsafe_allow_html=True
            )
    else:
        st.markdown('<div class="toc-item"><em>Generate an article to see contents</em></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-footer">Built by Div &#10084;&#65039;</div>', unsafe_allow_html=True)

# Article display (image shows with first h1 section)
if st.session_state.sections:
    st.markdown('---', unsafe_allow_html=True)
    for idx, s in enumerate(st.session_state.sections):
        if idx == 0 and st.session_state.image_url:
            st.markdown(
                f'<img src="{st.session_state.image_url}" '
                'style="float:right;width:250px;margin:0 0 1rem 1rem;border:1px solid #3d4451;border-radius:5px;">',
                unsafe_allow_html=True
            )
        if s['level'] == 'h1':
            st.header(s['heading'], anchor=s['anchor'])
        elif s['level'] == 'h2':
            st.subheader(s['heading'], anchor=s['anchor'])
        elif s['level'] == 'h3':
            st.markdown(f'<h3 id="{s["anchor"]}">{s["heading"]}</h3>', unsafe_allow_html=True)
        if s['content'].strip():
            st.markdown(s['content'].strip())
    st.markdown('---', unsafe_allow_html=True)
    st.info(f"📅 Generated in {st.session_state.generated_time} seconds")
    st.info("🔄 Enter a new topic above to generate another article")
