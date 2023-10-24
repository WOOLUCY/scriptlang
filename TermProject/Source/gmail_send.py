'''
gmail_send.py
런처에서 이메일 버튼을 누르면 실행되는 모듈입니다.

functions
- sendMail
- onEmailInput
- onEmailPopup
'''
# === import ===
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
import tkinter.messagebox as msgbox
import server

# === functions ===
def sendMail(fromAddr, toAddr, msg):    # SMTP 연결로 메일을 보내는 함수
    import smtplib # 파이썬의 SMTP 모듈
    # 메일 서버와 connect하고 통신 시작
    s = smtplib.SMTP("smtp.gmail.com", 587) # SMTP 서버와 연결
    s.starttls() # SMTP 연결을 TLS (Transport Layer Security) 모드로전환
    
    # 앱 password 이용
    s.login('kikanaidek@gmail.com', '') 
    s.sendmail(fromAddr , [toAddr], msg.as_string())
    s.close()

def onEmailInput():     
    # 이메일 주소를 입력 후 버튼 클릭 시 실행되는 함수
    # HTML 파일 변환, 작성
    # 메시지 보내기
    senderAddr = "kikanaidek@gmail.com"
    addrEmail = inputEmail.get()

    if '@' in addrEmail and addrEmail != '':
        # HTML 전달을 위해 컨테이너 역할을 할 수 있는 "multipart/alternative" 타입사용
        msg = MIMEMultipart('') 
        msg['Subject'] = "어디병원에서 찾으신 병원정보입니다." 
        msg['From'] = 'where the hospital' 
        msg['To'] = addrEmail 

        # 파일로부터 읽어서 MIME 문서를 생성. 
        htmlFD = open("image/logo.html", 'rb')
        HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8' )
        htmlFD.close()
        # 만든 mime을 MIMEBase에 첨부. 
        msg.attach(HtmlPart)

        # 텍스트 형식의 본문 내용
        info = server.info_text + '\n\n' + '[검색결과]' + '\n' +'https://www.google.com/search?q=' + server.hospital_name
        text = MIMEText(info, _charset = 'UTF-8')
        # Data 영역의 메시지에 바운더리 추가
        msg.attach(text)

        try:
            sendMail(senderAddr, addrEmail, msg)
            msgbox.showinfo("알림", "정상적으로 메일을 보냈습니다.")
            inputEmail.focus_set()
            inputEmail.delete(0, 'end')
        except: # 예외처리: 메일 보내기에 실패했을 때
            msgbox.showerror("Error", "유효하지 않은 메일주소입니다.")
            inputEmail.focus_set()
            inputEmail.delete(0, 'end')
        
    else:
        # 예외처리: 메일 형식이 맞지 않을 때
        response = msgbox.askretrycancel("Error", "유효하지 않은 메일입니다. 다시 시도하시겠습니까?")
        if response == 1: 
            inputEmail.focus_set()
            inputEmail.delete(0, 'end')

def onEmailPopup():     
    # 런처에서 메일 버튼 누르면 실행되는 함수
    # 이메일 입력창 팝업

    # 예외처리: 사용자가 병원을 선택하지 않고, 버튼을 누를 경우
    if server.hospital_name == None: 
        msgbox.showinfo("알림", "목록에서 병원을 먼저 선택해주십시오.")
        return

    global addrEmail, popup
    addrEmail = None 
    popup = Toplevel() # popup 띄우기
    popup.geometry("300x100+650+400")
    popup.title("병원 정보 이메일로 보내기")
    popup.resizable(False, False)
    global inputEmail, btnEmail, textLabel, mailListBox, btnSend

    # 설명 라벨 부분
    textLabel = Label(popup, text="받을 이메일을 입력하십시오", font=server.fontNormal)
    textLabel.place(x=5, y=5, width=300, height=30)

    # 사용자 입력 부분
    inputEmail = Entry(popup, font=server.fontNormal)
    inputEmail.place(x=10,y = 35, width = 280, height= 30)

    btnEmail = Button(popup, text="메일 보내기", command=onEmailInput, font=server.fontNormal, cursor="hand2")
    btnEmail.place(x=10,y = 65, width = 280, height= 30)


if __name__ == '__main__':
    print("gamil_send.py runned\n")
else:
    print("gamil_send.py imported\n")
