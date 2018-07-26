from flask import Flask
app = Flask(__name__)

supported_stock_code = ["5", "6", "700", "7336"]

def get_stock_by_code(stock_code):
	return "{stock_code: " + stock_code + ", stock_price: " + str(73.2) + "}" if stock_code in supported_stock_code else "{}"

@app.route("/stock-api/stock_code/<stock_code>")
def get_stock(stock_code):
  return get_stock_by_code(stock_code)