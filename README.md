Flask CI/CD Project: Jenkins, Docker aur AWS EC2
Abdul Hayee | 7 October 2026

Ek Python Flask app ko GitHub, Docker aur Jenkins ke zariye AWS EC2 server par khud ba khud build aur deploy karna. Code push karo, 1 se 3 minute mein app update ho jati hai.
Flow
Laptop (git push) → GitHub (malikabdulhayee1/devops_project_1) → Jenkins on EC2 (har 2 minute mein check) → docker build → docker run → /health smoke test → app live on port 5000.
Tools
• Flask 3.1 + gunicorn: app aur routes /info, /mail, /me, /name, /health
• Docker (python:3.12-slim): app ka container
• Jenkins (Java 21): Jenkinsfile se pipeline
• AWS EC2: t2.medium, Ubuntu 24.04, 20 GB, Security Group ports 22, 8080, 5000
Pipeline stages
Checkout, Build Docker Image, Deploy, Smoke Test. Image ka tag har build par badalta hai (flask-app:1, :2, :3), isliye purane version par rollback ho sakta hai.
Kya seekha
• Pipeline as Code: pipeline Jenkinsfile mein hai aur Git mein version hoti hai
• Docker layer caching: requirements.txt pehle copy hoti hai, is liye code badalne par build tez rehti hai
• Pinned versions: Flask==3.1.0, har build same banta hai
• Least privilege: Jenkins aur app ke ports sirf My IP par khule
• Secrets: .gitignore mein .env aur *.pem
• Health endpoint: /health se app ka zinda hona check hota hai
