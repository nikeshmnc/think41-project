# 🛍️ Ecommerce Customer Support Chatbot

A smart chatbot built using **Flask** and **JavaScript** that helps customers:

- 📊 View the top 5 best-selling products  
- 🔍 Check stock availability of any product  
- 📦 Track the status of an order by ID  

---

## 🚀 Features

- 🔎 **Product Search** — Ask: `Do you have tankini?`
- 📊 **Top Products** — Ask: `top-5` or `top sold`
- 📦 **Order Status** — Ask: `status of order 12345`

✅ Real-time answers using CSV product/order data  
✅ Clean chat UI with browser-based history  
✅ REST APIs handled by Flask backend  

---

## 🛠️ Tech Stack

| Layer     | Technology             |
|-----------|------------------------|
| Frontend  | HTML, CSS, JavaScript  |
| Backend   | Python (Flask)         |
| Data      | CSV + Pandas           |

---

## 📁 Project Structure

```
ecommerce-chatbox/
├── backend/
│   ├── app.py          # Flask API app
│   └── chatbox.py      # Chat logic (top, stock, status)
│
├── frontend/
│   └── index.html      # Chatbot UI
│
├── archive/            # All datasets
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   └── ...
│
└── readme.md           # You're reading it!
```

---

## ▶️ Run Locally

### Step 1: Start the Flask Server

```bash
cd backend
python app.py
```

### Step 2: Open Frontend

Just open:

```bash
frontend/index.html
```

✅ Make sure the `archive/` folder with CSV files is in the root directory.

---

## 💬 Sample Questions to Ask

```
top-5
Do you have tankini?
status of order 12345
```

---

## 👨‍💻 Author

**Nikhesh M**  
GitHub: [@nikeshmnc](https://github.com/nikeshmnc)
