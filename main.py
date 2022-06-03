import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

ticker = input("Introduzca un YAHOO TICKER: ")
print()
print("Introduzca los siguientes datos.")
print()
start = input("Fecha de Inicio (AAAA-MM-DD): ")
print()
end = input("Fecha de Término (AAAA-MM-DD): ")
print()
aapl_df = yf.download(ticker, 
                      start=start, 
                      end=end, 
                      progress=False,
)

print(aapl_df.head())
#print(help(yf.download))