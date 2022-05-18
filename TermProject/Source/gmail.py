from audioop import add
from ctypes import addressof
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText # MIMEtexe 생성에 사용
from http.client import HTTPSConnection
from mimetypes import MimeTypes
from tkinter import *
import server

popup = inputEmail = btnEmail = None
addrEmail = None

# todo: 복수의 수신자 설정 

def onEmailInput():
    global addrEmail, info_text
    addrEmail = inputEmail.get()
    # msg = MIMEText('본문: !너의 지메일은 해킹당하지 않았다!') 
    # msg['Subject'] = '제목: !너의 지메일은 해킹당하지 않았다!'

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
    # text = MIMEText(data, 'plain')
    text = MIMEText(server.info_text, _charset = 'UTF-8')
    # Data 영역의 메시지에 바운더리 추가
    msg.attach(text)
    # 메시지를 확인한다.
    # print(msg)

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


def sendMail(fromAddr, toAddr, msg):
    import smtplib # 파이썬의 SMTP 모듈
    # 메일 서버와 connect하고 통신 시작
    s = smtplib.SMTP("smtp.gmail.com", 587) # SMTP 서버와 연결
    s.starttls() # SMTP 연결을 TLS (Transport Layer Security) 모드로전환
    
    # 앱 password 이용
    s.login('kikanaidek@gmail.com', 'mktjlisojzwucwro') 
    s.sendmail(fromAddr , [toAddr], msg.as_string()) 
    s.close()

# todo: 크롤링
def getSearchResult(keyword):
    from urllib.parse import quote_plus 
    from bs4 import BeautifulSoup 
    from selenium import webdriver
    
    search = input("검색어를 입력하세요 : ") 
    url = 'https://www.google.com/search?q=' 
    newUrl = url + quote_plus(search) 

    driver = webdriver.Chrome() 
    driver.get(newUrl) 

    html = driver.page_source #열린 페이지 소스 받음 
    soup = BeautifulSoup(html) 

    r = soup.select('.r') #클래스 r을 선택 select 로 가져오면 list 형식임 

    for i in r : 
        print(i.select_one('.LC20lb.DKV0Md').text) 
        #select 를 안쓰는 이유는 select 를 쓰면 list 로 불러와져서 text 를쓸 수 없다 
        print(i.a.attrs['href']) #a 태그의 href 속성 가져오기 
        print()



def getStr(s):
    return '정보없음' if not s else s

if __name__ == '__main__':
    getSearchResult("유재석")
else:
    print("\ngmail.py imported\n")