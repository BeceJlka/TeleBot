import os
import telebot

token = os.getenv("TOKEN")

bot = telebot.TeleBot(token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Где ты', 'Связаться')
keyboard1.row('Инфо', 'Список команд')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Резюме', 'linkedin', 'Drive2')
keyboard2.row('Почта', 'back')
keyboard2.row('Оставить свой контакт')
last_location_latitude = 0
last_location_longitude = 0


@bot.message_handler(commands=['start'])
def i_can_start(message):
    bot.send_message(message.chat.id, 'Вы написали мне чем могу помочь?',
                     bot.send_message(message.chat.id, message.from_user.first_name),
                     reply_markup=keyboard1)


@bot.message_handler(content_types=['location'])
def my_location(message):
    if message.chat.id == 282060981:
        global last_location_latitude
        global last_location_longitude
        last_location_latitude = message.location.latitude
        last_location_longitude = message.location.longitude


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'инфо':
        bot.send_message(message.chat.id,
                         'Здесь вы можете найти информацию про создателя',
                         reply_markup=keyboard2)
    elif message.text.lower() == 'список команд':
        bot.send_message(message.chat.id,
                         'Инфо -- Найдете информацию про меня\n'
                         'Резюме -- Найдете мое резюме\n'
                         'linkedin -- Моя страничка на Линкедин\n'
                         'Где ты -- Данные о моем последнем местоположении\n'
                         'Drive2 -- Моя станичка на Драйв2\n'
                         'Почта -- Моя рабочая почта\n'
                         'Пока -- Бот попрощаеться с вами\n', reply_markup=keyboard1)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощайте, заходите к нам еще',
                         bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAIiKF471BJMj6ggpKgVeOJawauo8zD1AAJCAQACYyviCaDbFw5JxdrFGAQ"))
    elif message.text.lower() == 'почта':
        bot.send_message(message.chat.id, 'TimurLakoba@gmail.com')
    elif message.text.lower() == 'drive2':
        bot.send_message(message.chat.id, 'https://www.drive2.ru/users/govoroon')
    elif message.text.lower() == 'резюме':
        bot.send_message(message.chat.id, 'https://drive.google.com/open?id=1ZLcNbvztQj8jSkWv9Xwe948Zpm-NiUks')
    elif message.text.lower() == 'linkedin':
        bot.send_message(message.chat.id, 'https://www.linkedin.com/in/timur-lakoba-a413b2198')
    elif message.text.lower() == 'где ты' or message.text.lower() == 'туда':
        bot.send_message(message.chat.id, 'Последний раз был тут!',
                         bot.send_location(message.chat.id, last_location_latitude, last_location_longitude),
                         reply_markup=keyboard1)
    elif message.text.lower() == 'связаться':
        bot.send_message(message.chat.id,
                         'Ваше уведомление доставлено',
                         bot.send_message('282060981', 'Тебе там написали!'), reply_markup=keyboard1)
    elif message.text.lower() == 'back':
        bot.send_message(message.chat.id, 'Вернемся назад', reply_markup=keyboard1)


bot.polling()
