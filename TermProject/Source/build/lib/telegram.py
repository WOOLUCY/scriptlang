import telepot
import server
import tkinter.messagebox as msgbox

def sendSelectedInfo():
    if server.hospital_name == None: 
        msgbox.showinfo("알림", "목록에서 병원을 먼저 선택해주십시오.")
        return
    bot = telepot.Bot("5441441415:AAEolADNSY5sQlqcWJQCddqyQltgdB1hDh4")
    bot.sendMessage('5554103153', server.info_text + '\n\n' + '[검색결과]' + '\n' +'https://www.google.com/search?q=' + server.hospital_name)