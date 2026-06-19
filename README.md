# 🎬 AI Movie Recommender

An AI-powered movie recommendation web application built using **FastAPI**, **Groq LLM**, **HTML**, **CSS**, and **JavaScript**.

Users can enter a movie genre and mood, and the application generates personalized movie recommendations using AI.

---

## 🚀 Features

* AI-powered movie recommendations
* FastAPI backend
* Groq LLM integration
* Responsive modern UI
* Real-time recommendation generation
* Easy deployment on Render

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Groq API
* Python
* python-dotenv

### Frontend

* HTML
* CSS
* JavaScript

---

## 📂 Project Structure

```text
Movie_Recommender/
│
├── main.py
├── requirements.txt
├── .env
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
└── README.md
```

---



### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:

https://console.groq.com/

---

## ▶️ Run Locally

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## 🎯 Example Input

Genre:

```text
Sci-Fi
```

Mood:

```text
Mind-bending
```

The AI will generate 5 personalized movie recommendations.

---

## 🌐 Deployment

This project can be deployed easily on:

* Render
* Railway
* Fly.io
* Azure
* AWS

### Render Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

## 📸 Screenshots

Add screenshots of your application here after deployment.

---

## 👨‍💻 Author

Thomas Paul
