# 🛒 FastAPI Products Demo with UI

A full-stack product management application built with **FastAPI** and a vanilla JavaScript frontend. Supports full CRUD operations on products with a clean browser-based UI.

## 🚀 Features

- Create, Read, Update, Delete products
- RESTful API with FastAPI
- Interactive frontend UI (no frameworks)
- SQLAlchemy ORM with SQLite database
- Pydantic data validation
- Auto-generated Swagger API docs

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, SQLAlchemy, Pydantic
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript (48% JS, 36% CSS)

## 📁 Project Structure

```
fastapi-demo-products-with-ui/
├── frontend/              # Vanilla JS/CSS/HTML UI
├── main.py                # FastAPI routes & app entry point
├── database.py            # Database connection & session
├── database_models.py     # SQLAlchemy ORM models
├── models.py              # Pydantic schemas
├── requirements.txt
└── .gitignore
```

## ⚙️ Installation & Setup

```bash
# 1. Clone the repo
git clone https://github.com/Anandh2002/fastapi-demo-products-with-ui.git
cd fastapi-demo-products-with-ui

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000` for the UI and `http://127.0.0.1:8000/docs` for Swagger API docs.

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products` | List all products |
| GET | `/products/{id}` | Get a single product |
| POST | `/products` | Create a new product |
| PUT | `/products/{id}` | Update a product |
| DELETE | `/products/{id}` | Delete a product |

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
