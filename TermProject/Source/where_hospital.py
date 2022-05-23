from ctypes import addressof
from msilib.schema import ListBox
from tkinter import *
from tkinter import font
import tkinter.scrolledtext as st
from mail_send import *
import server

window = Tk()
window.title("Where the Hospital")
window.geometry("800x600+450+200")
window.resizable(False, False)
window.configure(bg='white')

searchImage = PhotoImage(file='image/search.png')  # search image
emailImage = PhotoImage(file='image/mail.png')     # gmail image
mapImage = PhotoImage(file='image/map.png')        # naver map image
logoImage = PhotoImage(file='image/logo.gif')      # logo image

def InitScreen():
    fontNormal = font.Font(window, size=15, weight='bold', family='굴림')
    fontInfo = font.Font(window, size=9, weight='bold', family='굴림')

    # 시(군) 선택 부분
    global CityListBox, clist
    CityScrollbar = Scrollbar(window)
    CityListBox = Listbox(window, activestyle='dotbox',relief='ridge', font=fontNormal, yscrollcommand=CityScrollbar.set) 
    global selectedCity
    selectedCity = [0]
    CityListBox.bind('<<ListboxSelect>>', setCity)
    clist = server.city_list

    for i, c in enumerate(clist): 
        CityListBox.insert(i, c)

    CityListBox.place(x=110, y=10, width=280, height=70)

    CityScrollbar.config(command=CityListBox.yview) 
    CityScrollbar.place(x=390, y=10, width=20, height=70)

    # 진료 과목 내용 정보
    global DeptListBox, dlist
    DeptScrollbar = Scrollbar(window)
    DeptListBox = Listbox(window, activestyle='dotbox', relief='ridge', font=fontNormal, yscrollcommand=DeptScrollbar.set) 
    global selectedDept
    selectedDept = [0]
    DeptListBox.bind('<<ListboxSelect>>', setDept)
    dlist = server.dept_list
    for i, s in enumerate(dlist): 
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

    # 선택된 필터 레이블 부분
    global filterLabel
    filterLabel = Label(window, bg="white", text=getStr(clist[selectedCity[0]]) + "\n" + getStr(dlist[selectedDept[0]]))
    filterLabel.place(x=410, y=90, width=120, height=120)
    
    # 메일 부분
    global MailButton
    MailButton = Button(window, image=emailImage, bg="white", command=onEmailPopup)
    MailButton.place(x=540, y=90, width=120, height=120)

    # 지도 부분
    global MapButton
    MapButton = Button(window, image=mapImage, bg="white")
    MapButton.place(x=670, y=90, width=120, height=120)   

    # 정보 부분
    global InfoLabel, ST
    # TempText = "해당병원 정보출력\nex) 위치, 입원, 실수, 전화번호"
    # InfoLabel = Label(text = TempText, font=fontInfo, bg="#bebebe", justify="left")
    # InfoLabel.place(x = 410, y= 220, width=380, height=370)

    ST = st.ScrolledText(window)
    ST.place(x = 410, y= 220, width=380, height=370)

def setCity(event):
    global selectedCity, CityListBox, clist, filterLabel
    sel = event.widget.curselection()
    if sel:
        selectedCity = sel
        print(selectedCity[0])
        filterLabel.configure(text=getStr(clist[selectedCity[0]]) + "\n" + getStr(dlist[selectedDept[0]]))


def setDept(event):
    global selectedDept, filterLabel
    sel = event.widget.curselection()
    if sel:
        selectedDept = sel
        filterLabel.configure(text=getStr(clist[selectedCity[0]]) + "\n" + getStr(dlist[selectedDept[0]]))
        print(selectedDept[0])    


def event_for_listbox(event):
    global InfoLabel, ST
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        # print(data)

        # 클릭 시, 정보 출력
        from xml.etree import ElementTree
        with open('경기도병원현황.xml', 'rb') as f:
            strXml = f.read().decode('utf-8')
        parseData = ElementTree.fromstring(strXml)

        elements = parseData.iter('row')

        info = "null"
        for item in elements:   # 'row' element들
            if item.find('BIZPLC_NM').text == data:
                info = '[병원명]' + '\n' + getStr(item.find('BIZPLC_NM').text) + \
                '\n\n' + '[의료기관종별명]' + '\n' + getStr(item.find('MEDINST_ASORTMT_NM').text) + \
                '\n\n' + '[전화번호]' + '\n' + getStr(item.find('LOCPLC_FACLT_TELNO_DTLS').text) + \
                '\n\n' + '[도로명 주소]' + '\n' +getStr(item.find('REFINE_ROADNM_ADDR').text)  + \
                '\n\n' + '[지번 주소]' + '\n' +getStr(item.find('REFINE_LOTNO_ADDR').text)  + \
                '\n\n' + '[진료 과목]' + '\n' +getStr(item.find('TREAT_SBJECT_CONT_INFO').text)  + \
                '\n\n' + '[의료인수]' + '\n' +getStr(item.find('MEDSTAF_CNT').text) + \
                '\n\n' + '[입원실수]' + '\n' +getStr(item.find('HOSPTLRM_CNT').text) + \
                '\n\n' + '[병상수]' + '\n' +getStr(item.find('MEDSTAF_CNT').text) + \
                '\n\n' + '[검색결과]' + '\n' +'https://www.google.com/search?q=' + getStr(item.find('BIZPLC_NM').text)    
                server.hospital_name = getStr(item.find('BIZPLC_NM').text)    
        server.info_text = info

        # InfoLabel.configure(text=info)
        ST.configure(state="normal")    # 수정 가능으로 풀어놨다가,
        ST.delete('1.0', END)
        ST.insert(INSERT, info)
        ST.configure(state="disabled")  # 수정 불가능(읽기 전용)으로 변경

def onSearch():     # '검색' 버튼 이벤트 처리
    global CityListBox, clist
    global DeptListBox, dlist
    global selectedCity, selectedDept

    cIdx = selectedCity[0]
    dIdx = selectedDept[0]

    # selC = CityListBox.curselection()
    # cSearchIndex = 0 if len(selC) == 0 else CityListBox.curselection()[0]
    
    # selD = DeptListBox.curselection()
    # dSearchIndex = 0 if len(selD) == 0 else DeptListBox.curselection()[0]

    SearchHospital(clist[cIdx], dlist[dIdx])
    # print(cSearchIndex, dSearchIndex)
    


# 유틸리티 함수: 문자열 내용 있을 때만 사용
def getStr(s):
    return '정보없음' if not s else s

def SearchHospital(city = '', dept = ''):    # '검색' 버튼 -> '병원'
    from xml.etree import ElementTree

    global listBox
    listBox.delete(0, listBox.size())

    with open('경기도병원현황.xml', 'rb') as f:
        strXml = f.read().decode('utf-8')
    parseData = ElementTree.fromstring(strXml)

    elements = parseData.iter('row')

    i = 1
    for item in elements:   # 'row' element들
        part_el = item.find('BIZPLC_NM')
        
        if InputLabel.get() not in part_el.text:
            continue

        if item.find('BSN_STATE_NM').text != "폐업" and item.find('SIGUN_NM').text == city:
            _text = getStr(item.find('BIZPLC_NM').text)
            
            listBox.insert(i-1, _text)
            i = i + 1
        
        elif item.find('BSN_STATE_NM').text != "폐업" and city == "선택안함":
            _text = getStr(item.find('BIZPLC_NM').text)
            
            listBox.insert(i-1, _text)
            i = i + 1

InitScreen()
window.mainloop()
