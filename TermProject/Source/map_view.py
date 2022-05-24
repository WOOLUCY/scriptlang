import server
from tkinter import * 
import tkintermapview

def onMapPopup():
    popup = Toplevel()
    popup.geometry("800x600+650+400")
    popup.title("Map")

    # root = Tk()
    # root.geometry(f"{800}x{600}")
    # root.title("map_view_example.py")

    map_widget = tkintermapview.TkinterMapView(popup, width=800, height=600, corner_radius=0) 
    map_widget.pack()

    marker_1 = map_widget.set_position(37.3134804, 126.8276347, marker=True) # 위도,경도 위치지정
    # 주소 위치지정 
    # marker_1 = map_widget.set_address("경기도 시흥시 산기대학로 237", marker=True)
    print(marker_1.position, marker_1.text) # get position and text 
    marker_1.set_text(server.hospital_name) # set new text 
    map_widget.set_zoom(15) # 0~19 (19 is the highest zoom level) 

    # root.mainloop()

onMapPopup()

if __name__ == '__main__':
    onMapPopup()
    print("\nmap_view.py runned\n")
else:
    print("\nmap_view.py imported\n")