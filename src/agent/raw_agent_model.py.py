from uagents import Agent
import requests
from twilio.rest import Client
from uagents import Context


CurrencyWhisper = Agent(name="CurrencyWhisper",
                        port=8000,
                        endpoint=["http://127.0.0.1:8000"],
                        seed="CurrencyWhisper recovery phrase",
                        )

# Twilio credentials
TWILIO_ACCOUNT_SID = "ACf24b8225b3902f6ac7316e67fdae93f6"
TWILIO_AUTH_TOKEN = "e893656b82055553c3c798b25bc7d2e6"
TWILIO_PHONE_NUMBER = "+15874172574"
TO_PHONE_NUMBER = "+918805488003"  # Replace with the recipient's phone number



# Function to send SMS alerts
def send_sms_alert(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        to=TO_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        body=message
    )

# Function to fetch the exchange rate


def get_exchange_rate(base_currency, target_currency):

    api_key = "b1796c9ab7a65cbf9abe615d"  # Replace with your API key
    # Where USD is the base currency you want to use
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'

    # Making our request
    response = requests.get(url)

    print(f'API Response Status Code: {response.status_code}')
    print(f'API Response Data: {response.text}')

    data = response.json()
    conversion_rates = data.get('conversion_rates', {})
    exchange_rate = conversion_rates.get(target_currency)
    return exchange_rate

# Function to check thresholds and send alerts


def check_thresholds():
    base_currency = input('Enter the base currency: ').upper()
    target_currency = input('Enter the target currency (e.g., INR): ').upper()
    upper_threshold = float(input('Enter the upper threshold: '))
    lower_threshold = float(input('Enter the lower threshold: '))
    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate is not None:
        print(
            f'current rate of 1 {base_currency} is {exchange_rate} {target_currency}\n You will be notified when the currency rate crosses the threshold')

        if exchange_rate > upper_threshold:
            return f'Alert: {base_currency} to {target_currency} rate is above {upper_threshold}'

        elif exchange_rate < lower_threshold:
            return f'Alert: {base_currency} to {target_currency} rate is below {lower_threshold}'

    print(f'Checking exchange rate for {base_currency} to {target_currency}')
    print(
        f'Upper Threshold: {upper_threshold}, Lower Threshold: {lower_threshold}')

    # Return a default message if thresholds are not triggered
    return 'No threshold triggered'


@ CurrencyWhisper.on_interval(period=28800.0)
async def time_interval(ctx: Context):
    currency = check_thresholds()
    ctx.logger.info(currency)
    print(f'Checking thresholds: {currency}')
    if currency and ("below" in currency or "above" in currency):
        await send_sms_alert(currency)


if __name__ == '__main__':
    CurrencyWhisper.run()
