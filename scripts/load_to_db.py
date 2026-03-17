import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def load_data(data):

    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )



    cur = conn.cursor()

    for coin in data:
        cur.execute("""
            INSERT INTO crypto_prices
            (coin_name, symbol, price_usd, market_cap, timestamp)
            VALUES (%s,%s,%s,%s,%s)
                ON CONFLICT (symbol)
                DO UPDATE SET
                price_usd = EXCLUDED.price_usd,
                market_cap = EXCLUDED.market_cap,
                timestamp = EXCLUDED.timestamp

        """, (
            coin["name"],
            coin["symbol"],
            coin["current_price"],
            coin["market_cap"],
            datetime.now()
        ))

    conn.commit()

    cur.close()
    conn.close()
