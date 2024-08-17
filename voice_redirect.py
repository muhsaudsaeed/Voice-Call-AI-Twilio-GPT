from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
from bot_response import bot_query
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a 'Hello world' message"""
    # Start our TwiML response
    response = VoiceResponse()
    gather = Gather(input='speech', action='/results', language='en-US', 
                    speechModel='phone_call', speechTimeout='auto')
    gather.say('Welcome to the Voice Call Assistant.')
    response.append(gather)
    response.redirect('/voice')
    return str(response)



@app.route('/results', methods=['GET', 'POST'])
def results_():
    """Respond to incoming phone calls."""
    userInput = request.form['SpeechResult']
    confidence = request.form['Confidence']
    # Start our TwiML response
    response = VoiceResponse()
    gather = Gather(input='speech', action='/results', language='en-US', 
                    speechModel='phone_call', speechTimeout='auto')
    bot_resp = bot_query(userInput)
    print(bot_resp)
    gather.say(bot_resp)
    response.append(gather)
    return str(response)


if __name__ == "__main__":
    app.run(debug=True)