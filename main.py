import telebot
from telebot import types
import Articles
from random import sample

bot = telebot.TeleBot("ТОКЕН ВСТАВИТЬ СЮДА ВМЕСТО ЭТОГОГО ТЕКСТА БЕЗ ПРОБЕЛОВ", # можешь заменить этот токен внутри ковычек на свой либо оставить и использовать моего бота
                      parse_mode=None)


def texts():
    text_with_articles = sample(Articles.texts, len(Articles.texts))
    for i in text_with_articles:
        text = i['text']
        number = i['amount_of_articles']
        articles = i['articles']

        yield text, articles, number


params = list(texts())
amount_of_articles = params[0][2]
text = params[0][0]
articles = params[0][1]
answer = ''


def reroll():
    global params, amount_of_articles, text, articles, answer
    params = list(texts())
    amount_of_articles = params[0][2]
    text = params[0][0]
    articles = params[0][1]
    answer = ''


def test(message):
    global answer
    answer = message.text


@bot.message_handler(commands=['start'])
def start(message):
    global answer, articles, amount_of_articles, text
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    buttons.add(types.KeyboardButton("An"), types.KeyboardButton("A"), types.KeyboardButton("The"), types.KeyboardButton("-"))
    msg = bot.send_message(message.chat.id, f'Choose the right article \n \n {text}', reply_markup=buttons)

    bot.register_next_step_handler(msg, test)
    for i in range(amount_of_articles):
        while not answer:
            pass
        else:
            if answer.lower() == articles[0].lower():
                text = text.replace("___", articles.pop(0), 1)
                msg = bot.send_message(message.chat.id, f'Right! \n\n {text}', reply_markup=buttons)
                if not i == amount_of_articles - 1:
                    bot.register_next_step_handler(msg, test)
                answer = ''
            else:
                right = articles[0]
                text = text.replace("___", articles.pop(0), 1)
                msg = bot.send_message(message.chat.id, f"Nope! Right is {right} \n\n {text}", reply_markup=buttons)
                if i != amount_of_articles - 1:
                    bot.register_next_step_handler(msg, test)
                answer = ''
    else:
        bot.send_message(message.chat.id, 'Game is over, type /start to play again', parse_mode='MarkdownV2')
        reroll()


bot.infinity_polling()