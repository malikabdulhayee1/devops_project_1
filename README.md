# devops_project_1

Flask app, Dockerized, deployed with a Jenkins CI/CD pipeline on AWS EC2.

Run locally:
    pip install -r requirements.txt
    python app.py

Run with Docker:
    docker build -t flask-app .
    docker run -d -p 5000:5000 flask-app
