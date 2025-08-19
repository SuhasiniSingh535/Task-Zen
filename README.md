<br>

<div align="center">

✨ Task Zen ✨
<br>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask Badge"/>
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite Badge"/>
</p>

A sleek and simple Task Management web app built to bring a little bit of calm to your daily chaos. 🧘‍♂️

</div>

📸 Sneak Peek
Here's a look at the clean, mobile-first interface. Never lose track of your to-dos again!

<div align="center">
<img src="https://i.imgur.com/rL4jP3c.png" alt="Task Master Screenshot" width="700"/>
</div>

🚀 Features
📝 Full CRUD Functionality: Add, edit, and delete tasks with ease.

✅ Task Tracking: Mark tasks as complete and move them to a dedicated "Completed" view.

📱 Responsive Design: Looks great on both desktop and mobile devices.

🌙 Dark Mode: A beautiful dark theme for those late-night work sessions.

📤 Export Tasks: Download your current task list as a .txt file.

📊 Simple Stats: Get a quick overview of your productivity.

🛠️ Tech Stack
Backend: Python 🐍, Flask 🧪

Database: SQLAlchemy, SQLite 💾

Frontend: HTML5, CSS3 🎨, Vanilla JavaScript 🍦

⚙️ Getting Started
Ready to get your own instance of Task Zen up and running? Follow these simple steps.

1. Clone the Repository
First, clone this repository to your local machine.

Bash

git clone https://github.com/your-username/task-zen.git
cd task-zen
2. Create and Activate a Virtual Environment
It's best practice to use a virtual environment to keep dependencies isolated.

Bash

# For Windows
python -m venv env
.\env\Scripts\activate

# For macOS/Linux
python3 -m venv env
source env/bin/activate
3. Install Dependencies
Install all the necessary packages from the requirements.txt file.

Bash

pip install -r requirements.txt
(Note: If you don't have a requirements.txt file, you'll need to install Flask and Flask-SQLAlchemy manually: pip install Flask Flask-SQLAlchemy)

4. Run the App! 🎬
Launch the Flask development server.

Bash

python app.py
The application will be running at http://127.0.0.1:5000. Open this URL in your browser to start managing your tasks!

📁 Project Structure
.
├── env/
├── static/
│   └── css/
│       └── main.css
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── completed.html
│   └── update.html
├── app.py
└── test.db
🔮 Future Improvements
[ ] User authentication to support multiple users 🙋‍♀️🙋‍♂️

[ ] Due dates and reminders for tasks 📅

[ ] Drag-and-drop task reordering ↕️

[ ] Sub-tasks and project categories 📂

<div align="center">
Made with ❤️ and a lot of coffee.
</div>
