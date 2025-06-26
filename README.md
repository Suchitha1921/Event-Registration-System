# 📅 Event Registration System 🚀

A lightweight backend system to manage events and registrations — built as part of the **30 Days of Python Challenge** with FastAPI and local file handling.

---

## 📌 Overview

This FastAPI-based project allows users to:
- **View available events** → `GET /events`
- **Register for an event** → `POST /register`
- **View all registrations** → `GET /registrations`

✨ Built to simulate real-world backend systems using JSON and CSV — simple yet powerful!

---

## 🔧 Tech Stack

| Tool        | Purpose                             |
|-------------|-------------------------------------|
| **FastAPI** | Backend API framework with docs     |
| **Pydantic**| Data validation and schema creation |
| **JSON**    | Event data handling (input/output)  |
| **CSV**     | Registration data storage           |
| **Uvicorn** | ASGI server to run FastAPI app      |

---

## 🚀 How to Run Locally

```bash
# 1️⃣ Clone the repo
git clone https://github.com/YourUsername/Event-Registration-System.git
cd Event-Registration-System

# 2️⃣ Create and activate a virtual environment
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the FastAPI app using Uvicorn
uvicorn main:app --reload


🧭 Open your browser and go to:
http://127.0.0.1:8000/docs — for the interactive API Swagger UI


