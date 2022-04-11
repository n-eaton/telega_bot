from datetime import datetime

def sample_responses (input_text):
    user_message = str(input_text).lower()

    if user_message in ('hey', 'sup', 'hi', 'hello', 'whats up'):
        return "Hey! How's it going?"

    if user_message in ('who are you?', "what's your name", 'who are you'):
        return "I am a bot"

    if user_message in ("time", "what's the time", "what time is it?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    return "I have know idea what you are talking about"
