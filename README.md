#  InterVueX – Advanced AI Interview Bot

InterVueX is an advanced AI-powered interview preparation platform that simulates real technical interviews with time pressure, role-based questions, and intelligent answer evaluation.  
The goal of this project is to help students and job seekers practice interviews in a realistic, stress-driven environment.

---

##  Key Highlights

-  Real-time countdown timer (live during typing)
-  Role-based interviews (Python, Java, Web Development)
-  AI-powered answer evaluation with scoring & feedback
-  Pressure-based interview simulation
-  Interview history storage using SQLite
-  Optional webcam-based confidence analysis (OpenCV)
-  Clean and interactive UI using Streamlit

---

##  How InterVueX Works

1. User selects an interview role (Python / Java / Web).
2. A role-specific question is selected randomly.
3. A live timer starts immediately.
4. User answers under time pressure.
5. AI evaluates the answer against ideal responses.
6. Score and feedback are generated instantly.
7. Interview data is stored for future analysis.

---

##  Tech Stack

| Category | Technology |
|--------|------------|
| Language | Python |
| Frontend | Streamlit |
| AI / NLP | NLP Similarity Techniques |
| Database | SQLite |
| Timer System | Streamlit Auto Refresh |
| Optional AI | OpenCV |
| Version Control | Git & GitHub |

---

##  Project Structure

InterVueX/
├── frontend/
│   └── app.py
├── backend/
│   ├── evaluator.py
│   └── database.py
├── webcam/
│   └── confidence.py
├── data/
│   ├── questions.json
│   └── ideal_answers.json
├── roles/
│   └── roles.json
├── README.md

---

##  Installation & Run

### 1️⃣ Clone Repository
git clone https://github.com/Badalsha57/InterVueX.git
cd InterVueX

### 2️⃣ Install Dependencies
python -m pip install streamlit streamlit-autorefresh scikit-learn opencv-python

### 3️⃣ Run Application
python -m streamlit run frontend/app.py

---

##  Use Cases

- Placement & campus interview preparation
- Technical interview practice
- Time management under pressure
- AI-assisted self-evaluation

---

##  Future Enhancements

- Voice-based interview system
- Adaptive difficulty levels
- PDF interview report generation
- Cloud deployment

---

## Author

Badal Kumar Sharma  
B.Tech CSE Student | AI & Web Development  

GitHub: [https://github.com/Badalsha57](https://github.com/)  
Email: badalsha5757@gmail.com

---

⭐ If you like this project, give it a star on GitHub.
