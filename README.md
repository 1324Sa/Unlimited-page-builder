# 🚀 Brave Custom CMS (Flask)

A simple yet powerful Content Management System (CMS) built with **Python** and **Flask**. This platform allows you to create an unlimited number of dynamic web pages and customize them using HTML/CSS through a modern, intuitive dashboard.

## ✨ Key Features:
- **Admin Dashboard:** A sleek, Dark Mode user interface for managing your content.
- **Unlimited Pages:** Create, preview, and delete pages dynamically in real-time.
- **Full HTML/CSS Support:** Complete control over each page's content for professional customization.
- **SQLite Database:** Local data storage for easy setup and portable management.
- **Modern UI:** Responsive design that looks great on both desktop and mobile devices.

## 🛠️ Tech Stack:
- **Language:** Python 3.x
- **Framework:** Flask
- **Database:** Flask-SQLAlchemy (SQLite)
- **Templating:** Jinja2
- **Styling:** CSS3 (Modern UI with Glassmorphism effects)

## 📂 Project Structure:
```text
Brave/
├── app.py              # Main Flask application logic
├── pages_data.db       # SQLite database (generated locally)
├── requirements.txt    # List of dependencies
├── static/
│   └── style.css       # Global styles for generated pages
└── templates/
    ├── dashboard.html  # Admin control panel
    └── page_template.html # Template for generated websites
