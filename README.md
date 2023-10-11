# Currency Exchange Monitor & Alert Agent


## Description

The Currency Exchange Monitor & Alert Agent is a Python application developed using Fetch ai's uAgent framework that allows users to monitor real-time currency exchange rates and receive alerts when exchange rates cross specified thresholds. 
It is powered by the uAgent library, enabling a seamless and automated monitoring process. 
This application empowers users to stay informed about currency fluctuations.

##Features
1.Real-time Exchange Rate Monitoring: Stay updated with accurate and real-time exchange rate data, providing you with the most current information for your selected currency pairs.

2.Multi-Currency Support: Choose your base currency and one or more foreign currencies to monitor. This feature allows you to track multiple currency pairs simultaneously.

3.Customizable Thresholds: Set personalized upper and lower thresholds for exchange rates. Receive alerts when rates cross these predefined levels, helping you make timely decisions.

4.SMS Notifications: Receive SMS alerts directly to your phone through the Twilio integration. These notifications keep you informed, even when you're on the go.

5.Customizable Alerts: Alerts are tailored to your preferences, allowing you to specify currency pairs and threshold levels, ensuring you only receive relevant notifications.

6.User-Friendly Web Interface: Access the application through a user-friendly web interface, making it easy to configure and monitor exchange rates.

## Instructions to Run the Project

To run the Currency Exchange Monitor & Alert Agent project, follow these steps:

On your computer, you may need to install:

Python 3.8, 3.9 or 3.10.

PIP (Python Installs Packages).

Poetry for virtual environment.

uAgents framework,

Twilio framework for sending messages.

for more info visit: (https://fetch.ai/docs/guides/agents/installing-uagent)

**Configuration:**

- Set up a Twilio account and obtain the following credentials:
  - Twilio Account SID
  - Twilio Auth Token
  - Twilio Phone Number (a phone number purchased or received from Twilio)
  - Recipient Phone Number (the phone number where you want to receive notifications)

- Open the `main.py` file and replace the placeholders for Twilio credentials with your actual Twilio credentials:

  ```python
  TWILIO_ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID'
  TWILIO_AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'
  TWILIO_PHONE_NUMBER = 'YOUR_TWILIO_PHONE_NUMBER'
  TO_PHONE_NUMBER = 'RECIPIENT_PHONE_NUMBER'
  ```

-Set up API KEY for currency exchange monitor
 -visit: (https://www.exchangerate-api.com/) 
 -obtain api-key

- Open the `main.py` file and replace the placeholders for API_KEY with your actual API_KEY:

  ```python
  API_KEY = 'YOUR API_KEY'
  ```


**Running the Application:**

- Execute the following command to start the Flask application:

Create a virtual environment.

  ```
  python main.py
  ```

- Access the application by opening a web browser and navigating to `http://localhost:5000`.

5. **Monitoring Exchange Rates:**

- Input your base currency, target currency, select the threshold amount with the limit - upper/lower.
- You will receive SMS alerts via Twilio when exchange rates cross the specified thresholds.

## Special Considerations

- This project utilizes the uAgent library, a tool for creating and managing agents to monitor exchange rates in the background.

- The application leverages the Twilio API for sending SMS notifications when exchange rates cross specified thresholds. Make sure you have a valid Twilio account and have configured the Twilio credentials in the `main.py` script.

-The application also leverages the Exchange rate api-key, replace it with you own api key.