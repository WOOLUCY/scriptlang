from tkinter import *
import tkintermapview
from tkinter import font
from xml.etree import ElementTree
from urllib.request import urlopen
import server

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
    fontLittle = font.Font(popup, size=7, family='G마켓 산스 TTF Medium') 

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
        if nMax == data[i]: color="skyblue3" 
        elif nMin == data[i]: color='light pink' 
        else: color="ivory2"    

        curHeight = maxheight * data[i] / nMax # 최대값에 대한 비율 반영
        top = bottom - curHeight # bar의 top 위치
        left = i * rectWidth # bar의 left 위치
        right = (i + 1) * rectWidth # bar의 right 위치
        leftList.append(left)
        topList.append(top)

        city = server.city_list[i + 1]
        canvas.create_rectangle(left, top, right, bottom, fill=color, tags=city, activefill='ivory4')

        # 위에 값, 아래에 번호. 
        canvas.create_text((left+right)//2, top-10, text=data[i], tags="grim") 
        canvas.create_text((left+right)//2, bottom+10, text=server.city_list[i + 1], font = fontLittle, tags="grim")

    leftList.append(1178)

def getData():
    # 클릭 시, 정보 출력
    key = "8a2e77d6b1a846d1a28fff0ca47f1215"
    url = "https://openapi.gg.go.kr/GgHosptlM?pSize=1000&pIndex=1&KEY=" + key

    res_body = urlopen(url).read()
    strXml = res_body.decode('utf-8')
    tree = ElementTree.fromstring(strXml)

    elements = tree.iter("row")

    for item in elements:   # 'row' element들
        for i, city in enumerate(server.city_list):
            if item.find('SIGUN_NM').text == city:
                server.hList[i] += 1           

def mouseClicked(event):
    server.mouse_x= event.x
    server.mouse_y= event.y
    for i, left in enumerate(leftList):
        if left <= server.mouse_x < leftList[i + 1]:
            if ( topList[i] < server.mouse_y):
                print(server.city_list[i+1])
                onMapPopup(server.city_list[i+1])

def onMapPopup(city):
    global map_popup
    map_popup = Toplevel()
    map_popup.geometry("800x600+100+100")
    map_popup.title("<" + city + "> 내 병원")

    fontNormal = font.Font(map_popup, size=24, family='G마켓 산스 TTF Medium')

    global map_widget
    map_widget = tkintermapview.TkinterMapView(map_popup, width=800, height=600, corner_radius=0) 
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22) 
    map_widget.place(x=0, y=0, width=800, height=600)

    key = "8a2e77d6b1a846d1a28fff0ca47f1215"
    url = "https://openapi.gg.go.kr/GgHosptlM?pSize=1000&pIndex=1&KEY=" + key

    res_body = urlopen(url).read()
    strXml = res_body.decode('utf-8')
    tree = ElementTree.fromstring(strXml)

    elements = tree.iter("row")
    for item in elements:   # 'row' element들
        if item.find('SIGUN_NM').text == city and getStr(item.find('REFINE_WGS84_LAT').text) != '정보없음' and getStr(item.find('REFINE_WGS84_LOGT').text) != '정보없음':
            # 주소 위치지정 
            lat = float(item.find('REFINE_WGS84_LAT').text)
            logt = float(item.find('REFINE_WGS84_LOGT').text)
            marker_1 = map_widget.set_position(lat, logt, \
                marker=True, marker_color_outside="grey", marker_color_circle="white") # 위도,경도 위치지정
            marker_1.set_text(item.find('BIZPLC_NM').text) # set new text

            map_widget.set_zoom(12)

def getStr(s):
    return '정보없음' if not s else s

if __name__ == '__main__':
    onGraphPopup()
    print("graph.py runned\n")
else:
    print("graph.py imported\n")