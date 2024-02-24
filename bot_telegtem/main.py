import telebot
from telebot.types import User
import random

# "cat_1.jpg", "cat-car.jpg", "mostafa.jpg", "patrik.jpg"
MY_PHOTOS = ["cat_1.jpg", "cat-car.jpg", "patrik.jpg"]


bot = telebot.TeleBot("6730687393:AAF3yWfeFWi5AhteMjAOPdeorpVjTRUY4SU")

print("---------------------------------------")
my_ansers = {
    "mostafa": """سلام مصطفی حالت چطوره؟""",
    "mahdi": """سلام مهدی حالت چطوره؟""",
}


@bot.message_handler(commands=["profilephotos"])
def get_user_profiles(message):
    user_id = message.from_user.id
    profile_photos = bot.get_user_profile_photos(user_id)

    if profile_photos.total_count > 0:
        for photo in profile_photos.photos:
            bot.send_photo(message.chat.id, photo[-1].file_id)
    else:
        bot.send_message(message.chat.id, "Don't have profile")


counter_photos = 0


@bot.message_handler(commands=["photo"])
def send_photo(message):
    global counter_photos
    counter_photos += 1
    i = random.choice(MY_PHOTOS)
    bot.send_photo(
        message.chat.id,
        open(f"C:/Users/Almas Rayan/Desktop/bot_telegtem/photos/{i}", "rb"),
    )
    print(f"counter_photos ==> {counter_photos}")


counter_audio = 0


@bot.message_handler(func=lambda message: True)
def send_message(message):
    user = message.from_user
    if message.text == "audio":
        bot.send_audio(message)

    elif message.text == "photo":
        bot.send_photo(message)

    elif message.text == "profilephotos":
        bot.get_user_profile_photos(message)

    elif user.username == "Storm0o0":
        message_Mostafa = message.text
        with open("texts/text_mostafa.txt", "a", encoding="utf-8") as f:
            f.write(f"messge mostafa ==>\t{str(message_Mostafa)}\n")
        bot.reply_to(message, my_ansers["mostafa"])

    elif user.username == "Mahdi_1134":
        bot.reply_to(message, my_ansers["mahdi"])

    else:
        bot.reply_to(
            message,
            f"سلام  {user.full_name},از این که وارد ربات ما شدید از شما ممنونیم \n,شما یک ربات {user.is_bot} هستید,ایدی تلگرام شما \n{user.username} هست.",
        )


if __name__ == "__main__":
    bot.polling()
