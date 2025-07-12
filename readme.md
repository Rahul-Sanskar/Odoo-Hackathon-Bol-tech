Skill Swap Platform — AI-Powered (Odoo Hackathon 2025)

A full-stack Skill Sharing & Mentoring platform built for the Odoo Hackathon 2025.
It uses AI and semantic intelligence to match users for skill exchanges, recommend
learning paths, optimize availability, and more.

All features are modular, API-ready (FastAPI), and integrated with Git LFS for handling large model files.

Features Implemented

Skill Matching (Semantic)

Recommends compatible users by matching offered & wanted skills using Sentence-BERT.

Smart Skill Autocomplete

Suggests skill names using fuzzy matching and semantic similarity while typing.

Mutual Interest Matching

Computes match score based on both skill alignment and availability overlap.

Time-Slot Optimized Swapping

Prioritizes mentors/mentees who are free at the same time for smoother scheduling.

Suggested Learning Paths

Recommends next skills to learn based on current skills using embeddings + vector math.

Models (Stored via Git LFS)

Model	Format	Use
skillmatcher_model	.zip, .pkl	Feature 1
skill_autocomplete_model	.zip, .pkl	Feature 2
mutual_match_model	.zip, .pkl	Feature 3
time_swap_model	.zip, .pkl	Feature 4
learning_path_model	.zip, .pkl	Feature 5

AI & Libraries Used

sentence-transformers (MiniLM-L6-v2)

fuzzywuzzy (for fuzzy skill tag search)

numpy & pandas

Git LFS for large model storage

Google Colab for model training and testing

Dataset

Stored in Google Drive (linked via Colab):

users.csv — synthetic dataset with 10,000+ user profiles

skills_dataset.xlsx — unique skills for autocomplete & recommendations

Setup for Git LFS

git lfs install
git lfs track ".zip"
git lfs track ".pkl"
git add .gitattributes
git add *.zip *.pkl
git commit -m "Add models via Git LFS"
git push origin main

Upcoming Features

✅ Sentiment Analysis on Feedback (Feature 6)

✅ AI-generated Profile Summary

Chatbot Assistant for Swap Scheduling

Toxic Comment Detection in Messages

Team & Credits

👤 Rahul Sanskar

🤖 AI Assist via OpenAI + GitHub Copilot

☁️ Colab + HuggingFace for modeling
