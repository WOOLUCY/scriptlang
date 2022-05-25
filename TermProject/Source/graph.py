from gc import callbacks
from http.client import CannotSendHeader
from msilib import sequence
from tkinter import *

from click import command
from numpy import insert 
import server
from tkinter import font

def onGraphPopup(): 
    global popup
    print("graph button clicked")
    popup = Toplevel()
    popup.geometry("1200x400+100+100")
    popup.title("경기도 병원 현황 내 시군별 병원 그래프")
    popup.resizable(False, False)
    popup.bind('<Button-1>', mouseClicked)

    w = Canvas(popup, width = 1200, height=400, bg='white') 
    w.place(relx=.5, rely=.5,anchor= CENTER) # 한가운데 위치

    getData()
    
    drawGraph(w, server.hList[1:], 1200, 400)


def drawGraph(canvas, data, canvasWidth, canvasHeight):
    fontLittle = font.Font(popup, size=8, family='나눔바른고딕') 

    canvas.delete("grim") # 기존 그림 지우기
    if not len(data): # 데이터 없으면 return
        canvas.create_text(canvasWidth/2,(canvasHeight/2), text="No Data", tags="grim")
        return

    nData = len(data) # 데이터 개수, 최대값, 최소값 얻어 놓기
    nMax = max(data) 
    nMin = min(data)

    # background 그리기
    canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill='white', tag="grim")

    if nMax == 0: # devide by z
        nMax = 1

    rectWidth = (canvasWidth // nData) # 데이터 1개의 폭. 
    bottom = canvasHeight - 20 # bar의 bottom 위치 
    maxheight = canvasHeight - 40 # bar의 최대 높이.(위/아래 각각 20씩 여유.)

    global leftList, topList
    leftList = []
    topList = []

    for i in range(nData): # 각 데이터에 대해.. 
        # max/min은 특별한 색으로.
        if nMax == data[i]: color="red" 
        elif nMin == data[i]: color='blue' 
        else: color="grey"    

        curHeight = maxheight * data[i] / nMax # 최대값에 대한 비율 반영
        top = bottom - curHeight # bar의 top 위치
        left = i * rectWidth # bar의 left 위치
        right = (i + 1) * rectWidth # bar의 right 위치
        leftList.append(left)
        topList.append(top)

        city = server.city_list[i + 1]
        canvas.create_rectangle(left, top, right, bottom, fill=color, tags=city, activefill='yellow')

        # 위에 값, 아래에 번호. 
        canvas.create_text((left+right)//2, top-10, text=data[i], tags="grim") 
        canvas.create_text((left+right)//2, bottom+10, text=server.city_list[i + 1], font = fontLittle, tags="grim")

    leftList.append(1178)



def clicked(*args):
    global leftList
    print(server.mouse_x, server.mouse_y)
    print("hello")
    

def getCity():
    print("hello")

def getData():
    # 클릭 시, 정보 출력
    from xml.etree import ElementTree
    with open('경기도병원현황.xml', 'rb') as f:
        strXml = f.read().decode('utf-8')
    parseData = ElementTree.fromstring(strXml)

    elements = parseData.iter('row')
    for item in elements:   # 'row' element들
        # if item.find('SIGUN_NM').text in hList
        for i, city in enumerate(server.city_list):
            if item.find('SIGUN_NM').text == city:
                server.hList[i] += 1           
    # for i, city in enumerate(server.hList):
    #     print(server.city_list[i], city)

def mouseClicked(event):
    server.mouse_x= event.x
    server.mouse_y= event.y
    for i, left in enumerate(leftList):
        if left <= server.mouse_x < leftList[i + 1]:
            if ( topList[i] < server.mouse_y):
                print(server.city_list[i+1])



if __name__ == '__main__':
    onGraphPopup()
    print("\graph.py runned\n")
else:
    print("\graph.py imported\n")