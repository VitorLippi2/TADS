import yfinance as yf

tkr =  yf.Ticker('PETR4.SA')
hist = tkr.history(period="5d")

hist = hist.drop("Dividends", axis=1)
hist = hist.drop("Stock Splits", axis=1)

hist = hist.reset_index()
print(hist)