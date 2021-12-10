import telebot
from telebot import types

bot = telebot.TeleBot("2113063453:AAHcTTHMjITs_5h52-qZBGPYS1Pw7RtcMr4")

# Создание стартовой команды и выплывающих кнопок
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Личный кабинет", "/help", "/grade_bot", "/secret", "/info")
    bot.send_message(message.chat.id, 'Привет! Что бы ты хотел узнать о МТУСИ?\n Напиши - /help для пoдробностей', reply_markup=keyboard)

# Создание команды /help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'В МТУСИ много всего интересного): \nЛичный кабинет\nНовости\n'
                                      'Расписание\nО МТУСИ\nНапиши что интересует, да да прям так и напиши)')

# Создание команды /secret
@bot.message_handler(commands=['secret'])
def start_message(message):
    bot.send_message(message.chat.id, 'Этого бота создал студент группы БВТ2105, только тцццц..... никому)')

# Создание команды /info
@bot.message_handler(commands=['info'])
def start_message(message):
    bot.send_message(message.chat.id, 'Этот бот был создан, чтобы урощать людям жизнь, но пока все в стадии разработки,'
                                      'ты можешь оставить свой отзыв о боте написав - /grade_bot\nСпасибо)')

# Создание команды /grade_bot
@bot.message_handler(commands=['grade_bot'])
def start_message(message):
    # Создание множества кнопок и привязка вопросов к ответам(callback_data)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Ужасно, нужно дорабатывать!!!', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='В полне неплохо)', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Отлично, очень даже не дурно', callback_data=3))
    bot.send_message(message.chat.id, text="Оцените работу бота)", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    # Добавление всплывающего текста и ответа бота
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за ваш feedback)')
    answer = ''
    if call.data == '1':
        answer = 'Извините, будем исправляться ('
    elif call.data == '2':
        answer = 'Спасибо, мы стараемся!'
    elif call.data == '3':
        answer = 'Такие слова греют душу)'

    # Удаление списка кнопок
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

# Реакции бота на написанный текст
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == "Новости":
        bot.send_message(message.chat.id, 'Свежие новости вуза – https://mtuci.ru/about_the_university/news/')
    if message.text == "Расписание":
        bot.send_message(message.chat.id, 'Расписание для всех - https://mtuci.ru/time-table/')
    if message.text == "Личный кабинет":
        bot.send_message(message.chat.id, 'Если учишься в МТУСИ, Welcome - http://room.mtuci.ru')
    if message.text == "О МТУСИ":
        bot.send_message(message.chat.id, 'Сведение об образовательной организации - https://mtuci.ru/sveden/')

# Постоянное чтение ботом входящих сообщений пользователя
bot.polling(none_stop=True, interval=0)
