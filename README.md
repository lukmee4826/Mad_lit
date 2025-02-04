# 📝 Mad Lib Game - Django Web App

This is a Django-based **Mad Lib Game** that asks users a series of fun questions, then generates a humorous story based on their answers. The web app features a **step-by-step question flow** with beautiful animations using **Tailwind CSS** and **Animate.css**.

---

## 🚀 Features
- 🔄 Step-by-step question format (1 page per question)
- ✨ Smooth animations using **Animate.css**
- 🎨 Styled with **Tailwind CSS**
- 🔊 Option to read out the final story (Coming soon!)
- 📦 Built with **Django 4+** and **Python 3.10+**

---

## 📂 Project Structure
madlib_project/ │── madlib_project/ # Main Django project folder │ ├── settings.py # Django settings │ ├── urls.py # Project-level URLs │ ├── wsgi.py # WSGI entry point │ └── asgi.py # ASGI entry point │ │── madlib_app/ # Django app folder │ ├── migrations/ # Database migrations │ ├── templates/ # HTML templates │ │ ├── madlib_question.html # Question page │ │ ├── madlib_result.html # Result page │ ├── static/ # Static files (CSS, JS) │ ├── views.py # Views for the app │ ├── urls.py # App-level URLs │ ├── models.py # Database models (if needed) │ ├── forms.py # Forms for the game │ ├── tests.py # Test cases │ │── db.sqlite3 # SQLite database (auto-generated) │── manage.py # Django management script │── README.md # Project documentation │── requirements.txt # Dependencies list


---

## 🛠️ Installation & Setup

### ✅ 1. Clone the Repository
```sh
cd madlib-game

python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

📜 License
This project is open-source and available under the MIT License.

💡 Future Improvements
🎨 More Themes & Styles
🔗 Social Sharing (Share your funny Mad Libs!)
```sh


