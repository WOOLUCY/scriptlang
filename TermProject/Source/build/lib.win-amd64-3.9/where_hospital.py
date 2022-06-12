'''
where_hospital.py
프로그램의 메인모듈

functions
- InitScreen
- setCity
- setDept
- resetFilter
- onSearch
- getStr
- saveMemo
- event_for_listbox
- SearchHospital
'''

# === import ===
from tkinter.tix import NoteBook
from turtle import bgcolor
from urllib.request import urlopen
from server import window
from tkinter import *
from tkinter import font
import tkinter.scrolledtext as st
from tkinter.ttk import Notebook, Style
from xml.etree import ElementTree

from gmail_send import *
import server
from graph import *
from map import *
from telegram import *
from link import *
from book_mark import *

# === functions ===
def InitScreen():       # 메인 GUI 창을 시작하는 함수
    # === frame arrangement ===
    # 분류 제목 레이블 부분
    global CityLabel, NameLabel, DeptLabel
    CityLabel = Label(window, text="시/군", font=server.fontLabel, bg = "white", image=server.labelImage, compound='center')
    DeptLabel = Label(window, text="진료 과목", font=server.fontLabel, bg = "white", image=server.labelImage, compound='center')
    NameLabel = Label(window, text="병원명", font=server.fontLabel, bg = "white", image=server.labelImage, compound='center')

    CityLabel.place(x=10, y=10, width=100, height=70)
    DeptLabel.place(x=10, y=90, width=100, height=70)
    NameLabel.place(x=10, y=170, width=100, height=70)

    # 시(군) 선택 부분
    global CityListBox, clist
    CityScrollbar = Scrollbar(window)
    CityListBox = Listbox(window, activestyle='dotbox',relief='ridge', font=server.fontNormal, yscrollcommand=CityScrollbar.set, cursor="hand2") 
    global selectedCity
    selectedCity = [0]
    CityListBox.bind('<<ListboxSelect>>', setCity)
    clist = server.city_list

    for i, c in enumerate(clist): 
        CityListBox.insert(i, c)

    CityListBox.place(x=110, y=10, width=270, height=70)

    CityScrollbar.config(command=CityListBox.yview, cursor="sb_v_double_arrow") 
    CityScrollbar.place(x=380, y=10, width=20, height=70)

    # 진료 과목 내용 정보
    global DeptListBox, dlist
    DeptScrollbar = Scrollbar(window)
    DeptListBox = Listbox(window, activestyle='dotbox', relief='ridge', font=server.fontNormal, yscrollcommand=DeptScrollbar.set, cursor="hand2") 
    global selectedDept
    selectedDept = [0]
    DeptListBox.bind('<<ListboxSelect>>', setDept)
    dlist = server.dept_list
    for i, s in enumerate(dlist): 
        DeptListBox.insert(i, s)
    DeptListBox.place(x=110, y=90, width=270, height=70) 

    DeptScrollbar.config(command=DeptListBox.yview, cursor="sb_v_double_arrow") 
    DeptScrollbar.place(x=390 - 10, y=90, width=20, height=70)

    # 사용자 입력부분
    global InputLabel
    InputLabel = Entry(window, font=server.fontNormal, width=36, borderwidth=3, relief='ridge', cursor="xterm")
    InputLabel.place(x=110, y=170, width=220, height=70)

    InputButton = Button(window, font=server.fontNormal, image=searchImage, command=onSearch, bg="white",cursor="hand2", overrelief="groove", activebackground= "dark grey")
    InputButton.place(x=110 + 220, y=170, width=70, height=70)

    # 필터 초기화 버튼 부분
    global ResetButton
    ResetButton = Button(window, bg="white", command=resetFilter, font=server.fontNormal, text=getStr(clist[selectedCity[0]]) + "\t\t" + getStr(dlist[selectedDept[0]]), cursor="hand2", overrelief="sunken")
    ResetButton.place(x=410, y=90, width=380, height=70 )

    # 병원 목록 부분
    global listBox
    ListScrollBar = Scrollbar(window)
    listBox = Listbox(window, selectmode='extended', font=server.fontList, width=10, height=15, \
        borderwidth=5, relief='ridge', yscrollcommand=ListScrollBar.set, cursor="hand2")
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.place(x = 10, y = 250, width=380 - 10, height=340)

    ListScrollBar.place(x = 390 - 10, y = 250, width=20, height=340)
    ListScrollBar.config(command=listBox.yview, cursor="sb_v_double_arrow")

    # 로고버튼 부분
    global LogoLabel
    LogoLable = Button(window, image=server.logoImage, bg="white", command=onLogo, relief="flat", activebackground= "dark grey", cursor="hand2", overrelief="groove")
    LogoLable.place(x=410, y=10, width=380, height=70)

    # 그래프버튼 부분
    global GraphButton
    GraphButton = Button(window, bg="white", image=server.graphImage, command=onGraphPopup, activebackground= "dark grey", cursor="hand2", overrelief="sunken")
    GraphButton.place(x=410, y=170, width=72, height=72)
    
    # 메일버튼 부분
    global MailButton
    MailButton = Button(window, image=server.emailImage, bg="white", command=onEmailPopup, activebackground= "dark grey", cursor="hand2", overrelief="sunken")
    MailButton.place(x=410 + 76, y=170, width=72, height=72)

    # 지도버튼 부분
    global MapButton
    MapButton = Button(window, image=server.mapImage, bg="white", command=onMapPopup, activebackground= "dark grey", cursor="hand2", overrelief="sunken")
    MapButton.place(x=410 + 76 * 2, y=170, width=72, height=72)   

    # 북마크버튼 부분
    global MarkButton
    MarkButton = Button(window, image=server.emptymarkImage, bg="white", activebackground= "dark grey", cursor="hand2", overrelief="sunken", command=onMarkPopup)
    MarkButton.place(x=410 + 76 * 3, y=170, width=72, height=72)

    # 텔레그램버튼 부분
    global TelegramButton
    TelegramButton = Button(window, image=server.telegramImage, bg="white", activebackground= "dark grey", cursor="hand2", overrelief="sunken", command=sendSelectedInfo)
    TelegramButton.place(x=410 + 76 * 4, y=170, width=72, height=72)   

    # 정보 부분 (notebook)
    global InfoLabel, ST, notebook
    style = Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="gray")
    style.map("TNotebook", background= [("selected", "gray")])

    notebook = Notebook(window)
    notebook.place(x = 410, y= 250, width=380, height=370 + 48 - 80)

    # notebook page1: 병원 정보 출력
    ST = st.ScrolledText(window, font=server.fontInfo, cursor="arrow")
    notebook.add(ST, text="Info")

    # notebook page2: 링크 모음
    frame2 = Frame(window, background='white', relief='flat', borderwidth=0)
    notebook.add(frame2, text="Link") 
    link1 = Button(frame2, image=server.googleLinkImage, bg='white', relief="flat", command=onGoogleLink, cursor="hand2")
    link2 = Button(frame2, image=server.naverImage, bg='white', relief="flat", command=onNaverLink, cursor="hand2")
    link3 = Button(frame2, image=server.naverMapImage, bg='white', relief="flat", command=onNaverMapLink, cursor="hand2")

    link1.pack(pady=20)
    link2.pack(pady=20)
    link3.pack(pady=20)

    # notebook page3: 메모
    global memoST
    frame3 = Frame(window, background='white', relief='flat', borderwidth=0)
    memoST = st.ScrolledText(frame3, relief='raised', font=server.fontInfo)
    memoST.place(x=0, y=0, width=380, height=288)
    memoButton = Button(frame3, text='북마크 저장', command=saveMemo,font=server.fontInfo, cursor="hand2")
    memoButton.place(x=0, y=288, width=380, height=30)
    notebook.add(frame3, text="BookMark")  

    # bookmark data load
    dirpath = os.getcwd()
    if os.path.isfile(dirpath + '\mark'):            
        f = open('mark', 'rb')
        dic = pickle.load(f) #파일에서 리스트 load
        f.close()
        server.MarkDict = dic

def setCity(event): # command for city list box. 시군 필터
    global selectedCity, CityListBox, clist, ResetButton
    sel = event.widget.curselection()
    if sel:
        selectedCity = sel
        ResetButton.configure(text=getStr(clist[selectedCity[0]]) + "\t\t" + getStr(dlist[selectedDept[0]]))

def setDept(event): # command for dept list box. 진료과목 필터
    global selectedDept, ResetButton
    sel = event.widget.curselection()
    if sel:
        selectedDept = sel
        ResetButton.configure(text=getStr(clist[selectedCity[0]]) + "\t\t" + getStr(dlist[selectedDept[0]]))

def resetFilter():  # command for reset button. 필터 초기화
    global selectedCity, selectedDept, listBox
    selectedCity = [0]
    selectedDept = [0]
    ResetButton.configure(text=getStr(clist[selectedCity[0]]) + "\t\t" + getStr(dlist[selectedDept[0]]))   
    listBox.delete(0, listBox.size())


def onSearch():     # command for search button
    global CityListBox, clist
    global DeptListBox, dlist
    global selectedCity, selectedDept

    cIdx = selectedCity[0]
    dIdx = selectedDept[0]

    SearchHospital(clist[cIdx], dlist[dIdx])

def saveMemo():     # 메모를 저장해 서버로 넘기는 함수
    if server.hospital_name:
        server.memo_text = memoST.get("1.0", END)
        # print (server.memo_text)
        memoST.delete('1.0', END)
        makeBookMark()
    else:
        msgbox.showinfo("알림", "목록에서 병원을 먼저 선택해주십시오.")      

def event_for_listbox(event):   # command for list box
    global InfoLabel, ST
    selection = event.widget.curselection()

    if selection:       # 리스트 박스에서 클릭 발생 시
        index = selection[0]
        data = event.widget.get(index)

        # REST API에서 해당 이름의 정보 검색 후 출력
        key = "8a2e77d6b1a846d1a28fff0ca47f1215"
        url = "https://openapi.gg.go.kr/GgHosptlM?pSize=1000&pIndex=1&KEY=" + key

        res_body = urlopen(url).read()
        strXml = res_body.decode('utf-8')
        tree = ElementTree.fromstring(strXml)

        elements = tree.iter("row")

        info = "null"
        for item in elements:   # 'row' element들
            if item.find('BIZPLC_NM').text == data:
                info = '[병원명]' + '\n' + getStr(item.find('BIZPLC_NM').text) + \
                '\n\n' + '[의료기관종별명]' + '\n' + getStr(item.find('MEDINST_ASORTMT_NM').text) + \
                '\n\n' + '[전화번호]' + '\n' + getStr(item.find('LOCPLC_FACLT_TELNO').text) + \
                '\n\n' + '[도로명 주소]' + '\n' +getStr(item.find('REFINE_ROADNM_ADDR').text)  + \
                '\n\n' + '[지번 주소]' + '\n' +getStr(item.find('REFINE_LOTNO_ADDR').text)  + \
                '\n\n' + '[진료 과목]' + '\n' +getStr(item.find('TREAT_SBJECT_CONT_INFO').text)  + \
                '\n\n' + '[의료인수]' + '\n' +getStr(item.find('MEDSTAF_CNT').text) + \
                '\n\n' + '[입원실수]' + '\n' +getStr(item.find('HOSPTLRM_CNT').text) + \
                '\n\n' + '[병상수]' + '\n' +getStr(item.find('MEDSTAF_CNT').text) 
                server.hospital_name = getStr(item.find('BIZPLC_NM').text)
                
                # 지도를 위해 정보 가져옴
                if item.find('REFINE_WGS84_LAT').text == None and item.find('REFINE_WGS84_LOGT').text == None:
                    server.latitude = 0.0
                    server.longitude = 0.0    
                    MapButton.configure(image=server.noImage)                                    
                else:
                    server.latitude = float(item.find('REFINE_WGS84_LAT').text)
                    server.longitude = float(item.find('REFINE_WGS84_LOGT').text)
                    MapButton.configure(image=server.mapImage)  

        # 북마크 여부 표시        
        if data in server.MarkDict:
            MarkButton.configure(image=server.markImage)
        else:
            MarkButton.configure(image=server.emptymarkImage)

        # 선택된 병원 정보 서버로 넘기기
        server.info_text = info

        # 병원 정보 출력
        ST.configure(state="normal")    # 수정 가능으로 풀어놨다가,
        ST.delete('1.0', END)
        ST.insert(INSERT, info)
        ST.configure(state="disabled")  # 수정 불가능(읽기 전용)으로 변경

def SearchHospital(city = '', dept = ''):       # 리스트 박스 구성을 위해 병원 목록을 만드는 함수
    global listBox
    listBox.delete(0, listBox.size())

    # 1. XML 파일 사용 방식
    # with open('경기도병원현황.xml', 'rb') as f:
    #     strXml = f.read().decode('utf-8')
    # parseData = ElementTree.fromstring(strXml)

    # elements = parseData.iter('row')

    # 2. REST API 사용 방식
    key = "8a2e77d6b1a846d1a28fff0ca47f1215"
    url = "https://openapi.gg.go.kr/GgHosptlM?pSize=1000&pIndex=1&KEY=" + key

    res_body = urlopen(url).read()
    strXml = res_body.decode('utf-8')
    tree = ElementTree.fromstring(strXml)

    elements = tree.iter("row")
    
    i = 1
    for item in elements:   # 'row' element들
        part_el = item.find('BIZPLC_NM')

        if InputLabel.get() not in part_el.text:
            continue
        
        # 시군 O, 과목 O
        if item.find('SIGUN_NM').text == city and dept in getStr(item.find('TREAT_SBJECT_CONT_INFO').text):
            _text = getStr(item.find('BIZPLC_NM').text) 
            
            listBox.insert(i-1, _text)
            i = i + 1

        # 시군 O, 과목 X 
        elif item.find('SIGUN_NM').text == city and dept == "선택안함":
            _text = getStr(item.find('BIZPLC_NM').text) 
            
            listBox.insert(i-1, _text)
            i = i + 1

        # 시군 X, 과목 O
        elif dept in getStr(item.find('TREAT_SBJECT_CONT_INFO').text) and city == "선택안함":
            _text = getStr(item.find('BIZPLC_NM').text) 
            
            listBox.insert(i-1, _text)
            i = i + 1        
        
        elif city == "선택안함" and dept == "선택안함":
            _text = getStr(item.find('BIZPLC_NM').text)
            
            listBox.insert(i-1, _text)
            i = i + 1

def getStr(s):  # utitlity function: 문자열 내용 있을 때만 사용
    return '정보없음' if not s else s

if __name__ == '__main__':
    print("main laucher runned\n")
    InitScreen()
    window.mainloop()
else:
    print("main launcher imported\n")