# from ctypes import addressof
# from msilib.schema import ListBox
from cProfile import label
import webbrowser
from tkinter import *
from tkinter import font
import tkinter.scrolledtext as st
from mail import *
import server
from graph import *
from map import *
from server import window

# window = Tk()
# window.title("Where the Hospital")
# window.geometry("800x600+450+200")
# window.resizable(False, False)
# window.configure(bg='white')

searchImage = PhotoImage(file='image/search.png')       # search image
filterImage = PhotoImage(file='image/filter_icon.png')      # filter image
emailImage = PhotoImage(file='image/mail_icon3.png')        # mail image
mapImage = PhotoImage(file='image/map_icon2.png')           # map image
linkImage = PhotoImage(file='image/link.png')               # link image
telegramImage = PhotoImage(file='image/telegram_icon.png')  # link image
logoImage = PhotoImage(file='image/logo.gif')               # logo image
graphImage = PhotoImage(file='image/trend.png')             # graph image
noImage = PhotoImage(file='image/close.png')                # no image
labelImage = PhotoImage(file='image/label.png')             # no image

def InitScreen():
    fontNormal = font.Font(window, size=14, family='G마켓 산스 TTF Medium')
    fontLabel= font.Font(window, size=14, family='G마켓 산스 TTF Bold')
    fontInfo = font.Font(window, size=10, family='G마켓 산스 TTF Medium')
    fontList = font.Font(window, size=14, family='G마켓 산스 TTF Medium')   

    # 시(군) 선택 부분
    global CityListBox, clist
    CityScrollbar = Scrollbar(window)
    CityListBox = Listbox(window, activestyle='dotbox',relief='ridge', font=fontNormal, yscrollcommand=CityScrollbar.set, cursor="hand2") 
    global selectedCity
    selectedCity = [0]
    CityListBox.bind('<<ListboxSelect>>', setCity)
    clist = server.city_list

    for i, c in enumerate(clist): 
        CityListBox.insert(i, c)

    CityListBox.place(x=110, y=10, width=280 - 10, height=70)

    CityScrollbar.config(command=CityListBox.yview, cursor="sb_v_double_arrow") 
    CityScrollbar.place(x=390 - 10, y=10, width=20, height=70)

    # 진료 과목 내용 정보
    global DeptListBox, dlist
    DeptScrollbar = Scrollbar(window)
    DeptListBox = Listbox(window, activestyle='dotbox', relief='ridge', font=fontNormal, yscrollcommand=DeptScrollbar.set, cursor="hand2") 
    global selectedDept
    selectedDept = [0]
    DeptListBox.bind('<<ListboxSelect>>', setDept)
    dlist = server.dept_list
    for i, s in enumerate(dlist): 
        DeptListBox.insert(i, s)
    DeptListBox.place(x=110, y=90, width=280 - 10, height=70) 

    DeptScrollbar.config(command=DeptListBox.yview, cursor="sb_v_double_arrow") 
    DeptScrollbar.place(x=390 - 10, y=90, width=20, height=70)

    # 사용자 입력부분
    global InputLabel
    InputLabel = Entry(window, font=fontNormal, width=36, borderwidth=3, relief='ridge', cursor="xterm")
    InputLabel.place(x=110, y=170, width=220, height=70)

    InputButton = Button(window, font=fontNormal, image=searchImage, command=onSearch, bg="white",cursor="hand2", overrelief="groove", activebackground= "dark grey")
    InputButton.place(x=110 + 220, y=170, width=70, height=70)

    # 필터 초기화 버튼 부분
    global ResetButton
    ResetButton = Button(window, bg="white", command=resetFilter, font=fontNormal, text=getStr(clist[selectedCity[0]]) + "\t\t" + getStr(dlist[selectedDept[0]]), cursor="hand2", overrelief="sunken")
    ResetButton.place(x=410, y=90, width=380, height=70 )

    # 목록 부분
    global listBox
    ListScrollBar = Scrollbar(window)
    listBox = Listbox(window, selectmode='extended', font=fontList, width=10, height=15, \
        borderwidth=5, relief='ridge', yscrollcommand=ListScrollBar.set, cursor="hand2")
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.place(x = 10, y = 250, width=380 - 10, height=340)

    ListScrollBar.place(x = 390 - 10, y = 250, width=20, height=340)
    ListScrollBar.config(command=listBox.yview, cursor="sb_v_double_arrow")

    # 분류 제목 부분
    global CityLabel, NameLabel, DeptLabel
    CityLabel = Label(window, text="시(군) 선택", font=fontLabel, bg = "white", image=labelImage, compound='center')
    DeptLabel = Label(window, text="진료 과목", font=fontLabel, bg = "white", image=labelImage, compound='center')
    NameLabel = Label(window, text="병원명", font=fontLabel, bg = "white", image=labelImage, compound='center')

    CityLabel.place(x=10, y=10, width=100, height=70)
    DeptLabel.place(x=10, y=90, width=100, height=70)
    NameLabel.place(x=10, y=170, width=100, height=70)

    # 로고 부분
    global LogoLabel
    LogoLable = Button(window, image=logoImage, bg="white", command=onLogo, relief="flat", activebackground= "dark grey", cursor="hand2", overrelief="groove")
    LogoLable.place(x=410, y=10, width=380, height=70)

    # 그래프 부분
    global GraphButton
    GraphButton = Button(window, bg="white", image=graphImage, command=onGraphPopup, activebackground= "dark grey", cursor="hand2", overrelief="sunken")
    GraphButton.place(x=410, y=170, width=72, height=72)
    
    # 메일 부분
    global MailButton
    MailButton = Button(window, image=emailImage, bg="white", command=onEmailPopup, activebackground= "dark grey", cursor="hand2", overrelief="sunken")
    MailButton.place(x=410 + 76, y=170, width=72, height=72)

    # 지도 부분
    global MapButton
    MapButton = Button(window, image=mapImage, bg="white", command=onMapPopup, activebackground= "dark grey", cursor="hand2", overrelief="sunken")
    MapButton.place(x=410 + 76 * 2, y=170, width=72, height=72)   

    # 링크 부분
    global LinkButton
    LinkButton = Button(window, image=linkImage, bg="white", command=onLink, activebackground= "dark grey", cursor="hand2", overrelief="sunken")
    LinkButton.place(x=410 + 76 * 3, y=170, width=72, height=72)

    # 텔레그램 부분
    global TelegramButton
    TelegramButton = Button(window, image=telegramImage, bg="white", activebackground= "dark grey", cursor="hand2", overrelief="sunken")
    TelegramButton.place(x=410 + 76 * 4, y=170, width=72, height=72)   

    # 정보 부분
    global InfoLabel, ST
    # TempText = "해당병원 정보출력\nex) 위치, 입원, 실수, 전화번호"
    # InfoLabel = Label(text = TempText, font=fontInfo, bg="#bebebe", justify="left")
    # InfoLabel.place(x = 410, y= 220, width=380, height=370)

    ST = st.ScrolledText(window, font=fontInfo, cursor="arrow")
    ST.place(x = 410, y= 250, width=380, height=370 + 48 - 80)

def setCity(event):
    global selectedCity, CityListBox, clist, ResetButton
    sel = event.widget.curselection()
    if sel:
        selectedCity = sel
        # print(selectedCity[0])
        ResetButton.configure(text=getStr(clist[selectedCity[0]]) + "\t\t" + getStr(dlist[selectedDept[0]]))

def setDept(event):
    global selectedDept, ResetButton
    sel = event.widget.curselection()
    if sel:
        selectedDept = sel
        ResetButton.configure(text=getStr(clist[selectedCity[0]]) + "\t\t" + getStr(dlist[selectedDept[0]]))
        # print(selectedDept[0])    

def resetFilter():
    global selectedCity, selectedDept
    # print(selectedCity)
    selectedCity = [0]
    selectedDept = [0]
    ResetButton.configure(text=getStr(clist[selectedCity[0]]) + "\t\t" + getStr(dlist[selectedDept[0]]))   
    # print(selectedCity)

    global listBox
    listBox.delete(0, listBox.size())

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
                '\n\n' + '[병상수]' + '\n' +getStr(item.find('MEDSTAF_CNT').text) 
                server.hospital_name = getStr(item.find('BIZPLC_NM').text)
                
                if item.find('REFINE_WGS84_LAT').text == None and item.find('REFINE_WGS84_LOGT').text == None:
                    server.latitude = 0.0
                    server.longitude = 0.0    
                    MapButton.configure(image=noImage)
                                    
                else:
                    server.latitude = float(item.find('REFINE_WGS84_LAT').text)
                    server.longitude = float(item.find('REFINE_WGS84_LOGT').text)
                    MapButton.configure(image=mapImage)  
                
                # print(server.latitude, server.longitude)

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

def onLogo():
    url = 'https://github.com/WOOLUCY/scriptlang/tree/main/TermProject'
    webbrowser.open(url)

def onLink():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=' + server.hospital_name
    webbrowser.open(url)

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
        
        # 시군 O, 과목 O
        if item.find('SIGUN_NM').text == city and dept in getStr(item.find('TREAT_SBJECT_CONT_INFO').text) and item.find('BSN_STATE_NM') != "폐업":
            _text = getStr(item.find('BIZPLC_NM').text) 
            
            listBox.insert(i-1, _text)
            i = i + 1

        # 시군 O, 과목 X 
        elif item.find('SIGUN_NM').text == city and dept == "선택안함" and item.find('BSN_STATE_NM') != "폐업":
            _text = getStr(item.find('BIZPLC_NM').text) 
            
            listBox.insert(i-1, _text)
            i = i + 1

        # 시군 X, 과목 O
        elif dept in getStr(item.find('TREAT_SBJECT_CONT_INFO').text) and city == "선택안함" and item.find('BSN_STATE_NM') != "폐업":
            _text = getStr(item.find('BIZPLC_NM').text) 
            
            listBox.insert(i-1, _text)
            i = i + 1        
        
        elif city == "선택안함" and dept == "선택안함" and item.find('BSN_STATE_NM') != "폐업":
            _text = getStr(item.find('BIZPLC_NM').text)
            
            listBox.insert(i-1, _text)
            i = i + 1

InitScreen()
window.mainloop()
