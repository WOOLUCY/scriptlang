from xmlbook import *
from http.client import HTTPSConnection

conn = None
server = "openapi.naver.com" # 네이버 OpenAPI 서버

def connectOpenAPIServer(): 
    global conn, server 
    conn = HTTPSConnection(server) 
    conn.set_debuglevel(1)

def userURIBuilder(uri, **user): 
    str = uri + "?"
    for key in user.keys(): 
        str += key + "=" + user[key] + "&"
    return str

def getBookDataFromISBN(isbn): 
    global server, conn
    client_id = "3fupGESFqNJ87bqJLdbw" 
    client_secret = "yDxJ19vg1J"
    if conn == None : 
        connectOpenAPIServer() # OpenAPI 접속
    #네어버에서 ISBN에 의한 도서정보 가져올 URL 생성
    uri = userURIBuilder("/v1/search/book_adv.xml", display="1", start="1", d_isbn=isbn)
    conn.request("GET", uri, None, #GET 요청
        {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})

    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200 : 
        print("Book data downloading complete!")
        return extractBookData(req.read()) #요청이 성공이면 book 정보추출
    else: 
        print ("OpenAPI request has been failed!! please retry")
        return None

def extractBookData(strXml): #strXml은 OpenAPI 검색 결과 XML 문자열
    from xml.dom.minidom import parseString
    from xml.etree import ElementTree

    tree = ElementTree.fromstring(strXml)

    print (parseString(strXml.decode('utf-8')).toprettyxml()) # 내용확인용
    
    # "item" 하위의 "title" 찾기. 
    # # Note! 그냥 "title"은 찾으면 상단의 "title"도 검색되므로. 
    itemElements = tree.iter("item")    # item 엘리먼트 리스트추출
    for item in itemElements:
        isbn = item.find("isbn")      #isbn 검색
        title = item.find("title")    #title 검색
        if len(title.text) > 0 :        
            # AddBook()에 줄 수 있는 사전형식 반환
            return {"ISBN":isbn.text,"title":title.text}

def sendMail(fromAddr, toAddr, msg):
    import smtplib # 파이썬의 SMTP 모듈
    # 메일 서버와 connect하고 통신 시작
    s = smtplib.SMTP("smtp.gmail.com", 587) # SMTP 서버와 연결
    s.starttls() # SMTP 연결을 TLS (Transport Layer Security) 모드로전환
    
    # 앱 password 이용
    s.login('kikanaidek@gmail.com', 'mktjlisojzwucwro') 
    s.sendmail(fromAddr , [toAddr], msg.as_string())
    s.close()

def sendBookMail(): 
    html = "" 
    
    # 사용자 입력 받기
    title = input ('Title :') 
    senderAddr = input ('sender email address :') 
    recipientAddr = input ('recipient email address :') 
    msgtext = input ('write message :')
    passwd = input ('input your app password :') 
    msgtext = input ('Do you want to include book data (y/n):')
    if msgtext == 'y' : 
        keyword = input ('input keyword to search:')
        html = MakeHtmlDoc(SearchBookTitle(keyword))
    
    from email.mime.multipart import MIMEMultipart #MIMEMultipart MIME생성
    from email.mime.text import MIMEText

    # HTML 전달을 위해 컨테이너 역할을 할 수 있는 "multipart/alternative" 타입사용
    msg = MIMEMultipart('alternative') 

    msg['Subject'] = title #set message 
    msg['From'] = senderAddr 
    msg['To'] = recipientAddr 
    
    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset = 'UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부 
    msg.attach(msgPart) 
    msg.attach(bookPart)
    
    print ("connect smtp server ... ") 
    sendMail(senderAddr, recipientAddr, msg) # send mail
    print ("Mail sending complete!!!")