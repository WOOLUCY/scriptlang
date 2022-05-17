# 메일 모듈이다.
import smtplib
# 메일 메시지를 만드 모듈이다. (MIMEBase는 이하 MIMEMultipart, MIMEText, MIMEApplication, MIMEImage, MIMEAudio)의 상위 모듈이다.
# 굳이 선언할 필요없다.
#from email.mime.base import MIMEBase;
# 메일의 Data 영역의 메시지를 만드는 모듈 (MIMEText, MIMEApplication, MIMEImage, MIMEAudio가 attach되면 바운더리 형식으로 변환)
from email.mime.multipart import MIMEMultipart
# 메일의 본문 내용을 만드는 모듈
from email.mime.text import MIMEText
# 메일의 첨부 파일을 base64 형식으로 변환
from email.mime.application import MIMEApplication
# 메일의 이미지 파일을 base64 형식으로 변환(Content-ID 생성)
from email.mime.image import MIMEImage
# 메일의 음악 파일을 base64 형식으로 변환(Content-ID 생성)
from email.mime.audio import MIMEAudio
# 파일 IO
import io

# 메일 서버와 통신하기 전에 메시지를 만든다.
data = MIMEMultipart()
# 송신자 설정
data['From'] = "kikanaidek@gmail.com"
# 수신자 설정 (복수는 콤마 구분이다.)
data['To'] = "kikanaidek@gmail.com"
# 참조 수신자 설정
data['Cc'] = "kikanaidek@gmail.com"
# 숨은 참조 수신자 설정
data['Bcc'] = "kikanaidek@gmail.com"
# 메일 제목
data['Subject'] = "Test Mail"

# # 첨부 파일 추가
# with open("test.xlsx", "rb") as fp:
#     # Name은 메일 수신자에서 설정되는 파일 이름
#     part = MIMEApplication(fp.read(), Name = "test.xlsx")
#     # Data 영역의 메시지에 바운더리 추가
#     data.attach(part)

# 이미지 파일 추가
with open("logo.png", 'rb') as fp:
    # Name은 메일 수신자에서 설정되는 파일 이름
    img = MIMEImage(fp.read(), Name = "logo.png")
    # 해더에 Content-ID 추가(본문 내용에서 cid로 링크를 걸 수 있다.)
    img.add_header('Content-ID', '<capture>')
    # Data 영역의 메시지에 바운더리 추가
    data.attach(img)

# 텍스트 형식의 본문 내용
#msg = MIMEText("Hello world", 'plain');
# Html 형식의 본문 내용 (cid로 이미 첨부 파일을 링크했다.)
msg = MIMEText("Hello Test<br /><img src='cid:capture'>", 'html')
# Data 영역의 메시지에 바운더리 추가
data.attach(msg)
# 메시지를 확인한다.
print(data)

# 메일 서버와 telnet 통신 개시
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
#server = smtplib.SMTP('smtp.gmail.com',587);
# 메일 통신시 디버그
server.set_debuglevel(1)
# 헤로 한번 해주자.(의미 없음)
server.ehlo()
# tls 설정 주문 - tls 587 포트의 경우
#server.starttls();
# 헤로 또 해주자.(의미 없음)
server.ehlo()
# 로그인 한다.
server.login("kikanaidek@gmail.com", "mktjlisojzwucwro")
# 심심하니 또 헤로 해주자.(의미 없음)
server.ehlo()

# MAIL(송신자) 설정
sender = data['From']
# RCPT(수신자), 리스트로 보낸다.
# 수신자 추가
receiver = data['To'].split(",")
# 참조자 추가
if data['Cc'] is not None:
    receiver += data['Cc'].split(",")
# 숨은 참조자 추가
if data['Bcc'] is not None:
    receiver += data['Bcc'].split(",")

# 메일 프로토콜 상 MAIL, RCPT, DATA 순으로 메시지를 보내야 하는데 이걸 sendmail함수에서 자동으로 해준다.
server.sendmail(sender, receiver, data.as_string())
# QUIT을 보내고 접속을 종료하고 메일을 보낸다.
server.quit()
