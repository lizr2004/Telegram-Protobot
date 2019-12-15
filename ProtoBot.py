import random, json, time
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
fp = json.load(open("wordlist_zh.json"))
co = json.load(open("config.json"))

token = co['token']
con = fp['constraints']
ite = fp['items']
pre = fp['prependText']

def getIdea():
    random.seed(time.time())
    r = ''
    c = random.choice(con)
    i = random.choice(ite)
    if c.startswith('为'):
        return c + pre + i
    else:
        return pre + c + i

def handleInlineQuery(bot, updater):
    result = []
    for x in range(10):
        r = getIdea()
        t = InlineQueryResultArticle(str(x), r, InputTextMessageContent(r))
        result.append(t)
    updater.inline_query.answer(result, cache_time=0)

def handleCommand(bot, updater):
    updater.message.reply_text(getIdea())

def initBot():
    updater = Updater(token)
    updater.dispatcher.add_handler(InlineQueryHandler(handleInlineQuery))
    updater.dispatcher.add_handler(CommandHandler(['getidea'], handleCommand))
    updater.start_polling()
    updater.idle()

initBot()
