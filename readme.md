# Skill Swap Platform — AI-Powered (Odoo Hackathon 2025)

A full-stack Skill Sharing & Mentoring platform built for the Odoo Hackathon 2025.
It uses AI and semantic intelligence to match users for skill exchanges, recommend
learning paths, optimize availability, and more.

All features are modular, API-ready (FastAPI), and integrated with Git LFS for handling large model files.

## Features Implemented

- ***Skill Matching (Semantic)***

    - Recommends compatible users by matching offered & wanted skills using Sentence-BERT.

- ***Smart Skill Autocomplete***

    - Suggests skill names using fuzzy matching and semantic similarity while typing.

- ***Mutual Interest Matching***

    - Computes match score based on both skill alignment and availability overlap.

- ***Time-Slot Optimized Swapping***

    - Prioritizes mentors/mentees who are free at the same time for smoother scheduling.

- ***Suggested Learning Paths***

    - Recommends next skills to learn based on current skills using embeddings + vector math.

 

### 🤖 ML Models (Stored via Git LFS)

| **Model**                 | **Format**         | **Use**        |
|--------------------------|--------------------|----------------|
| `skillmatcher_model`     | `.zip`, `.pkl`     | Feature 1      |
| `skill_autocomplete_model` | `.zip`, `.pkl`   | Feature 2      |
| `mutual_match_model`     | `.zip`, `.pkl`     | Feature 3      |
| `time_swap_model`        | `.zip`, `.pkl`     | Feature 4      |
| `learning_path_model`    | `.zip`, `.pkl`     | Feature 5      |

### AI & Libraries Used

- ***sentence-transformers (MiniLM-L6-v2)***

- ***fuzzywuzzy (for fuzzy skill tag search)***

- ***numpy & pandas***

- ***Git LFS for large model storage***

- ***Google Colab for model training and testing***

### Dataset

- Stored in Google Drive (linked via Colab):

- users.csv — synthetic dataset with 10,000+ user profiles

- skills_dataset.xlsx — unique skills for autocomplete & recommendations

### Setup for Git LFS

```bash
git lfs install
git lfs track ".zip"
git lfs track ".pkl"
git add .gitattributes
git add *.zip *.pkl
git commit -m "Add models via Git LFS"
git push origin main
```
---
# Skill Swap Platform Backend
This is the backend for the Skill Swap Platform, built with FastAPI and SQLite. It provides APIs for user authentication, skill management, skill swapping, and admin functionalities. This README guides you through setting up the backend on a Windows environment using a GitHub repository.
## Prerequisites

- **Python**: Version 3.12 or higher.
- **Git**: Installed and configured.
- **Virtualenv**: For creating a virtual environment.
- **SQLite**: Included with Python, no separate installation needed.
- **GitHub Repository**: Assumed to be at https://github.com/Rahul-Sanskar/Odoo-Hackathon-Bol-tech.

## Setup Instructions
- 1. Clone the Repository
Clone the project from GitHub to your local machine:
```bash
git clone https://github.com/Rahul-Sanskar/Odoo-Hackathon-Bol-tech
cd Odoo-Hackathon-Bol-tech/backend
```
- 2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies:
```bash
python -m venv env
.\env\Scripts\activate
```

- 3. Install Dependencies
Install the required Python packages listed in requirements.txt:
```bash
pip install -r requirements.txt
```
Ensure requirements.txt includes:
```bash
fastapi
uvicorn
sqlalchemy
pydantic-settings
alembic
python-jose[cryptography]
passlib[bcrypt]
```
- 4. Configure Environment Variables
Create a .env file in the backend/ directory with the following content:
```bash
SECRET_KEY=d3cf8a3be5c158ca42a7cf5d9aae91a0650831b1b692ad938bb82f3258a7f511
DATABASE_URL=sqlite:///skillswap.db
```
For Windows, you can use an absolute path if needed:
```bash
DATABASE_URL=sqlite:///D:/path/to/skill-swap-platform/backend/skillswap.db
```
- 5. Apply Database Migrations
Initialize the SQLite database and apply migrations using Alembic:

Verify Migration Script:

Ensure backend/alembic/versions/c22efbbd8a5b_initial_migration.py exists, creating tables for users, skills, swaps, and feedback.


Apply Migration:
```bash
alembic upgrade head
```

This creates skillswap.db in the backend/ directory with the required schema.


Verify Database:
```bash
sqlite3 skillswap.db ".tables"
```

Expected output: alembic_version  feedback  skills  swaps  users



- 6. Run the FastAPI Application
Start the FastAPI server:
```bash
python run.py
```

The server will run at http://localhost:8000.
Access the interactive API documentation at http://localhost:8000/docs.

- 7. Test the API
Test the core endpoints using curl or the Swagger UI (http://localhost:8000/docs):

Register a User:
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" -H "Content-Type: application/json" -d "{\"name\":\"Test User\",\"email\":\"test@example.com\",\"password\":\"password123\",\"location\":\"Test City\",\"is_public\":true}"
```

Obtain a Token:
```bash
curl -X POST "http://localhost:8000/api/v1/auth/token" -H "Content-Type: application/x-www-form-urlencoded" -d "username=test@example.com&password=password123"
```

Create a Skill:
```bash
curl -X POST "http://localhost:8000/api/v1/skills/" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d "{\"name\":\"Python Programming\",\"is_offered\":true}"
```

Create a Swap:
```bash
curl -X POST "http://localhost:8000/api/v1/swaps/" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d "{\"receiver_id\":1,\"skill_offered_id\":1,\"skill_wanted_id\":1,\"status\":\"pending\"}"
```

Verify Database:
```bash
sqlite3 skillswap.db "SELECT * FROM users;"
sqlite3 skillswap.db "SELECT * FROM skills;"
sqlite3 skillswap.db "SELECT * FROM swaps;"
```


Project Structure
```project-tree
skill-swap-platform/
├── backend/
│   ├── alembic/
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions/
│   │       └── c22efbbd8a5b_initial_migration.py
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── auth.py
│   │   │       ├── users.py
│   │   │       ├── skills.py
│   │   │       ├── swaps.py
│   │   │       ├── admin.py
│   │   │       └── models.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   └── security.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── skill.py
│   │   │   ├── swap.py
│   │   │   ├── feedback.py
│   │   │   └── __init__.py
│   │   ├── schemas/
│   │   │   ├── skill.py
│   │   │   └── swap.py
│   │   ├── dependencies.py
│   │   └── main.py
│   ├── .env
│   ├── alembic.ini
│   ├── requirements.txt
│   ├── run.py
│   └── skillswap.db
```
Troubleshooting

Database Issues:

- If skillswap.db fails to create, use absolute path in .env and alembic.ini:DATABASE_URL=sqlite:///D:/path/to/skill-swap-platform/backend/skillswap.db


- Ensure skillswap.db is writable (right-click, Properties, Security, grant write access).
- Reset database if needed:del skillswap.db
```bash
alembic upgrade head
```



Pydantic V2 Warning:

- Ensure all Pydantic models (e.g., in app/schemas/skill.py, app/schemas/swap.py) use:
```python
class Config:
    from_attributes = True
```



NameError for Models:

- Verify app/api/v1/models.py defines UserResponse and is imported in skills.py, swaps.py, etc.
- Check app/core/security.py for correct UserResponse import in get_current_user.


Migration Errors:

- If alembic upgrade head fails, delete alembic/versions/*.py and reapply the migration.



### Notes

- Pydantic V2: All models use from_attributes = True for compatibility.
- Database: The migration c22efbbd8a5b_initial_migration.py creates the schema for users, skills, swaps, and feedback.
- GitHub: Replace your-username in the clone URL with your actual GitHub username.
- Windows: Use forward slashes (/) in DATABASE_URL for compatibility.

--- 

# 🔄 SkillSwap Frontend

The frontend of the *SkillSwap Platform, a web app where users can exchange and request skills in a collaborative environment. Built using **React.js* and styled with *Material UI*, this responsive interface enables users to easily browse skills, connect with others, and manage their profiles.

---

## 🚀 Features

- 🌐 Modern and responsive UI
- 🔐 Login & Signup with JWT token handling
- 📋 Skill listing and request features
- 👥 Role-based views (e.g. learner, teacher)
- ⚙ Settings & profile management
- 🌙 Dark mode support (optional)
- 📁 Cloudinary integration for file uploads
- 🔄 API integration with FastAPI backend

---

## 🛠 Tech Stack

- *Framework:* React.js (Vite or CRA)
- *Styling:* Material UI (MUI v5)
- *Routing:* React Router
- *State Management:* useState, useContext (or Redux if added)
- *API Communication:* Axios / Fetch
- *Form Handling:* React Hook Form / Native

---

## Upcoming Features

- ✅ Sentiment Analysis on Feedback (Feature 6)

- ✅ AI-generated Profile Summary

- Chatbot Assistant for Swap Scheduling

- Toxic Comment Detection in Messages

## Team & Credits

👤 Rahul Sanskar (AI Developer)

🤖 AI Assist via OpenAI + GitHub Copilot

☁️ Colab + HuggingFace for modeling

------
👤 Esan Raj (Backend Developer)

🤖 AI Assist via Grok

☁️ Backend in FastAPI

----
👤 Inzamam-ul-Haque (Frontend Developer)

🤖 AI Assist via OpenAI + GitHub Copilot

☁️ ReactJS + Material UI for Frontend