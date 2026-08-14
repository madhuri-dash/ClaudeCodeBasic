# Product Requirements Document: Printing Hola MADHURI DASH!!

**Version:** 1.0
**Status:** Draft
**Date:** August 13, 2026

---

## 1. Overview

Printing Hola MADHURI DASH!! is a minimal demo web application. Its sole purpose is to display the text "Hola!!" to the user, served from a backend API and rendered by a frontend.

## 2. Goals

- Display "Hola MADHURI DASH!!" on the screen when the app loads.
- Serve the greeting from a backend API rather than hardcoding it in the frontend.
- Keep the implementation as simple as possible.

### Non-Goals

- No user input, forms, or interactivity beyond page load.
- No authentication, database, or persistence.
- No multi-page navigation.

## 3. User Story

| # | As a user, I want to... | So that... |
|---|--------------------------|-------------|
| 1 | Open the app | I see "Hola MADHURI DASH!!" displayed on the screen |

## 4. Functional Requirements

- On page load, the frontend calls the backend API to fetch the greeting message.
- The backend returns the text "Hola!!" in the API response.
- The frontend displays "Hola!!" on the screen.

## 5. Technical Requirements

### 5.1 Frontend
- **Framework:** React (bootstrapped with Vite)
- **Behavior:** On mount, fetch the greeting from the backend and render it on the page.

### 5.2 Backend
- **Framework:** FastAPI (Python)
- **API Endpoint:**

| Method | Endpoint | Description |
|--------|-----------|--------------|
| GET | `/hola` | Returns the greeting message |

- **Example Response:**

```json
{
  "message": "Hola MADHURI DASH!!"
}
```

## 6. Success Metrics

- Page loads and displays "Hola MADHURI DASH!!" without errors.
- API responds in under 300ms.

---

*End of document.*
