# Chemical Equipment Parameter Visualizer (Hybrid App)

## Overview
This project is a hybrid application that runs both as a Web Application and Desktop Application to analyze chemical equipment datasets.

It allows users to upload CSV files, generate analytics, visualize equipment distribution, maintain upload history, and download PDF reports.

---

## Tech Stack

Frontend (Web): React.js + Chart.js  
Frontend (Desktop): PyQt5 + Matplotlib  
Backend: Django + Django REST Framework  
Database: SQLite  
Data Processing: Pandas  

---

## Features

✅ CSV Upload from Web & Desktop  
✅ Data Summary API  
✅ Interactive Charts  
✅ Upload History (Last 5 datasets)  
✅ PDF Report Generation  
✅ Hybrid Architecture  

---

## Project Structure

backend/ → Django REST API
web-frontend/ → React dashboard
desktop-app/ → PyQt desktop application


---

## Setup Instructions

### 1️⃣ Backend



cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


---

### 2️⃣ Web App



cd web-frontend
npm install
npm start


---

### 3️⃣ Desktop App



cd desktop-app
pip install requests matplotlib pyqt5
python app.py


---

## Demo Dataset
Use the provided:



sample_equipment_data.csv


---

## Author
Charuishika S
