# Voice Call AI with Twilio and OpenAI

This project is a Flask-based application that uses Twilio and OpenAI to create an AI-driven voice call system. The system allows users to make a voice call to a specified number, where the AI will respond to queries.

## Prerequisites

- Python 3.10.12
- Twilio Account
- OpenAI API Key

## Setup Instructions

### 1. Twilio Setup

1. [Sign up for a Twilio account](https://www.twilio.com/try-twilio).
2. Buy a Twilio phone number to use for the calls.
3. Add a balance to your Twilio account to cover call costs.

### 2. OpenAI Setup

1. Sign up for an [OpenAI account](https://beta.openai.com/signup/).
2. Obtain an OpenAI API key from the OpenAI dashboard.
3. Store the API key securely as it will be used to generate responses from the OpenAI model.

### 3. Python Environment Setup

1. Ensure you have Python 3.10.12 installed on your system.
2. Create a Python virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

4. Install the required packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

### 4. Running the Application

1. Run the Flask application:

    ```bash
    python voice_redirect.py
    ```

2. Create an ngrok link to expose port 5000 to the internet:

    ```bash
    ngrok http 5000
    ```

3. Copy the ngrok link and add it to the `.env` file under the variable `CALL_REDIRECT_URL`.

4. Add your Twilio phone number to the `.env` file with the variable name `TWILIO_PHONE_NUMBER`.

5. Add the recipient phone number (where you want to test the call) to the `.env` file with the variable name `TO_PHONE_NUMBER`.

### 5. Making a Test Call

1. Run the following command to initiate a call:

    ```bash
    python voice_call.py
    ```

2. You will receive a call on the phone number specified in the `TO_PHONE_NUMBER` variable.

## Notes

- Ensure that your Twilio account is set up correctly with a balance, a phone number, and API credentials.
- The OpenAI API key is required to generate responses during the call.

## Troubleshooting

If you encounter any issues, ensure that all environment variables are set correctly in the `.env` file, and that your Python environment is activated.
