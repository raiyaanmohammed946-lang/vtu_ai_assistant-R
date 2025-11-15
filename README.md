VTU AI Assistant - Starter Project
---------------------------------
This is a minimal starter Flask web app that provides simple endpoints and a static frontend.

How to run (Linux / macOS / Windows WSL):

1. Create a virtual environment (recommended):
   python3 -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
2. Install requirements:
   pip install -r requirements.txt
3. Run the app:
   python app.py
4. Open http://127.0.0.1:5000 in your browser.

What is included:
- app.py : Flask backend with simple endpoints
- templates/index.html : Simple frontend UI to search and browse
- static/ : place to add CSS/JS/assets
- README.md : this file

Notes:
- This is a starting point. Expand DATA in app.py or hook it to a database.
- To prepare a production build consider using Gunicorn, nginx, or deploying to a PaaS.
