# from audioop import add
# from ctypes import addressof
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText # MIMEtexe 생성에 사용
# from http.client import HTTPSConnection
# from mimetypes import MimeTypes
from tkinter import *
import server
from tkinter import font
import tkinter.scrolledtext as st
import tkinter.messagebox as msgbox
import tkintermapview

popup = inputEmail = btnEmail = None
addrEmail = None
mailNum = 0

# todo: 복수의 수신자 설정 
def onEmailInput():
    global addrEmail, info_text
    # addrEmail = inputEmail.get()
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
    try:
        sendMail('kikanaidek@gmail.com', addrEmail, msg)
        msgbox.showinfo("알림", "정상적으로 메일을 보냈습니다.")
        # onEmailPopup()
        # popup.destroy() # popup 내리기
    except:
        msgbox.showerror("Error", "유효하지 않은 메일주소입니다.")

def event_for_add():
    global mailNum, mailListBox
    str = inputEmail.get()

    with open('mail_list.txt', 'a') as f:
        if str != '' and not (str in server.mail_list):
            if '@' in str:
                f.write(str + '\n')
                inputEmail.delete(0, END)
                mailListBox.insert(mailNum, str)
                mailNum += 1
                server.mail_list.insert(mailNum, str)
            else:
                response = msgbox.askretrycancel("Error", "유효하지 않은 메일입니다. 다시 시도하시겠습니까?")
                if response == 1: 
                    onEmailPopup()
                elif response == 0: 
                    pass
        elif str in server.mail_list:
            response = msgbox.askretrycancel("Error", "이미 리스트에 있는 메일입니다. 다시 시도하시겠습니까?")
            if response == 1: 
                popup.destroy() # popup 내리기
                onEmailPopup()
            elif response == 0: 
                popup.destroy() # popup 내리기
            

def onEmailPopup(): 
    global addrEmail, popup
    addrEmail = None 
    popup = Toplevel() # popup 띄우기
    popup.geometry("300x240+650+400")
    popup.title("받을 이메일 주소 입력")
    popup.resizable(False, False)

    fontNormal = font.Font(popup, size=10, weight='bold', family='나눔바른고딕')

    global inputEmail, btnEmail, textLabel, mailListBox, btnSend
    textLabel = Label(popup, text="받을 이메일을 입력하세요", font=fontNormal)
    textLabel.place(x=5, y=5, width=300, height=30)

    inputEmail = Entry(popup, font=fontNormal)
    inputEmail.place(x=10,y = 35, width = 250, height= 30)

    btnEmail = Button(popup, text="추가", font=fontNormal, command=event_for_add)
    btnEmail.place(x=260,y = 35, width = 30, height= 30)

    mailListBox = Listbox(popup, selectmode='extended', font=fontNormal, width=10, height=15, \
        borderwidth=1, relief='ridge')
    mailListBox.bind('<<ListboxSelect>>', event_for_mailListbox)

    global mailNum
    with open('mail_list.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            mailListBox.insert(mailNum, line)
            mailNum += 1
            server.mail_list.insert(mailNum, line)
    
    print (server.mail_list)

    mailListBox.place(x=10, y=70, width=280, height=120)

    btnEmail = Button(popup, text="메일 보내기", command=onEmailInput, font=fontNormal)
    btnEmail.place(x=10,y = 195, width = 280, height= 30)


    # inputEmail = Entry(popup, width = 200, font=fontNormal)
    # inputEmail.pack(fill='x', padx=10, expand=True)

    # btnEmail = Button(popup, text="확인", command=onEmailInput, font=fontNormal)
    # btnEmail.pack(anchor="s", padx=10, pady=10)


def sendMail(fromAddr, toAddr, msg):
    import smtplib # 파이썬의 SMTP 모듈
    # 메일 서버와 connect하고 통신 시작
    s = smtplib.SMTP("smtp.gmail.com", 587) # SMTP 서버와 연결
    s.starttls() # SMTP 연결을 TLS (Transport Layer Security) 모드로전환
    
    # 앱 password 이용
    s.login('kikanaidek@gmail.com', 'mktjlisojzwucwro') 
    s.sendmail(fromAddr , [toAddr], msg.as_string()) 
    s.close()

def event_for_mailListbox(event):
    global addrEmail

    selection = event.widget.curselection()
    if selection:
        addrEmail = server.mail_list[selection[0]]

def getStr(s):
    return '정보없음' if not s else s

def onMapPopup():
    popup = Toplevel()
    popup.geometry("800x600+100+100")
    popup.title("<" + server.hospital_name + "> 의 지도")

    # root = Tk()
    # root.geometry(f"{800}x{600}")
    # root.title("map_view_example.py")

    if server.latitude == 0 and server.longitude == 0:
        emptyLabel = Label(popup, width=800, height=600, text="해당 병원의 지도 정보가 없습니다.")
        emptyLabel.pack()

    else:
        map_widget = tkintermapview.TkinterMapView(popup, width=800, height=600, corner_radius=0) 
        map_widget.pack()

        marker_1 = map_widget.set_position(server.latitude, server.longitude, marker=True) # 위도,경도 위치지정
        # 주소 위치지정 
        # marker_1 = map_widget.set_address("경기도 시흥시 산기대학로 237", marker=True)
        print(marker_1.position, marker_1.text) # get position and text 
        marker_1.set_text(server.hospital_name) # set new text 
        map_widget.set_zoom(15) # 0~19 (19 is the highest zoom level) 

if __name__ == '__main__':
    onEmailPopup()
    onMapPopup()
    print("\npop_up.py runned\n")
else:
    print("\npop_up.py imported\n")