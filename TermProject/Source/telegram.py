import telepot
import server

def sendSelectedInfo():
    bot = telepot.Bot("5441441415:AAEolADNSY5sQlqcWJQCddqyQltgdB1hDh4")
    bot.sendMessage('5554103153', server.info_text)

