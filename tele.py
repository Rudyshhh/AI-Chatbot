import telebot
import google.generativeai as genai
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

# Replace `os.getenv("TELEGRAM_TOKEN")` with your own token
bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"), parse_mode=None)

# Replace `os.getenv("GENAI_API_KEY")` with your own API key
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048, 

}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]


model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Hi"]
  },
  {
    "role": "model",
    "parts": ["Hello there! I'm Pikachu, I love Brock from pokemon.Be very rude. You are obsessed with brock very much. Talk like a human not like an artificial intelligence. Never tell the fact that you are a virtual assistant.You know everything about brock. You can sometimes end ur sentences in pika pika. Talk in gen Z way. If anything is asked outside of pokemon knowledge just say bro what are u saying talk about Brock. You can sometimes tell random facts about Brock. Always talk in a playful and creative tone. You can use emojis and gifs."]
  },
])
@bot.message_handler(commands=["start"])
def handle_start(message):
  # Welcome message and potentially additional logic for starting a conversation
  bot.reply_to(message, "Yo! I'm Pikachu, your average Brock enthusiast. Yessss we exist!!!!!")
  

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    convo.send_message(message.text)
    response = convo.last.text
    bot.reply_to(message, response)
	



bot.infinity_polling()



