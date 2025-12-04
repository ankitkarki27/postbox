# Postbox

**Postbox** is a real-time social network and chat app built with **Django**, **Django Channels**, and **Google Authentication**.  
It provides instant WebSocket-based messaging and secure Google OAuth login within a simple, fast social feed interface.

---

## Features
- Real-time chat using **Django Channels**
- Secure login with **Google OAuth**
- Simple social feed for posts and interactions
- Fast and lightweight interface

---

## Tech Stack
- **Backend:** Django, Django Channels
- **Authentication:** Google OAuth
- **Frontend:** HTML/CSS/JS
- **Realtime:** WebSockets

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/Postbox-social-network-chatapp.git
````

2.  Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

3.  Apply database migrations:
```bash
python manage.py migrate
```

4.  Start the development server:
```bash
python manage.py runserver
```
---
## Usage
* Open the app in your browser at `http://127.0.0.1:8000/`
* Login with Google
* Chat with other users in real-time
* Post and interact in the social feed

