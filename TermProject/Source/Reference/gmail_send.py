from email.mime.text import MIMEText # MIMEtexe 생성에 사용

def sendMail(fromAddr, toAddr, msg):
    import smtplib # 파이썬의 SMTP 모듈
    # 메일 서버와 connect하고 통신 시작
    s = smtplib.SMTP("smtp.gmail.com", 587) # SMTP 서버와 연결
    s.starttls() # SMTP 연결을 TLS (Transport Layer Security) 모드로전환
    
    # 앱 password 이용
    s.login('kikanaidek@gmail.com', 'mktjlisojzwucwro') 
    s.sendmail(fromAddr , [toAddr], msg.as_string()) 
    s.close()

msg = MIMEText('본문: !너의 지메일은 해킹당했다!') 
msg['Subject'] = '제목: !너의 지메일은 해킹당했다!' 
sendMail('kikanaidek@gmail.com', 'chayeon1789@gmail.com', msg)