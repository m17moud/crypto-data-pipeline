# 🚀 Crypto Data Pipeline

A production-style **Data Engineering project** that builds a complete ETL pipeline for cryptocurrency data using Python and PostgreSQL.

---

## 📊 Architecture

![Pipeline Architecture](architecture.png)

---

## 🔄 Pipeline Overview

This project implements a simple ETL pipeline:

- **Extract**: Fetch cryptocurrency market data from CoinGecko API
- **Transform**: Clean and structure the data using Python
- **Load**: Store the data into PostgreSQL database

---

## 🛠 Tech Stack

- Python
- PostgreSQL
- REST API
- Logging
- Environment Variables

---

## ⚙️ Features

- Automated ETL pipeline
- Logging system (`pipeline.log`)
- Secure database connection using `.env`
- Clean modular code structure

---

## 📁 Project Structure



crypto-data-pipeline
│
├── scripts
│ ├── extract_crypto.py
│ └── load_to_db.py
│
├── data
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── architecture.png


---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/crypto-data-pipeline.git
cd crypto-data-pipeline

2. Create virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Create .env file
DB_HOST=localhost
DB_NAME=crypto_db
DB_USER=postgres
DB_PASSWORD=yourpassword

5. Run the pipeline
python main.py
