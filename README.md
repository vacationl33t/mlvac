# ML-Inz-example

This project contains two main components:
1. A Flask backend serving HTML, CSS, and JavaScript.
2. A machine learning service using the `suno/bark` to do voice-to-speech

##Structure 
```
  mlvac/
  │
  ├── Backend/
  │   ├── app/
  │   │   ├── __init__.py
  │   │   ├── main.py
  │   │   ├── templates/
  │   │   │   └── index.html
  │   │   ├── static/
  │   │   │   ├── css/
  │   │   │   │   └── style.css
  │   │   │   └── js/
  │   │   │       └── script.js
  │   ├── __init__.py
  │   ├── Dockerfile
  │   ├── requirements.txt
  │
  ├── model/
  │   ├── app/
  │   │   ├── __init__.py
  │   │   ├── main.py
  │   │   ├── model.py
  │   ├── __init__.py
  │   ├── Dockerfile
  │   ├── requirements.txt
  │
  ├── tests/
  │   ├── __init__.py
  │   ├── test_backend.py
  │   ├── test_ml_service.py
  ├── __init__.py
  ├── docker-compose.yml
  ├── setup.py
  ├── README.md
  ├── MANIFEST.in
  └── pytest.ini
```

##how to start
1. Clone rep from git 
2. pip install -r backend/requirements.txt
3. pip install -r ml_service/requirements.txt
4. Start with python main.py from Backend/app
5. Start with python main.py from model/app
6. http://localhost:8000 - backend adress
7. http://localhost:8001 - front addres
