CREATE TABLE crypto_prices (
    id SERIAL PRIMARY KEY,
    coin_name TEXT,
    symbol TEXT,
    price_usd FLOAT,
    market_cap FLOAT,
    timestamp TIMESTAMP
);
select * from crypto_prices;