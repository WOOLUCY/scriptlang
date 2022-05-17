from audioop import add
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText # MIMEtexe 생성에 사용
from http.client import HTTPSConnection
from where_hospital import *
from tkinter import *

popup = inputEmail = btnEmail = None
addrEmail = None

def onEmailInput():
    global addrEmail
    addrEmail = inputEmail.get()
    popup.destroy() # popup 내리기

def onEmailPopup(): 
    global window, addrEmail, popup
    addrEmail = None 
    popup = Toplevel(window) # popup 띄우기
    popup.geometry("300x150")
    popup.title("받을 이메일 주소 입력")

    global inputEmail, btnEmail
    inputEmail = Entry(popup, width = 200,)
    inputEmail.pack(fill='x', padx=10, expand=True)

    btnEmail = Button(popup, text="확인", command=onEmailInput)
    btnEmail.pack(anchor="s", padx=10, pady=10)


def sendMail(fromAddr, toAddr, msg):
    import smtplib # 파이썬의 SMTP 모듈
    # 메일 서버와 connect하고 통신 시작
    s = smtplib.SMTP("smtp.gmail.com", 587) # SMTP 서버와 연결
    s.starttls() # SMTP 연결을 TLS (Transport Layer Security) 모드로전환
    
    # 앱 password 이용
    s.login('kikanaidek@gmail.com', 'mktjlisojzwucwro') 
    s.sendmail(fromAddr , [toAddr], msg.as_string()) 
    s.close()

