@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
@bot.message_handler(commands=['mem'])
def send_mem(message):
    rnd = random.randint(1, 100)
    if rnd <= 60:
        img_name = "image1.jpg"
    elif rnd <= 90:
        img_name = "image2.jpg"
    elif rnd <= 99:
        img_name = "image3.jpg"
    else:
        images = os.listdir("images")
        other_images = [i for i in images if i not in {"image1.jpg", "image2.jpg", "image3.jpg"}]
        if other_images:
            img_name = random.choice(other_images)
        else:
            img_name = "image1.jpg"
    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)
bot.polling()
