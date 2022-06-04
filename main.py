import pandas as pd
import yfinance as yf
#from yahoofinancials import YahooFinancials
#from get_all_tickers import get_tickers as gt

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

# time_interval = input('Intervalo de tiempo (daily, weekly, montly, annual): ')
# yahoo_financials = YahooFinancials('AAPL')
# aapl_df = yahoo_financials.get_historical_price_data(start_date='2019-01-01', 
#                                                   end_date='2019-12-31', 
#                                                   time_interval=time_interval)

aapl_df = pd.DataFrame(aapl_df)

print(aapl_df.head())
#print(help(yf.download))