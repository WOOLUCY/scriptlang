from audioop import add
from ctypes import addressof
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText # MIMEtexe 생성에 사용
from http.client import HTTPSConnection
from tkinter import *

popup = inputEmail = btnEmail = None
addrEmail = None

def onEmailInput():
    global addrEmail
    addrEmail = inputEmail.get()
    # msg = MIMEText('본문: !너의 지메일은 해킹당하지 않았다!') 
    # msg['Subject'] = '제목: !너의 지메일은 해킹당하지 않았다!'

    # 메일 주소를 저장
    adrs = addrEmail + "\n"
    f = open("mail_list.txt", 'a') 
    f.write(adrs)
    f.close()

    # HTML 전달을 위해 컨테이너 역할을 할 수 있는 "multipart/alternative" 타입사용
    msg = MIMEMultipart('') 
    msg['Subject'] = "Test email for 어디병원" 
    msg['From'] = 'kikanaidek@gmail.com' 
    msg['To'] = addrEmail 

    # 파일로부터 읽어서 MIME 문서를 생성. 
    htmlFD = open("logo.html", 'rb')
    HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8' )
    htmlFD.close()

    # 만든 mime을 MIMEBase에 첨부. 
    msg.attach(HtmlPart)

    # 텍스트 형식의 본문 내용
    data = "안녕하세요 \n 반갑습니다 \n 다시 만나요"
    text = MIMEText(data, 'plain')
    # Data 영역의 메시지에 바운더리 추가
    msg.attach(text)
    # 메시지를 확인한다.
    print(msg)

    # 메일 발송.
    sendMail('kikanaidek@gmail.com', addrEmail, msg)
    popup.destroy() # popup 내리기

def onEmailPopup(): 
    global addrEmail, popup
    addrEmail = None 
    popup = Toplevel() # popup 띄우기
    popup.geometry("300x150")
    popup.title("받을 이메일 주소 입력")

    global inputEmail, btnEmail
    inputEmail = Entry(popup, width = 200)
    inputEmail.pack(fill='x', padx=10, expand=True)

    btnEmail = Button(popup, text="확인", command=onEmailInput)
    btnEmail.pack(anchor="s", padx=10, pady=10)

    # todo: 사용했던 이메일
    mailList = []
    with open('mail_list.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if not line in mailList:
                mailList.append(line)
    f.close()

    ### todo: 수정
    global mListBox
    DeptScrollbar = Scrollbar(popup)
    mailList = Listbox(popup, activestyle='none', relief='ridge', yscrollcommand=DeptScrollbar.set) 

    for i, s in enumerate(mailList): 
        mListBox.insert(i, s)
    mListBox.pack(fill='both', padx=10, expand=True)

    DeptScrollbar.config(command=mListBox.yview) 
    DeptScrollbar.pack(fill='both', padx=10, expand=True)
    ###

    print(mailList)


def sendMail(fromAddr, toAddr, msg):
    import smtplib # 파이썬의 SMTP 모듈
    # 메일 서버와 connect하고 통신 시작
    s = smtplib.SMTP("smtp.gmail.com", 587) # SMTP 서버와 연결
    s.starttls() # SMTP 연결을 TLS (Transport Layer Security) 모드로전환
    
    # 앱 password 이용
    s.login('kikanaidek@gmail.com', 'mktjlisojzwucwro') 
    s.sendmail(fromAddr , [toAddr], msg.as_string()) 
    s.close()


if __name__ == '__main__':
    print("\ngmail.py runned\n")
else:
    print("\ngmail.py imported\n")