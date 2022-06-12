'''
book_mark.py
런처에서 북마크 버튼을 누르면 실행되는 모듈입니다.

functions
- onMarkPopup
- deleteHospital
- showInfo
- makeBookMark
'''

# === import ===
import pickle   # 피클 모듈을 사용한 북마크
from click import command
import server
import tkinter.messagebox as msgbox
import os
from tkinter import *
from tkinter import font
import tkinter.scrolledtext as st

# C/C++ 연동
import cLink

selHospital = None

# === functions ===
def onMarkPopup():  # 북마크 팝업을 띄움
    global popup
    print("graph button clicked")
    popup = Toplevel()
    popup.geometry("800x370+450+200")
    popup.title("북마크")
    popup.resizable(False, False)

    fontInfo = font.Font(popup, size=10, family='G마켓 산스 TTF Medium')
    fontList = font.Font(popup, size=14, family='G마켓 산스 TTF Medium') 

    # 북마크 병원 목록 리스트박스
    global listBox
    ListScrollBar = Scrollbar(popup)
    listBox = Listbox(popup, selectmode='extended', font=fontList, width=10, height=15, \
        borderwidth=5, relief='ridge', yscrollcommand=ListScrollBar.set, cursor="hand2")

    dirpath = os.getcwd()
    if os.path.isfile(dirpath + '\mark'):            
        f = open('mark', 'rb')
        dic = pickle.load(f) 
        f.close()
        server.MarkDict = dic

    print(server.MarkDict.keys())
    i = 0
    for hospital, info in server.MarkDict.items():
        print(hospital)
        listBox.insert(i, hospital)
        i = i + 1

    listBox.bind('<<ListboxSelect>>', showInfo)
    listBox.place(x = 10, y = 0, width=390 - 10, height=340)

    ListScrollBar.place(x = 390, y = 0, width=20, height=340)
    ListScrollBar.config(command=listBox.yview, cursor="sb_v_double_arrow")

    # 선택된 병원의 정보 출력하는 ScrolledText
    global ST
    ST = st.ScrolledText(popup, font=fontInfo, cursor="arrow")
    ST.place(x = 390 + 20, y = 0, width=385, height=340)

    # 선택된 병원 삭제 버튼
    global deleteButton
    deleteButton = Button(popup, font=fontList, text='북마크에서 해당 병원 제외하기', command=deleteHospital)
    deleteButton.place(x = 0, y = 340, width=800, height=30)

def deleteHospital():       # 북마크에서 선택된 병원을 삭제하는 함수
    global ST
    if len(server.MarkDict) == 0:   # 북마크가 빈 상태에서 삭제 버튼을 누른 경우
        msgbox.showinfo("알림", "북마크가 비어있습니다.")  
        popup.focus_set()
    else: 
        if selHospital in server.MarkDict:
            del server.MarkDict[selHospital]     

            f = open('mark', 'wb')              
            pickle.dump(server.MarkDict, f)    
            f.close()
            ST.delete('1.0', END)

def showInfo(event):   # 병원 리스트박스에서 병원 선택 시 정보 출력하는 함수
    global InfoLabel, ST, selHospital
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        selHospital = data

        if data in server.MarkDict:
            info = server.MarkDict[data]
            ST.configure(state="normal")    # 수정 가능으로 풀어놨다가,
            ST.delete('1.0', END)
            ST.insert(INSERT, info)
            ST.configure(state="disabled")  # 수정 불가능(읽기 전용)으로 변경


def makeBookMark():    
    # 북마크를 추가하는 함수
    # 런쳐 노트북 3페이지에서 북마크 저장 버튼을 눌렀을 시 실행
    if server.hospital_name:
        if server.hospital_name in server.MarkDict:
            msgbox.showinfo("알림", "이미 북마크에 추가한 병원입니다.")          

        else:
            text = server.info_text + '\n\n' + '[MEMO]' + '\n' + server.memo_text

            dirpath = os.getcwd()

            if os.path.isfile(dirpath + '\mark'):            
                f = open('mark', 'rb')
                server.MarkDict = pickle.load(f)   
                f.close()

                server.MarkDict[server.hospital_name] = text

                f = open('mark', 'wb')     
                pickle.dump(server.MarkDict, f) 
                f.close()

                f = open('mark', 'rb')
                server.MarkDict = pickle.load(f) 
                f.close()

                print(server.MarkDict)

            else:
                server.MarkDict[server.hospital_name] = text
                f = open('mark', 'wb') 
                pickle.dump(server.MarkDict, f)
                f.close()

                print(server.MarkDict)

            # C/C++ 연동
            try:        # cLink.pyd 파일을 Lib에 추가시킨 경우
                text = "성공적으로 북마크를 저장했습니다.\n메모 글자수: " + str(cLink.strlen(server.memo_text)) + "자"
                msgbox.showinfo("알림", text)
            except:     # cLink.pyd 파일을 Lib에 추가시키지 않은 경우
                msgbox.showinfo("알림", "성공적으로 북마크를 저장했습니다.")                

    else:   # 예외 처리
        msgbox.showinfo("알림", "목록에서 병원을 먼저 선택해주십시오.")


if __name__ == '__main__':
    print("book_mark.py runned\n")
else:
    print("book_mark.py imported\n")