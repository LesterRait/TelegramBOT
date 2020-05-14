import telebot
from telebot import types

bot = telebot.TeleBot('ADD TOKEN')


@bot.message_handler(commands=['Facebook'])
def facebook(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти на мой Facebook", url="https://www.facebook.com/LeesterRait"))
	bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы перейти на страницу",parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['Instagram'])
def instagram(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти в мой Instagram", url="https://www.instagram.com/Leeeesteeer/"))
	bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы перейти на страницу", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['VK'])
def vk(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Посетить мою страницу VK", url="https://vk.com/prog_life"))
	bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы перейти на страницу", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['Telegram'])
def vk(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Написать мне в Telegram", url="https://t.me/LesterRait"))
	bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы написать мне", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	btn1 = types.KeyboardButton('Обо мне')
	btn2 = types.KeyboardButton('Я в соц. сетях')
	btn3 = types.KeyboardButton('Мои работы')
	markup.add(btn1, btn2, btn3)
	send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nВ Telegram боте найдете все данные обо мне.\n С уважением Максим Ан"
	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text.strip().lower()

	if get_message_bot == "меню":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Обо мне')
		btn2 = types.KeyboardButton('Я в соц. сетях')
		btn3 = types.KeyboardButton('Поговори со мной')
		markup.add(btn1, btn2, btn3)

		final_message = "Тебе еще интересно? \nВыбери, что тебя интересует:"
	elif get_message_bot == "я в соц. сетях":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('/VK')
		btn2 = types.KeyboardButton('/Instagram')
		btn3 = types.KeyboardButton('/Facebook')
		btn4 = types.KeyboardButton('/Telegram')
		btn5 = types.KeyboardButton("Меню")
		markup.add(btn1, btn2, btn3, btn4, btn5)
		final_message = "Отлично, какие социальные сети тебя интересуют?"


	elif get_message_bot == "поговори со мной":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Привет')
		btn2 = types.KeyboardButton('Как жизнь?')
		btn3 = types.KeyboardButton('Что делаешь?')
		btn4 = types.KeyboardButton('Хочешь угарнуть?')
		btn5 = types.KeyboardButton("Меню")
		markup.add(btn1, btn2, btn3, btn4, btn5)
		final_message = "Отлично, о чём поговорим?"
	elif get_message_bot == "привет":
		markup = types.InlineKeyboardMarkup()
		final_message = "Привет!"
	elif get_message_bot == "как жизнь?":
		markup = types.InlineKeyboardMarkup()
		final_message = "Отлично! Что насчёт тебя?"
	elif get_message_bot == "что делаешь?":
		markup = types.InlineKeyboardMarkup()
		final_message = "Сижу, играю на гитаре, и думаю о тебе)"
	elif get_message_bot == "хочешь угарнуть?":
		markup = types.InlineKeyboardMarkup()
		final_message = "Угарать я люблю, хааххахаха"

	elif get_message_bot == "обо мне":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Кто ты?')
		btn2 = types.KeyboardButton('Чем увлекаешься?')
		btn3 = types.KeyboardButton("Меню")
		markup.add(btn1, btn2, btn3)
		final_message = "Отлично, что тебя интересует?"
	elif get_message_bot == "кто ты?":
		markup = types.InlineKeyboardMarkup()
		final_message = "Меня звать Максим Ан, родился 17 окт. 2003 года."
	elif get_message_bot == "чем увлекаешься?":
		markup = types.InlineKeyboardMarkup()
		final_message = "Увлечений у меня чертовски много, всё написать не смогу \nЯ играю на двух инструментах: гитара, фортепиано. "

	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Обо мне')
		btn2 = types.KeyboardButton('Я в соц. сетях')
		btn3 = types.KeyboardButton('Поговори со мной')
		markup.add(btn1, btn2, btn3)
		final_message = "Вот чёрт, ничего не выдало?\nПопробуй-ка воспользоваться кнопками"
	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)