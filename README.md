# 📆 Twilio WhatsApp Scheduler Bot

A Python-based WhatsApp bot that allows users to schedule messages to be sent automatically via WhatsApp using Twilio's API.

## 🚀 Features

- ✅ Schedule WhatsApp messages to be sent at a future time.
- ⏰ Supports custom message text and scheduled time.
- 📲 Uses Twilio WhatsApp API for message delivery.

---

## 🛠️ Tech Stack

- Python 
- Flask
- Twilio API – for WhatsApp messaging
- APScheduler – for scheduling messages

---

## Environment variables
- Create a .env file in the root directory and add the following:
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
TO_WHATSAPP_NUMBER=whatsapp:+your_verified_number


## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/twilio-whatsapp-scheduler.git
cd twilio-whatsapp-scheduler

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt


