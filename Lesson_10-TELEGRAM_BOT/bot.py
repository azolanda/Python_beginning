from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from random import randint


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def goodbye(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Goodbye {update.effective_user.first_name}')


async def magic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    charmed_box = {1: 'Вам светит удача', 2: 'Ваш семейный бюджет пополнится',
                   3: 'Ваша жизнь изменится к лучшему', 4: 'Вас ждет неожиданная встреча',
                   5: 'Слушайте свою интуицию', 6: 'Слушайте зов сердца',
                   7: 'Праздники будут счастливыми', 8: 'Ваши желания исполнятся',
                   9: 'Вас ждут новые приключения', 10: 'Вас ждут новые достижения',
                   11: 'Вы получите интересное предложение',
                   12: 'Вам откроются перспективы в карьере', 13: 'Дома вас ждет уют',
                   14: 'Вас ждут новые знакомства', 15: 'Благоприятное время для поиска любви',
                   16: 'Вас ждет неожиданный подарок', 17: 'У вас откроется новый талант',
                   18: 'У вас появится новое хобби', 19: 'Вас ждет вкусный ужин',
                   20: 'Вы узнаете важный секрет', 21: 'Сделал дело - гуляй смело',
                   22: 'Вас ждет увлекательная поездка', 23: 'Ученье - свет',
                   24: 'Вас ждет интересная игра', 25: 'Вы любите и любимы',
                   26: 'Все проблемы и невзгоды пройдут стороной',
                   27: 'Вас ждет счастливая возможность', 28: 'Впереди долгожданная встреча',
                   29: 'Давние долги будут возвращены вам', 30: 'Удача придет, откуда не ждете',
                   31: 'Вы найдете то, что ищете'}

    charmed_num = randint(1, 31)
    await update.message.reply_text(f'{charmed_box[charmed_num]}')


app = ApplicationBuilder().token("HIDDEN_TOKEN").build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("goodbye", goodbye))
app.add_handler(CommandHandler("magic", magic))

app.run_polling()
