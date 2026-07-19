import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# ---------- DB ----------
conn = sqlite3.connect("tickets.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    category TEXT,
    priority TEXT,
    agent TEXT,
    status TEXT,
    created_at TEXT,
    resolved_at TEXT
)
""")
conn.commit()

# ---------- AI ----------
def classify_ticket(text):
    text = text.lower()

    if "payment" in text or "refund" in text:
        return "Billing", "High"
    elif "error" in text or "bug" in text:
        return "Technical", "High"
    elif "slow" in text:
        return "Technical", "Medium"
    else:
        return "General", "Low"

def assign_agent(category):
    if category == "Billing":
        return "Agent A"
    elif category == "Technical":
        return "Agent B"
    else:
        return "Agent C"

# ---------- UI ----------
st.title("🎫 AI Support Ticket System")

menu = st.sidebar.selectbox("Menu", ["Create Ticket", "Agent Dashboard", "Analytics"])

# ---------- CREATE ----------
if menu == "Create Ticket":
    st.header("📩 Submit Ticket")

    text = st.text_area("Describe your issue")

    if st.button("Submit"):
        category, priority = classify_ticket(text)
        agent = assign_agent(category)

        conn.execute("""
        INSERT INTO tickets (text, category, priority, agent, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (text, category, priority, agent, "Open", str(datetime.now())))
        conn.commit()

        st.success(f"Ticket Created! Assigned to {agent}")
        st.write(f"Category: {category}, Priority: {priority}")

# ---------- DASHBOARD ----------
elif menu == "Agent Dashboard":
    st.header("👨‍💼 Agent Dashboard")

    df = pd.read_sql("SELECT * FROM tickets", conn)

    if not df.empty:
        st.dataframe(df)

        ticket_id = st.number_input("Enter Ticket ID to Resolve", step=1)

        if st.button("Mark as Resolved"):
            conn.execute("""
            UPDATE tickets
            SET status='Resolved', resolved_at=?
            WHERE id=?
            """, (str(datetime.now()), ticket_id))
            conn.commit()
            st.success("Ticket Resolved!")

# ---------- ANALYTICS ----------
elif menu == "Analytics":
    st.header("📊 Insights")

    df = pd.read_sql("SELECT * FROM tickets", conn)

    if not df.empty:
        st.subheader("Tickets by Category")
        st.bar_chart(df["category"].value_counts())

        st.subheader("Tickets by Priority")
        st.bar_chart(df["priority"].value_counts())

        st.subheader("Agent Performance")
        st.bar_chart(df["agent"].value_counts())
