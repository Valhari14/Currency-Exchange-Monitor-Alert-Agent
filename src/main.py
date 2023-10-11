from uagents import Agent,Context
from flask import Flask, render_template, request
from twilio.rest import Client
import requests
from decouple import config



# Initialize your CurrencyWhisper agent
CurrencyWhisper = Agent(
    name="CurrencyWhisper",
    port=8000,
    endpoint=["http://127.0.0.1:8000"],
    seed="CurrencyWhisper recovery phrase"
)

app = Flask(__name__)

# Retrieve Twilio credentials from environment variables
TWILIO_ACCOUNT_SID = config('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = config('TWILIO_PHONE_NUMBER')
TWILIO_TO_PHONE_NUMBER = config('TWILIO_TO_PHONE_NUMBER')

# Function to send SMS alerts
def send_sms_alert(message, phone_number):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        to=phone_number,
        from_=TWILIO_PHONE_NUMBER,
        body=message
    )

# Function to fetch the exchange rate
def get_exchange_rate(base_currency, target_currency):
    API_KEY = config('API_KEY')
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}'
    response = requests.get(url)
    data = response.json()
    conversion_rates = data.get('conversion_rates', {})
    exchange_rate = conversion_rates.get(target_currency)
    return exchange_rate

# Function to check thresholds and send alerts
def check_thresholds(base_currency, target_currency, threshold_type, threshold_amount, phone_number):
    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate is not None:
        message = f'Current rate of 1 {base_currency} is {exchange_rate} {target_currency}. '

        if threshold_type == 'Upper' and exchange_rate > threshold_amount:
            message += f'Alert: {base_currency} to {target_currency} rate is above {threshold_amount}'
            send_sms_alert(message, phone_number)
        elif threshold_type == 'Lower' and exchange_rate < threshold_amount:
            message += f'Alert: {base_currency} to {target_currency} rate is below {threshold_amount}'
            send_sms_alert(message, phone_number)

    return message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    base_currency = request.form['basecurrency'].upper()
    target_currency = request.form['targetcurrency'].upper()
    threshold_type = request.form['limit']
    threshold_amount = float(request.form['amount'])
    phone_number = request.form['phone']

    message = check_thresholds(
        base_currency, target_currency, threshold_type, threshold_amount, phone_number)

    return render_template('index.html', message=message)

@ CurrencyWhisper.on_interval(period=3600.0)
async def time_interval(ctx: Context):
    currency = check_thresholds()
    ctx.logger.info(currency)
    print(f'Checking thresholds: {currency}')
    if currency and ("below" in currency or "above" in currency):
         send_sms_alert(currency)

if __name__ == '__main__':
    app.run(debug=True)
