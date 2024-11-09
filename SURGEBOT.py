import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import os
import getpass
import requests
import colorama

# Initialize colorama
colorama.init()

# Define color variables
blue = colorama.Fore.LIGHTBLUE_EX
red = colorama.Fore.LIGHTRED_EX
green = colorama.Fore.LIGHTGREEN_EX
cyan = colorama.Fore.LIGHTCYAN_EX

# Define senders and receivers
senders = {
    "vladlord444@gmail.com": "edsl kboc pgoc yzib",
    "IvanKarma2000@gmail.com": "irlr cggo xksq tlbb",
    "misha28272727@gmail.com": "kgwq xvkg jycc ibkm",
    "edittendo0@gmail.com": "mzdl lrmx puyq epur",
    "shshsbsbsbwbwvw@gmail.com": "jqrx qivo qxjy jejt",
    "d6325841@gmail.com": "xuzq ztyx jzvb rant",
    "desireelinnert0@gmail.com": "xwzb lzla ppve hevz",
    "veterovseverov@gmail.com": "jubm pkhe udpr gkze",
    "Ivan27727272hwhs@gmail.com": "ozcu edfd gmgk rkqg",
    "dlyabravla655@gmail.com": "kprn ihvr bgia vdys",
    "topzone6400@gmail.com": "laum lkuc thvi lsol",
    "sanyaravanov@gmail.com": "xqvh vmmh omcy oata",
    "volkborz2022@gmail.com": "cdzp ghoo xhaj gegd",
    "borzghost2024@gmail.com": "tmnx xtka nsas soqb",
    "dlatt6677@gmail.com": "usun ruef otzx zcrh",
    "hujnadadada@gmail.com": "ydwe writ tlyf dxnl",
    "editt1345@gmail.com": "hezf xuel hzvz jzur",
    "ghostchat2023@gmail.com": "dezs aqvy mouq lfja"
}

receivers = {
    "support@telegram.org",
    "dmca@telegram.org",
    "security@telegram.org",
    "sms@telegram.org",
    "info@telegram.org",
    "marta@telegram.org",
    "spam@telegram.org",
    "alex@telegram.org",
    "abuse@telegram.org",
    "pavel@telegram.org",
    "durov@telegram.org",
    "elies@telegram.org",
    "ceo@telegram.org",
    "mr@telegram.org",
    "levlam@telegram.org",
    "perekopsky@telegram.org",
    "recover@telegram.org",
    "germany@telegram.org",
    "hyman@telegram.org",
    "qa@telegram.org",
    "stickers@telegram.org",
    "ir@telegram.org",
    "vadim@telegram.org",
    "shyam@telegram.org",
    "stopca@telegram.org",
    "u003esupport@telegram.org",
    "ask@telegram.org",
    "125support@telegram.org",
    "me@telegram.org",
    "enquiries@telegram.org",
    "api_support@telegram.org",
    "marketing@telegram.org",
    "ca@telegram.org",
    "recovery@telegram.org",
    "http@telegram.org",
    "corp@telegram.org",
    "corona@telegram.org",
    "ton@telegram.org",
    "sticker@telegram.org"
}

def clear():
    os.system("clear")

def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(red + f"Ошибка при отправке письма: {e}")
        return False

def handle_complaint(senders, receivers):
    total_emails = len(senders) * len(receivers)
    sent_emails = 0

    snosbot = blue + """
[1] Докс бот
[2] Рассылка порнографии
[3] Бот-мошенник
[4] Продажа запрещенных товаров/услуг
[5] Реклама
    """
    print(snosbot)
    complaint_choice = input(blue + "[?] Выберите причину сноса -> ")

    if complaint_choice in ["1", "2", "3", "4", "5"]:
        clear()
        bot = input(blue + "[?] Введите username бота -> ")
        complaint_texts = {
            "1": f"Здравствуйте, хочу пожаловаться и попросить заблокировать бота: {bot} данный бот служит для деанонимизации простых пользователей telegram",
            "2": f"Здравствуйте, уважаемая поддержка, я обнаружил бота который занимается рассылкой порнографии что запрещается на вашей площадке, username бота: {bot}",
            "3": f"Уважаемая поддержка, на вашей площадке telegram был обнаружен бот {bot}, данный бот является мошенническим в связи с чем прошу его заблокировать",
            "4": f"Приветствую, я обнаружил telegram бота {bot}, данный бот был создан для продажи запрещенных товаров и услуг что запрещается на вашей площадке, прошу принять меры",
            "5": f"Здравствуйте, на вашей площадке telegram мне я обнаружил бота который был создан для навязчивой рекламы, username бота: {bot} прошу как можно скорее принять меры"
        }

        for _ in range(len(senders) * len(receivers)):
            sender_email, sender_password = random.choice(list(senders.items()))
            receiver_email = random.choice(list(receivers))
            complaint_text = complaint_texts[complaint_choice]
            complaint_body = complaint_text.format(bot=bot.strip())
            if send_email(receiver_email, sender_email, sender_password, "Жалоба на Telegram бота", complaint_body):
                print(red + "[!] Успешно отправлено")
                sent_emails += 1
            else:
                print(red + "[!] Ошибка при отправке")
                getpass.getpass(blue + "Нажмите ENTER для возврата в главное меню\n")
                os.system("python SURGE_SNOSv2.py")
    else:
        getpass.getpass(red + "[!] Произошла ошибка, перепроверьте вводимые данные и нажмите ENTER для возврата в главное меню\n")
        clear()
        os.system("python SURGE_SNOSv2.py")

if __name__ == "__main__":
    clear()
    handle_complaint(senders, receivers)
