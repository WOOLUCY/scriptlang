from msilib.schema import ListBox
from tkinter import *
from tkinter import font

window = Tk()
window.title("어디 병원")
window.geometry("800x600+450+200")
window.resizable(False, False)


emailImage = PhotoImage(file='image/email.png')     # gmail image
mapImage = PhotoImage(file='image/map2.png')        # naver map image
logoImage = PhotoImage(file='image/logo.png')       # logo image

def InitScreen():
    fontNormal = font.Font(window, size=15, weight='bold')

    # 시(군) 선택 부분
    global CityListBox
    CityListBox = Listbox(window, activestyle='none',relief='ridge', font=fontNormal) 
    slist = ["안양시", "시흥시", "성남시", "광명시"]
    for i, s in enumerate(slist): 
        CityListBox.insert(i, s)
    CityListBox.place(x=110, y=10, width=280, height=70)

    # 병원종류
    global TypeListBox
    TypeListBox = Listbox(window, activestyle='none', relief='ridge', font=fontNormal)
    slist = ["한방병원", "종합병원", "요양병원"]
    for i, s in enumerate(slist): 
        TypeListBox.insert(i, s)
    TypeListBox.place(x=110, y=90, width=280, height=70)

    # 진료 과목 내용 정보
    global DeptListBox
    DeptListBox = Listbox(window, activestyle='none', relief='ridge', font=fontNormal) 
    slist = ["치과", "내과", "피부과", "정형외과"]
    for i, s in enumerate(slist): 
        DeptListBox.insert(i, s)
    DeptListBox.place(x=110, y=170, width=280, height=70) 

    # 목록 부분
    global listBox
    listBox = Listbox(window, selectmode='extended', font=fontNormal, width=10, height=15, \
        borderwidth=12, relief='ridge')
    listBox.place(x = 10, y = 250, width=380, height=340)

    # 분류 제목 부분
    global CityLabel, TypeLabel, DeptLabel
    CityLabel = Label(window, text="시(군) 선택", font=fontNormal)
    TypeLabel = Label(window, text="병원 종류", font=fontNormal)
    DeptLabel = Label(window, text="진료 과목", font=fontNormal)

    CityLabel.place(x=10, y=10, width=100, height=70)
    TypeLabel.place(x=10, y=90, width=100, height=70)
    DeptLabel.place(x=10, y=170, width=100, height=70)


    # 로고 부분
    global LogoLabel
    LogoLable = Label(window, image=logoImage)
    LogoLable.place(x=410, y=10, width=380, height=70)

    # 메일 부분
    global MailButton
    MailButton = Button(window, image=emailImage)
    MailButton.place(x=430, y=90, width=150, height=150)

    # 지도 부분
    global MapButton
    MapButton = Button(window, image=mapImage)
    MapButton.place(x=620, y=90, width=150, height=150)   

    # 정보 부분
    global InfoLabel
    InfoLabel = Label(text = "정보", font=fontNormal, bg="cyan")
    InfoLabel.place(x = 410, y= 250, width=380, height=340)

InitScreen()
window.mainloop()