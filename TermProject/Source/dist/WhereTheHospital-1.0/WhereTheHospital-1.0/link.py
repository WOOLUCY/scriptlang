# 여러 가지 링크
import webbrowser
import server
import tkinter.messagebox as msgbox

def onLogo():   # command for logo button
    url = 'https://github.com/WOOLUCY/scriptlang/tree/main/TermProject'
    webbrowser.open(url)

def onNaverLink():   # command for link button
    if server.hospital_name:
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=' + server.hospital_name
        webbrowser.open(url)
    else:
        msgbox.showinfo("알림", "목록에서 병원을 먼저 선택해주십시오.")

def onGoogleLink():   # command for link button
    if server.hospital_name:
        url = 'https://www.google.com/search?q=' + server.hospital_name
        webbrowser.open(url)
    else:
        msgbox.showinfo("알림", "목록에서 병원을 먼저 선택해주십시오.")

def onNaverMapLink():
    if server.hospital_name:
        url = 'https://map.naver.com/v5/search/' + server.hospital_name
        webbrowser.open(url)
    else:
        msgbox.showinfo("알림", "목록에서 병원을 먼저 선택해주십시오.")