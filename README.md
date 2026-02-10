# AngularJS + Spring Boot + Python Dashboard Prototype

This prototype demonstrates a simple dashboard frontend (AngularJS 1.x) that fetches aggregated application metrics from a Spring Boot backend. A small Python Flask service is included to simulate separate application endpoints.

Folder layout:
- backend-python: Flask sample services (simulates multiple apps)
- backend-springboot: Minimal Spring Boot app exposing `/api/apps`
- frontend: AngularJS (1.x) dashboard UI

Quick start (Windows):

1) Python backend (simulated apps)

```powershell
cd C:\2026-Python-Agentic-Project\Angular-SpringBoot-DashBoard-Project\backend-python
python -m pip install -r requirements.txt
python app.py
```

2) Spring Boot backend (API aggregator)

```powershell
cd C:\2026-Python-Agentic-Project\Angular-SpringBoot-DashBoard-Project\backend-springboot
mvn clean package
# run the jar (adjust the name depending on version)
java -jar target/backend-springboot-0.0.1-SNAPSHOT.jar
```

Note: The Spring Boot app returns sample data. You can update it to call the Python endpoints if you run both services.

3) Frontend

Open `frontend/index.html` in your browser or serve it with a simple HTTP server:

```powershell
cd C:\2026-Python-Agentic-Project\Angular-SpringBoot-DashBoard-Project\frontend
python -m http.server 4200
# then open http://localhost:4200
```

If you want, I can try building and running the services for you. Would you like me to attempt that now?
