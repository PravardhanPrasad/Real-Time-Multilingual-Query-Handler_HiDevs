from googletrans import Translator

translator = Translator()

def translate_to_english(text):
    try:
        translated = translator.translate(text, dest='en')
        return translated.text
    except Exception as e:
        return f"❌ Translation error: {str(e)}"

def generate_auto_response(english_text):
    if "how are you" in english_text.lower():
        return "I'm doing well, thank you! How can I assist you today?"
    elif "price" in english_text.lower():
        return "Our pricing depends on your location. Please visit our pricing page."
    elif "help" in english_text.lower():
        return "Sure, we're here to help! Please describe your issue."
    else:
        return "Thank you for reaching out. We'll get back to you shortly."
