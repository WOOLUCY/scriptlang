from tkinter import *

window = Tk()
window.title("어디병원")
window.geometry("800x600+450+200")
window.resizable(False, False)
window.configure(bg='white')

# datas
info_text = None
hospital_name = None

latitude = 0.0      # 위도
longitude = 0.0     # 경도

city_list = ['선택안함', '가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', \
    '김포시', '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', \
    '안양시', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시', '의왕시', '의정부시', \
    '이천시', '파주시', '평택시', '포천시', '하남시', '화성시']

dept_list = ['선택안함', '가정의학과', '결핵과', '구강내과', '구강병리과', '구강악안면방사선과', \
    '구강악안면외과', '내과', '마취통증의학과', '방사선종양학과', '방사선종양학과', '병리과', '비뇨의학과', \
    '사상체질과', '사상체질과', '산부인과', '성형외과', '소아청소년과', '신경과', \
    '신경외과', '안과', '영상의학과', '영상치의학과', '예방의학과', '외과', '응급의학과', \
    '이비인후과', '재활의학과', '정신건강의학과', '정형외과', '직업환경의학과', '진단검사의학과', \
    '치과', '치주과', '침구과', '통합치의학과', '피부과', '한방내과', '한방부인과', \
    '한방소아과', '한방신경정신과', '한방안·이비인후·피부과', '한방응급과', '한방재활의학과', '핵의학과', '흉부외과']

hList = [0 for i in city_list]

mail_list = []

mouse_x = 0
mouse_y = 0


if __name__ == '__main__':
    print("\nserver.py runned\n")
else:
    print("\nserver.py imported\n")