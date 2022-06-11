from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import server
from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import font

def sendMail(fromAddr, toAddr, msg):
    import smtplib # 파이썬의 SMTP 모듈
    # 메일 서버와 connect하고 통신 시작
    s = smtplib.SMTP("smtp.gmail.com", 587) # SMTP 서버와 연결
    s.starttls() # SMTP 연결을 TLS (Transport Layer Security) 모드로전환
    
    # 앱 password 이용
    s.login('kikanaidek@gmail.com', 'mktjlisojzwucwro') 
    s.sendmail(fromAddr , [toAddr], msg.as_string())
    s.close()

def onEmailInput():
    senderAddr = "kikanaidek@gmail.com"
    addrEmail = inputEmail.get()

    if '@' in addrEmail and addrEmail != '':
        # HTML 전달을 위해 컨테이너 역할을 할 수 있는 "multipart/alternative" 타입사용
        msg = MIMEMultipart('') 
        msg['Subject'] = "어디병원에서 찾으신 병원정보입니다." 
        msg['From'] = 'where the hospital' 
        msg['To'] = addrEmail 

        # 파일로부터 읽어서 MIME 문서를 생성. 
        htmlFD = open("logo.html", 'rb')
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
        except:
            msgbox.showerror("Error", "유효하지 않은 메일주소입니다.")
        
    else:
        response = msgbox.askretrycancel("Error", "유효하지 않은 메일입니다. 다시 시도하시겠습니까?")
        if response == 1: 
            inputEmail.focus_set()
            inputEmail.delete(0, 'end')

def onEmailPopup(): 
    if server.hospital_name == None: 
        msgbox.showinfo("알림", "목록에서 병원을 먼저 선택해주십시오.")
        return

    global addrEmail, popup
    addrEmail = None 
    popup = Toplevel() # popup 띄우기
    popup.geometry("300x100+650+400")
    popup.title("병원 정보 이메일로 보내기")
    popup.resizable(False, False)

    fontNormal = font.Font(popup, size=10, weight='bold', family='G마켓 산스 TTF Light')

    global inputEmail, btnEmail, textLabel, mailListBox, btnSend
    textLabel = Label(popup, text="받을 이메일을 입력하십시오", font=fontNormal)
    textLabel.place(x=5, y=5, width=300, height=30)

    inputEmail = Entry(popup, font=fontNormal)
    inputEmail.place(x=10,y = 35, width = 280, height= 30)

    btnEmail = Button(popup, text="메일 보내기", command=onEmailInput, font=fontNormal, cursor="hand2")
    btnEmail.place(x=10,y = 65, width = 280, height= 30)
