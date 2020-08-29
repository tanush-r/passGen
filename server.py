from api_handler import telegram_chatbot
import generator

bot = telegram_chatbot("config.cfg")
update_id = None

print("Started server...")
running = True
loggedDict = {}

while running:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    send = ""
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            user_id = item["message"]["from"]["id"]

            if message == "/start":
                print("Session start id:", user_id)
                if user_id not in loggedDict:
                    loggedDict[user_id] = False
                    send = "Hey! Welcome to password manager!\n/gen : Generate new password\n/end : End session"
                else:
                    send = "Session already started\n/gen : Generate new password\n/end : End session"

            elif message == "/gen":
                try:
                    check = loggedDict[user_id]
                    loggedDict[user_id] = True
                    send = "Enter length (minimum 6 characters, maximum 15 characters)"
                except:
                    send = "To begin session, enter /start"

            elif message in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']:
                if loggedDict[user_id]:
                    if 6 <= int(message) <= 15:
                        send = generator.randomGen(int(message))
                    else:
                        send = "Wrong length, try again"

            elif message == "/end":
                if user_id in loggedDict.keys():
                    del loggedDict[user_id]
                    send = "Goodbye! You will not be missed\nEnter /start to start bot again"

            else:
                send = "To begin session, enter /start"

            bot.send_message(send, user_id)
