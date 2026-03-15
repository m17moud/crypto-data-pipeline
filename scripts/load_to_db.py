import psycopg2
from datetime import datetime


def load_data(data):

    conn = psycopg2.connect(
        host="localhost",
        database="crypto_db",
        user="postgres",
        password="YOUR_PASSWORD"
    )

    cur = conn.cursor()

    for coin in data:
        cur.execute("""
            INSERT INTO crypto_prices
            (coin_name, symbol, price_usd, market_cap, timestamp)
            VALUES (%s,%s,%s,%s,%s)
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