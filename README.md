# 🎫 AI-Based Customer Support Ticketing System

An intelligent customer support platform that automates ticket classification, routing, and analytics using a lightweight AI approach. Built using Streamlit for rapid development and deployment.

---

## 🚀 Live Demo

Deployed on Streamlit Cloud
https://customer-support-ticketing-system-nwufhbdxhuqfxdxmttmpxq.streamlit.app/

---
<img width="1902" height="762" alt="image" src="https://github.com/user-attachments/assets/1507de5d-4c5a-4e85-8b08-85e9390d8d80" />


## 🧠 Project Overview

This project simulates a real-world **AI-powered support system** where customer issues are automatically categorized, prioritized, and assigned to agents.

It helps organizations:

* Reduce manual ticket sorting
* Improve response time
* Monitor agent performance
* Gain insights into customer issues

---

## ⚙️ Features

### ✅ AI-Based Ticket Classification

* Automatically categorizes tickets into:

  * Billing
  * Technical
  * General
* Assigns priority levels:

  * High / Medium / Low

### ✅ Smart Ticket Routing

* Assigns tickets to agents based on category

### ✅ SLA Tracking

* Tracks ticket lifecycle:

  * Created → Resolved
* Records timestamps for analysis

### ✅ Agent Dashboard

* View all tickets
* Resolve tickets with one click

### ✅ Analytics Dashboard

* Tickets by category
* Tickets by priority
* Agent workload distribution

---

## 🛠️ Tech Stack

* **Frontend + Backend:** Streamlit
* **Database:** SQLite
* **Language:** Python
* **Data Handling:** Pandas

---

## 🧩 System Architecture

User submits ticket → AI classification → Auto routing → Stored in database → Dashboard & analytics

---

## 📂 Project Structure

```
├── app.py
├── requirements.txt
└── README.md
```

---

## ▶️ How It Works

1. User submits a support ticket
2. System applies AI-based classification
3. Ticket is assigned to a relevant agent
4. Agent resolves the ticket
5. Data is used for analytics and insights

---

## 🧪 Example Inputs

| Input Text               | Category  | Priority |
| ------------------------ | --------- | -------- |
| "Payment not processed"  | Billing   | High     |
| "App shows error"        | Technical | High     |
| "App is slow"            | Technical | Medium   |
| "Need help with account" | General   | Low      |

---

## 📦 Installation (Optional Local Setup)

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deployment

1. Push code to GitHub
2. Go to Streamlit Cloud
3. Connect your repository
4. Deploy `app.py`

---

## ⚠️ Limitations

* Uses rule-based AI (can be upgraded to ML model)
* SQLite is not persistent for large-scale production

---

## 🔮 Future Enhancements

* 🔥 Machine Learning model (TF-IDF / NLP)
* 💬 Chatbot integration
* 📩 Email notifications
* 📊 SLA breach alerts
* ☁️ Cloud database (MongoDB / PostgreSQL)

---

## 👩‍💻 Author

**Deepalakshmi S**
B.Tech IT | Aspiring Data Scientist

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
