from flask import Flask, render_template, request, jsonify
import requests

# Initialize Flask app
app = Flask(__name__)

# API Gateway URL
API_GATEWAY_URL = "http://localhost:8765"

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_currency():
    """Handle currency conversion requests."""
    from_currency = request.form['fromCurrency']
    to_currency = request.form['toCurrency']
    quantity = request.form['quantity']

    try:
        # Call the API Gateway for currency conversion using Feign
        response = requests.get(
            f"{API_GATEWAY_URL}/currency-conversion-feign/from/{from_currency}/to/{to_currency}/quantity/{quantity}"
        )
        response.raise_for_status()
        data = response.json()

        return jsonify({
            "success": True,
            "convertedAmount": data.get("totalCalculatedAmount", "N/A")
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)