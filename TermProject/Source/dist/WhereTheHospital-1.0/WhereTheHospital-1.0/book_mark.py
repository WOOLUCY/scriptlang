import pickle
from click import command
import server
import tkinter.messagebox as msgbox
import os
from tkinter import *
from tkinter import font
import tkinter.scrolledtext as st

selHospital = None

def onMarkPopup():
    global popup
    print("graph button clicked")
    popup = Toplevel()
    popup.geometry("800x370+450+200")
    popup.title("북마크")
    popup.resizable(False, False)

    fontInfo = font.Font(popup, size=10, family='G마켓 산스 TTF Medium')
    fontList = font.Font(popup, size=14, family='G마켓 산스 TTF Medium') 

    # 병원 목록 부분
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

    # 진료 과목 내용 정보
    global ST
    ST = st.ScrolledText(popup, font=fontInfo, cursor="arrow")
    ST.place(x = 390 + 20, y = 0, width=385, height=340)

    # 병원 삭제 버튼
    global deleteButton
    deleteButton = Button(popup, font=fontList, text='북마크에서 해당 병원 제외하기', command=deleteHospital)
    deleteButton.place(x = 0, y = 340, width=800, height=30)

def deleteHospital():
    global ST
    if len(server.MarkDict) == 0:
        msgbox.showinfo("알림", "북마크가 비어있습니다.")  
        popup.focus_set()
    else: 
        if selHospital in server.MarkDict:
            del server.MarkDict[selHospital]     

            f = open('mark', 'wb')              
            pickle.dump(server.MarkDict, f)    
            f.close()
            ST.delete('1.0', END)

def showInfo(event):   # command for list box
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

    else:
        msgbox.showinfo("알림", "목록에서 병원을 먼저 선택해주십시오.")