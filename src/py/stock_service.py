import json
from flask import Flask
app = Flask(__name__)

symbol_map = {
	"00005.HK": {"desc": "HSBC HOLDINGS", "price": 74.55, "prev_close": 74.6},
	"00006.HK": {"desc": "POWER ASSETS", "price": 55.4, "prev_close": 55.95},
	"00700.HK": {"desc": "TENCENT", "price": 356.4, "prev_close": 367.2},
	"07336.HK": {"desc": "FI MR HS", "price": 5.73, "prev_close": 5.71}
}

def get_stock_by_symbol(symbol):
	return json.dumps(symbol_map.get(symbol) if symbol in symbol_map else {}, indent=2, separators=(", ", ": "))

@app.route("/stock-service/symbol/<symbol>")
def get_stock(symbol):
  return get_stock_by_symbol(symbol)