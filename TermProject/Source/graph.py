from tkinter import * 
import server

def onGraphPopup(): 
    print("reset button clicked")
    



def drawGraph(canvas, data, canvasWidth, canvasHeight):
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
    for i in range(nData): # 각 데이터에 대해.. 
        # max/min은 특별한 색으로.
        if nMax == data[i]: color="red" 
        elif nMin == data[i]: color='blue' 
        else: color="grey"    

        curHeight = maxheight * data[i] / nMax # 최대값에 대한 비율 반영
        top = bottom - curHeight # bar의 top 위치
        left = i * rectWidth # bar의 left 위치
        right = (i + 1) * rectWidth # bar의 right 위치
        canvas.create_rectangle(left, top, right, bottom, fill=color, tag="grim", activefill='yellow')

        # 위에 값, 아래에 번호. 
        canvas.create_text((left+right)//2, top-10, text=data[i], tags="grim") 
        canvas.create_text((left+right)//2, bottom+10, text=server.city_list[i+1], tags="grim")

window = Tk() 
window.title('tkinter notebook') 
window.geometry("1200x400+200+100")

w = Canvas(window, width = 1200, height=400, bg='green') 
w.place(relx=.5, rely=.5,anchor= CENTER) # 한가운데 위치

#drawGraph(w, [], 300, 300) # 시험용 데이터
#drawGraph(w, [670, 900, 150], 300, 300) # 시험용 데이터
drawGraph(w, [100, 200, 670, 900, 150], 1200, 400)

window.mainloop()