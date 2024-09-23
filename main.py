import ptbot
from pytimeparse import parse
from SECRET import TELEGRAM_TOKEN


def wait(chat_id, question):
    message_id = bot.send_message(chat_id,"запускаю таймер")
    bot.create_timer(parse(question)+1, choose, author_id=chat_id, author_question=question)
    bot.create_countdown(parse(question), notify_progress, author_id=chat_id, message_id=message_id, author_question=question)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(round((iteration / float(total) -1)*-100,1))
    filled_length = int((round((iteration / total -1),1))*-length)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify_progress(secs_left, author_id, message_id, author_question):
    message = f"Осталось секунд: {secs_left} \n {render_progressbar(parse(author_question), secs_left)}"
    bot.update_message(author_id, message_id, message)


def choose(author_id, author_question):
    message = "Время вышло!"
    bot.send_message(author_id, message)


def main():
    bot.reply_on_message(wait)
    bot.run_bot()


if __name__ == '__main__':
    bot = ptbot.Bot(TELEGRAM_TOKEN)
    main()