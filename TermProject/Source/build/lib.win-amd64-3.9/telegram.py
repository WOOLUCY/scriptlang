'''
telegram.py
런처에서 텔레그램 버튼을 누르면 실행되는 모듈입니다.

functions
- sendSelectedInfo
'''

# === import ===
import telepot
import server
import tkinter.messagebox as msgbox

# === function ===
def sendSelectedInfo():     # 선택된 병원 정보를 텔레그램으로 보내는 함수
    if server.hospital_name == None: 
        msgbox.showinfo("알림", "목록에서 병원을 먼저 선택해주십시오.")
        return
    bot = telepot.Bot("5441441415:AAEolADNSY5sQlqcWJQCddqyQltgdB1hDh4")
    bot.sendMessage('5554103153', server.info_text + '\n\n' + '[검색결과]' + '\n' +'https://www.google.com/search?q=' + server.hospital_name)
    msgbox.showinfo("알림", "메시지를 성공적으로 보냈습니다.")

if __name__ == '__main__':
    print("telegram.py runned\n")
else:
    print("telegram.py imported\n")