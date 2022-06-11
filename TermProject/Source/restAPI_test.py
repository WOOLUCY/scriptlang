import sys
import telepot
from pprint import pprint # 데이터를 읽기 쉽게 출력
from urllib.request import urlopen
import traceback
from xml.etree import ElementTree
from xml.dom.minidom import parseString

key = 'ZuzmMcb5viQ3a2SApJ8lHnLxu0st3sTXRGVXlEtlL8bh62SZjKNRTMgjbh0sLpxIjNR5h9ShzPoE1Jg%2FpXQUiQ%3D%3D'
TOKEN = '5480492402:AAEsYgy21URB4B8vFAshYMu7UUvQRF8-3H8'    # 텔레그램 봇 토큰
MAX_MSG_LENGTH = 300
baseurl = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?ServiceKey='+key
bot = telepot.Bot(TOKEN)

# loc_param: 지역코드, date_param: yyyymm
# 반환 : 거래 건 별로 문자열로 표현한 리스트. 
def getData(): 
    res_list = [] 
    url = "https://openapi.gg.go.kr/GgHosptlM?pSize=1000&pIndex=1&KEY=8a2e77d6b1a846d1a28fff0ca47f1215"
    res_body = urlopen(url).read() 
    strXml = res_body.decode('utf-8')
    tree = ElementTree.fromstring(strXml)

    items = tree.iter("row") # return list type
    for item in items: 
        name = item.find('BIZPLC_NM').text.strip()
        row = name
        res_list.append(row) 
    print(res_list)
    return res_list

def sendMessage(user, msg): 
    try:
        bot.sendMessage(user, msg) 
    except: 
        # 예외 정보와 스택 트레이스 항목을 인쇄. 
        traceback.print_exception(*sys.exc_info(), file=sys.stdout)

getData()