from tkinter import *
import server
import tkintermapview
from tkinter import font
import tkinter.messagebox as msgbox

isSatellite = True

satelliteImage = PhotoImage(file='image/satellite.png')             # satellite map image
normalImage = PhotoImage(file='image/normal_map.png')               # normal map image
hospitalImage = PhotoImage(file='image/hospital.png')               # hospital image
searchImage = PhotoImage(file='image/little_search.png')            # search hospital image

def onMapPopup():
    if server.hospital_name == None: 
        msgbox.showinfo("알림", "목록에서 병원을 먼저 선택해주십시오.")
        return
    global popup
    popup = Toplevel()
    popup.geometry("800x600+100+100")
    popup.title("<" + server.hospital_name + "> 의 지도")
    
    fontNormal = font.Font(popup, size=18, family='G마켓 산스 TTF Medium')

    if server.latitude == 0 and server.longitude == 0:
        emptyLabel = Label(popup, width=800, height=600, text="해당 병원의 지도 정보가 없습니다.", font=fontNormal)
        emptyLabel.pack()

    else:
        global map_widget, marker_1
        map_widget = tkintermapview.TkinterMapView(popup, width=800, height=550, corner_radius=0) 
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22) 
        map_widget.place(x=0, y=0, width=800, height=550)
        map_widget.add_right_click_menu_command(label="Add Marker", command=add_marker_event, pass_coords=True)


        # 주소 위치지정 
        marker_1 = map_widget.set_position(server.latitude, server.longitude, marker=True, marker_color_outside="black", marker_color_circle="white", text_color="black") # 위도,경도 위치지정
        marker_1.set_text(server.hospital_name) # set new text

        global addressLabel, InputButton, HospitalButton, SatButton
        addressLabel = Entry(popup, font=fontNormal, width=800, borderwidth=3, relief='ridge')
        addressLabel.place(x=0, y=550, width=650, height=50)

        InputButton = Button(popup, font=fontNormal, image=searchImage, command=onSearch, bg = "white", cursor="hand2")
        InputButton.place(x=650, y=550, width=50, height=50)   

        HospitalButton = Button(popup, font=fontNormal, image=hospitalImage, command=onHospital, bg="white", cursor="hand2")
        HospitalButton.place(x=700, y=550, width=50, height=50)   

        SatButton = Button(popup, font=fontNormal, command=onSat, image=satelliteImage, bg="white", cursor="hand2")
        SatButton.place(x=750, y=550, width=50, height=50)  

        map_widget.set_zoom(15) # 0~19 (19 is the highest zoom level) 

def onSearch():
    global destAddr, marker_2
    destAddr = addressLabel.get()
    marker_2 = map_widget.set_address(destAddr, marker=True, marker_color_outside="black", marker_color_circle="white", text_color="black") 
    marker_2.set_text(destAddr)

    path_1 = map_widget.set_path([marker_1.position, marker_2.position]) 
    map_widget.set_position(server.latitude, server.longitude)

    addressLabel.delete(0, 'end')

    map_widget.set_zoom(15)

def onHospital():
    map_widget.set_zoom(15)
    map_widget.set_position(marker_1.position[0], marker_1.position[1])

def onSat():
    global isSatellite
    if isSatellite:
        isSatellite = False
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google satellite
        map_widget.set_zoom(16)
        SatButton.configure(image=normalImage)
    else:
        isSatellite = True
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22) 
        map_widget.set_zoom(15)
        SatButton.configure(image=satelliteImage)
    
def add_marker_event(coords):
    print("Add marker:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="new marker")
    map_widget.set_path([coords, marker_1.position])
    
if __name__ == '__main__':
    print("map.py runned\n")
else:
    print("map.py imported\n")
