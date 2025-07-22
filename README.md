# Azure Flask App Deployment

This project demonstrates how to deploy a Python Flask web app to Azure using GitHub Actions, Azure App Services, Azure SQL Database, and monitoring tools.

## 🚀 Project Overview
In this project, you'll:
- Create a web app using HTML/CSS/JavaScript + Python Flask
- Host it on Azure App Service
- Use GitHub Actions for CI/CD
- Store data in Azure SQL Database
- Secure secrets with Azure Key Vault
- Monitor performance with Azure Monitor & Application Insights
- Optionally automate infrastructure using ARM templates or Terraform

## 🔧 Tech Stack
- Python + Flask
- Azure App Services
- Azure SQL Database
- Azure Key Vault
- GitHub Actions (CI/CD)
- Application Insights

## 📁 Folder Structure
simple-flask-app/
│
├── app.py
├── requirements.txt
├── templates/
│ └── index.html
└── static/
└── style.css

bash
Copy code

## 📝 How to Run Locally
1. Create a Python virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
python app.py
Visit http://localhost:5000 in your browser.

## ⚙️ Deployment

### Azure App Service
- Host the Flask app on Azure App Service with Python 3.11 runtime.
- Use Application Insights for monitoring.

### CI/CD with GitHub Actions
- GitHub Actions workflow automatically deploys the app on every push to the **main** branch.
- The workflow installs dependencies and deploys the app to Azure.

### Azure SQL Database
- Store user messages securely in Azure SQL Database.
- Connect using ODBC Driver 18 and `pyodbc`.

### Azure Key Vault
- Store sensitive information like database credentials securely.
- Access secrets via environment variables in your app.

### Monitoring
- Use Azure Monitor and Application Insights to track app health and performance.

---

## 🚀 Live Demo URL

[https://the-flask-cxekhwhje6d7fwdz.eastus-01.azurewebsites.net](https://the-flask-cxekhwhje6d7fwdz.eastus-01.azurewebsites.net)

---

## 📚 Learning Outcomes

By completing this project, you will learn how to:

- Create and deploy a Python Flask app on Azure App Service
- Set up CI/CD pipelines using GitHub Actions
- Use Azure SQL Database for persistent data storage
- Manage secrets securely with Azure Key Vault
- Monitor application health with Azure Monitor and Application Insights

