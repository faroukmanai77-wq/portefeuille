#!/usr/bin/env python3
"""
Met à jour prices.json avec les derniers prix de clôture/temps quasi-réel
pour chaque fonds défini dans data.json (champ funds.<SYMBOLE>.source).

Ce script tourne côté serveur (GitHub Actions), donc aucune restriction
CORS ne s'applique ici (contrairement à un appel depuis le navigateur).

Utilise yfinance (Yahoo Finance, non officiel mais fiable en usage serveur).
"""
import json
import os
import sys
from datetime import datetime, timezone

try:
    import yfinance as yf
except ImportError:
    print("ERREUR: le paquet 'yfinance' n'est pas installé (pip install yfinance)", file=sys.stderr)
    sys.exit(1)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(ROOT, "data.json")
PRICES_FILE = os.path.join(ROOT, "prices.json")


def load_json(path, default):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default


def main():
    data = load_json(DATA_FILE, {})
    prices = load_json(PRICES_FILE, {})

    fund_order = data.get("fundOrder", [])
    funds = data.get("funds", {})
    now = datetime.now(timezone.utc).isoformat()

    updated = 0
    for symbol in fund_order:
        meta = funds.get(symbol, {})
        ticker_symbol = (meta.get("source") or "").strip()
        if not ticker_symbol:
            print(f"SKIP {symbol}: aucun symbole source défini")
            continue
        try:
            ticker = yf.Ticker(ticker_symbol)
            hist = ticker.history(period="5d")
            if hist.empty or "Close" not in hist:
                print(f"WARN {symbol} ({ticker_symbol}): aucune donnée retournée")
                continue
            last_close = hist["Close"].dropna()
            if last_close.empty:
                print(f"WARN {symbol} ({ticker_symbol}): pas de prix de clôture disponible")
                continue
            price = float(last_close.iloc[-1])
            prices[symbol] = {
                "price": round(price, 4),
                "updated": now,
                "source": ticker_symbol,
            }
            updated += 1
            print(f"OK {symbol} ({ticker_symbol}): {price:.4f}")
        except Exception as e:
            print(f"ERREUR {symbol} ({ticker_symbol}): {e}")

    with open(PRICES_FILE, "w", encoding="utf-8") as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Terminé : {updated}/{len(fund_order)} fonds mis à jour.")


if __name__ == "__main__":
    main()
