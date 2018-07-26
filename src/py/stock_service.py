from flask import Flask
app = Flask(__name__)

supported_symbol_list = ["5", "6", "700", "7336"]

def get_stock_by_symbol(symbol):
	return "{symbol: " + symbol + ", stock_price: " + str(73.2) + "}" if symbol in supported_symbol_list else "{}"

@app.route("/stock-service/symbol/<symbol>")
def get_stock(symbol):
  return get_stock_by_symbol(symbol)