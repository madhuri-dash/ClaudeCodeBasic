# SimpleVibeCoding

A minimal demo web application that displays a greeting message, served from a FastAPI backend and rendered by a React (Vite) frontend.

## Structure

- `backend/` — FastAPI app (`main.py`) with a health check endpoint (`GET /` → `{"status": "OK"}`).
- `frontend/` — React app bootstrapped with Vite, displaying a greeting placeholder.

## Getting Started

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

mdvenv\Scripts\python.exe -m pytest -v
```

### Frontend

```bash
cd frontend
npm install
npm run dev

npm test
```

See `PRD.md` for full product requirements.
