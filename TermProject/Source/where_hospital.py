from msilib.schema import ListBox
from tkinter import *
from tkinter import font

window = Tk()
window.title("어디 병원")
window.geometry("800x600+450+200")
window.resizable(False, False)
window.configure(bg='white')

searchImage = PhotoImage(file='image/search.png')  # search image
emailImage = PhotoImage(file='image/mail.png')     # gmail image
mapImage = PhotoImage(file='image/map.png')        # naver map image
logoImage = PhotoImage(file='image/logo.png')      # logo image

def InitScreen():
    fontNormal = font.Font(window, size=15, weight='bold', family='나눔바른고딕')

    # 시(군) 선택 부분
    global CityListBox
    CityScrollbar = Scrollbar(window)
    CityListBox = Listbox(window, activestyle='none',relief='ridge', font=fontNormal, yscrollcommand=CityScrollbar.set) 
    slist = ["안양시", "시흥시", "성남시", "광명시"]        # todo: add list
    for i, s in enumerate(slist): 
        CityListBox.insert(i, s)
    CityListBox.place(x=110, y=10, width=280, height=70)

    CityScrollbar.config(command=CityListBox.yview) 
    CityScrollbar.place(x=390, y=10, width=20, height=70)

    # 진료 과목 내용 정보
    global DeptListBox
    DeptScrollbar = Scrollbar(window)
    DeptListBox = Listbox(window, activestyle='none', relief='ridge', font=fontNormal, yscrollcommand=DeptScrollbar.set) 
    slist = ["치과", "내과", "피부과", "정형외과"]          # todo: add list
    for i, s in enumerate(slist): 
        DeptListBox.insert(i, s)
    DeptListBox.place(x=110, y=90, width=280, height=70) 

    DeptScrollbar.config(command=DeptListBox.yview) 
    DeptScrollbar.place(x=390, y=90, width=20, height=70)

    # 사용자 입력부분
    global InputLabel
    InputLabel = Entry(window, font=fontNormal, width=36, borderwidth=12, relief='groove')
    InputLabel.place(x=110, y=170, width=230, height=70)

    InputButton = Button(window, font=fontNormal, text='검색', command=onSearch)
    InputButton.place(x=110 + 230, y=170, width=50, height=70)

    # 목록 부분
    global listBox
    ListScrollBar = Scrollbar(window)
    listBox = Listbox(window, selectmode='extended', font=fontNormal, width=10, height=15, \
        borderwidth=12, relief='ridge', yscrollcommand=ListScrollBar.set)
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.place(x = 10, y = 250, width=380, height=340)

    ListScrollBar.place(x = 390, y = 250, width=20, height=340)
    ListScrollBar.config(command=listBox.yview)

    # 분류 제목 부분
    global CityLabel, TypeLabel, DeptLabel
    CityLabel = Label(window, text="시(군) 선택", font=fontNormal, bg="#bebebe")
    DeptLabel = Label(window, text="진료 과목", font=fontNormal, bg="#bebebe")
    SearchLabel = Label(window, text="검색명", font=fontNormal, bg="#bebebe")

    CityLabel.place(x=10, y=10, width=100, height=70)
    DeptLabel.place(x=10, y=90, width=100, height=70)
    SearchLabel.place(x=10, y=170, width=100, height=70)

    # 로고 부분
    global LogoLabel
    LogoLable = Label(window, image=logoImage, bg="white")
    LogoLable.place(x=410, y=10, width=380, height=70)

    # 검색 부분
    global SearchButton
    SearchButton = Button(window, image=searchImage, bg="white")
    SearchButton.place(x=410, y=90, width=120, height=120)
    
    # 메일 부분
    global MailButton
    MailButton = Button(window, image=emailImage, bg="white")
    MailButton.place(x=540, y=90, width=120, height=120)

    # 지도 부분
    global MapButton
    MapButton = Button(window, image=mapImage, bg="white")
    MapButton.place(x=670, y=90, width=120, height=120)   

    # 정보 부분
    global InfoLabel
    TempText = "해당병원 정보출력\nex) 위치, 입원, 실수, 전화번호"
    InfoLabel = Label(text = TempText, font=fontNormal, bg="#bebebe")
    InfoLabel.place(x = 410, y= 220, width=380, height=370)

# todo command 함수 추가
def event_for_listbox(event):
    global InfoLabel
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(data)
        InfoLabel.configure(text=data)

def onSearch():     # '검색' 버튼 이벤트 처리
    global CityListBox

    sels = CityListBox.curselection()
    iSearchIndex = 0 if len(sels) == 0 else CityListBox.curselection()[0]
    if iSearchIndex == 0:
        SearchHospital()
    elif iSearchIndex == 1:
        pass
    elif iSearchIndex == 2:
        pass
    elif iSearchIndex == 3:
        pass

# 유틸리티 함수: 문자열 내용 있을 때만 사용
def getStr(s):
    return ''if not s else s

def SearchHospital(city = ''):    # '검색' 버튼 -> '병원'
    from xml.etree import ElementTree

    global listBox
    listBox.delete(0, listBox.size())

    with open('경기도병원현황.xml', 'rb') as f:
        strXml = f.read().decode('utf-8')
    parseData = ElementTree.fromstring(strXml)

    elements = parseData.iter('row')

    i = 1
    for item in elements:   # 'row' element들
        part_el = item.find('SIGUN_NM')
        
        if InputLabel.get() not in part_el.text:
            continue
        
        if item.find('BSN_STATE_NM').text != "폐업":
            _text = '[' + str(i) + ']' + \
            getStr(item.find('BIZPLC_NM').text) + \
            ' : ' + getStr(item.find('SIGUN_NM').text)   
            
            listBox.insert(i-1, _text)
            i = i + 1

InitScreen()
window.mainloop()