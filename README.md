# 어디병원: Where The Hospital
![logo](https://user-images.githubusercontent.com/89962345/173218210-ca651684-be63-4a68-974b-10cf2c18b40a.png)
#### 한국공학대학교 게임공학과 2022학년도 1학기 스크립트 언어 과목의 Term Project입니다.
Contributors: [우정연](https://github.com/WOOLUCY), [강경천](https://github.com/KangGyeongCheon)

## 목차
- [프로그램 개요](#프로그램-개요)
- [사용한 API](#사용한-api)
- [프로그램 기능](#프로그램-기능)
  - [1. OpenAPI 연동 검색](#openapi-연동-검색)
  - [2. 병원 정보 출력](#병원-정보-출력)
  - [3. 링크](#링크)
  - [4. 북마크](#북마크)
  - [5. 그래프](#그래프)
  - [6. 메일 보내기](#메일-보내기)
  - [7. 지도](#지도)
  - [8. GUI 내 텔레그램 보내기](#gui-내-텔레그램-보내기)
  - [9. 텔레그램 봇](#텔레그램-봇)
- [프로그램 모듈](#프로그램-모듈)
  - [1. where_hospital](#where_hospital)
  - [2. book_mark](#book_mark)
  - [3. gmail_send](#gmail_send)
  - [4. graph](#graph)
  - [5. link](#link)
  - [6. map](#map)
  - [7. telegram](#telegram)
  - [8. telegram_bot](#telegram_bot)
  - [9. server](#server)
- [유의사항](#유의사항)
- [발표 영상](#발표-영상)


## 프로그램 개요
![프로그램 GUI](https://user-images.githubusercontent.com/89962345/173217507-d349b8a4-46f5-42b3-920d-3ab683727320.png)

- 파이썬 내의 tkinter 모듈을 사용한 GUI 프로그래밍입니다.
- 경기도에 있는 다양한 병원 정보를 알려주는 프로그램입니다.
- 시군별, 진료과목별 병원을 검색할 수 있습니다.  


## 사용한 API
- [경기도 병원 현황 Link](https://www.data.go.kr/data/15056746/openapi.do?recommendDataYn=Y)
- 경기도 내의 시군별 병원에 대한 현황입니다.
- 경기도 내의 병원, 의원, 한의원 등의 병원명, 소재지주소, 소재지 위치 등의 정보를 제공합니다.


## 프로그램 기능
### OpenAPI 연동 검색 
![search](https://user-images.githubusercontent.com/89962345/173219294-05f6cf11-b9f7-4839-b74f-9b3e2ee25f87.png)
- **시군별, 진료과목별** 필터 검색이 가능합니다.
- **병원명** 을 입력해 원하는 병원을 검색할 수 있습니다.
- 검색할때마다 **REST API** 이용합니다.
- **필터 리셋** 기능을 버튼으로 지원합니다.



### 병원 정보 출력
![show](https://user-images.githubusercontent.com/89962345/173219403-ba239528-ac8a-4df3-860f-c50a0c0f7606.png)
- 리스트에서 선택한 병원 정보 출력
- 병원 정보는 병원명, 의료기관종별명, 전화번호, 도로명 주소, 지번 주소, 진료 과목, 의료인수, 입원실수, 병상수를 포함합니다.



### 링크
![link](https://user-images.githubusercontent.com/89962345/173219519-489d3d60-5e17-42fd-a274-6a154cae2c66.png)
- 선택한 병원의 검색결과 링크로 이동합니다.
- 구글 검색결과, 네이버 검색 결과, 네이버 지도 검색 결과를 지원합니다.



### 북마크
![bookmark](https://user-images.githubusercontent.com/89962345/173219601-ed6258e9-33c9-40e1-9351-82186837c4ab.png)
- 선택한 병원을 북마크 피클에 저장할 수 있습니다.
- 북마크에 저장할 때, 메모를 추가할 수 있습니다.
- 북마크에 저장한 병원을 다시 제거할 수 있습니다.
- 버튼 이미지로 해당 병원이 북마크에 포함되어있는지 확인할 수 있습니다.

|미포함 시|포함 시|
|-------|--------|
|![white_bookmark](https://user-images.githubusercontent.com/89962345/173219703-abad93c0-37f1-4c2c-9296-6389f844555d.png)|![bookmark](https://user-images.githubusercontent.com/89962345/173219704-b1a5c0c5-184d-4f1f-bdb4-e0eda3a8cd05.png)|



### 그래프
![trend](https://user-images.githubusercontent.com/89962345/173219776-ded877f0-b198-4c9a-aa8f-fcda25259819.png)
- 경기도 시군별 병원 현황을 그래프로 나타냅니다.
- 바를 클릭하면 해당하는 시군의 병원을 모두 보여주는 지도창이 뜹니다.


### 메일 보내기
![mail_icon3](https://user-images.githubusercontent.com/89962345/173219941-a4762350-1469-46d0-9f34-7e7f261a18ff.png)
- 팝업창에서 수신 메일 주소를 입력할 수 있습니다.
- 목록에서 선택한 병원의 정보를 입력한 메일 주소로 보냅니다.


### 지도
![map](https://user-images.githubusercontent.com/89962345/173220029-d5421311-37e7-4e4c-98ab-9cb781e3a0bd.png)
- 목록에서 선택한 병원의 위치를 지도에서 보여줍니다.
- 원하는 주소를 입력하면 병원에서 주소까지의 직선거리를 출력합니다.
- 병원 주소 버튼을 누르면 지도 내에서 병원 위치로 다시 이동합니다.
- 위성 지도를 지원합니다.
- 버튼 이미지로 병원의 주소 정보 제공 여부를 알 수 있습니다.

|제공 시|미제공 시|
|--|--|
|![map_icon2](https://user-images.githubusercontent.com/89962345/173220090-b195c112-b2e8-4683-8795-4e7ddf00881f.png)|![close](https://user-images.githubusercontent.com/89962345/173220084-d213a403-e1ab-43d8-be83-b238d5fcf6c5.png)|


### GUI 내 텔레그램 보내기
![telegram_icon](https://user-images.githubusercontent.com/89962345/173220131-e12ea5f1-00a0-4bbf-a12a-9f9dbe5a0f86.png)
- 목록에서 선택한 병원의 정보를 텔레그램에서 전송합니다.

### 텔레그램 봇
![telegram](https://user-images.githubusercontent.com/89962345/173220170-8d030386-4fd0-4e89-8a8c-5e6fbed7ce9f.png)
- 다양한 명령어를 통해 병원 정보를 받을 수 있습니다.
  - 도움말: 명령어를 찾아볼 수 있습니다.
  - 검색 + '병원명': 해당 병원 정보를 출력합니다. 예) 검색 한강요양병원
  - 시군 + '지역명': 지역 내에 있는 병원을 모두 출력합니다. 예) 시군 시흥시
  - 북마크: 내 북마크에 저장된 병원 정보를 볼 수 있습니다.
  - 저장 + '병원명': 북마크에 병원을 저장할 수 있습니다. 예) 저장 한강요양병원
- telegram_bot 모듈을 실행해야 합니다.

## 프로그램 모듈
### where_hospital
- **어디병원의 메인 모듈**
- 메인 GUI 창을 시작하고, 필터에 따라 검색하는 기능을 가지고 있습니다.
- 검색한 병원의 정보를 서버에 넘기는 역할을 합니다.
- 내장 함수
  - InitScreen: 메인 GUI 창을 시작
  - setCity, setDept: 필터를 설정
  - resetFilter: 필터를 초기화
  - onSearch: 필터 정보를 합해 검색 함수에 넘김
  - getStr: 유틸리티 함수
  - saveMemo: 입력한 메모를 저장해 서버로 넘김
  - event_for_listbox: 목록에서 선택한 병원의 정보를 조회 (REST API 사용)
  - SearchHospital: 병원 목록을 구성 (REST API 사용)

### book_mark
- 런처에서 북마크 버튼을 누를 때 사용
- C/C++ 연동 기능 포함
- 내장 함수
  - onMarkPopup: 북마크 팝업을 엶
  - deleteHospital: 선택된 병원을 북마크에서 삭제
  - showInfo: 리스트에서 선택 된 병원의 정보 출력
  - makeBookMark: 북마크를 추가

### gmail_send
- 런처에서 이메일 버튼을 누를 때 사용
- 내장 함수
  - sendMail: SMTP 연결로 메일 보내는 함수
  - onEmailInput: HTML 파일 변환, 작성 후 메일 보내기
  - onEmailPopup: 메일 팝업 엶

### graph
- 런처에서 그래프 버튼을 누르면 실행
- 내장 함수
  - onGraphPopup: 런처에서 그래프 버튼을 누르면 실행되는 함수
  - drawGraph: 받은 데이터에 따라 그래프를 그림
  - getData: REST API에서 데이터를 가져와 시군별 병원의 개수를 셈
  - mouseClicked: 마우스 좌표를 이용해 선택한 시군 정보를 알려줌
  - onMapPopup: 지도 팝업을 열고, 선택한 시군 내에 있는 병원(지도 정보가 포함된 병원에 한해) 위치 출력
  - getStr: 유틸리티 함수

### link
- 런처에서 링크 버튼을 누르면 실행되는 모듈입니다.

- 내장 함수
  - onLogo: 로고 버튼을 누르면 해당 프로젝트의 깃허브로 연결
  - onNaverLink: 네이버 로고 버튼을 누르면 해당 병원의 네이버 검색 결과로 연결
  - onGoogleLink: 구글 로고 버튼을 누르면 해당 병원의 구글 검색 결과로 연결
  - onNaverMapLink: 네이버 지도 버튼을 누르면 해당 병원의 네이버 지도 검색 결과로 연결

### map
- 런처에서 지도 버튼을 누르면 실행되는 모듈입니다.
- tkintermapview 모듈을 이용해 팝업에 지도를 그립니다.
- 내장 함수
  - onMapPopup: 선택한 병원의 지도를 보여주는 팝업을 엶
  - onSearch: 새 주소에 마커 추가
  - onHospital: 원래 병원 위치로 이동
  - onSat: 지도를 위성 지도로 변경
  - add_marker_event:마우스 우클릭으로 마커를 추가

### telegram
- 런처에서 텔레그램 버튼을 누르면 실행되는 모듈입니다.
- 내장 함수
  - sendSelectedInfo: 선택된 병원의 정보를 텔레그램으로 보냄

### telegram_bot
- **텔레그램 메인 모듈**입니다.
- 데이터를 수집, 처리하고 메시지를 보내는 noti 파트와 명령어에 반응하는 teller part로 구성되어 있습니다.

### server
- 모듈 간 데이터의 공유를 돕는 모듈입니다.
- 내장 함수를 가지고 있지 않습니다.
- 각 모듈에서 단순히 server를 import하면 필요한 정보를 제공받을 수 있습니다.

## 유의사항
### 1. 설치 후 **font** 폴더 내의 폰트를 모두 설치하는 것을 권고합니다.
미설치 시, 미관상 좋지 않거나 pack으로 생성된 GUI의 규격이 맞지 않을 가능성이 있습니다.
### 2. book_mark 모듈은 C/C++ 연동을 사용합니다.
- 해당 프로그램의 북마크 기능의 경우, C/C++ 연동이 되어있습니다.
- 다음과 같이, 입력된 문자열(한/영 혼합)의 문자 개수를 세어 반환하는 코드가 포함되어 있습니다.
```c
static PyObject* cLink_strlen(PyObject* self, PyObject* args) {
	char* str;

	if (!PyArg_ParseTuple(args, "s", &str))
		return NULL;

    int size = 0;
    for (int i = 0;; i++){
        if (str[i] & 0x80){
            size++;
            i += 2;
        }
        else if (str[i] == '\0') break;
        else                  
            size++;
    } 
	return Py_BuildValue("i", size);
}
```
|연동 시 알림 내용|미연동 시 알림 내용|
|--|--|
|![withSave](https://user-images.githubusercontent.com/89962345/173222002-968f4e3b-9b8c-4562-92b3-ea9ad6229eb8.png)|![withoutSave](https://user-images.githubusercontent.com/89962345/173222006-fb4e537d-955a-4e5a-81a6-be786e721e81.png)|

### 3. 메일보내기 기능은 지메일만 가능합니다.
- 수신 이메일 주소가 지메일인 경우만 메일을 보낼 수 있습니다.
- 이메일이 오지 않았다면, 스팸 메일함을 확인해주십시오. 간혹 메일이 스팸으로 처리되는 경우가 있습니다.

## 발표 영상
- [기획 발표](https://www.youtube.com/watch?v=B3Ki9xvumqw)
- [중간 발표](https://youtu.be/fD1uGRC4z8g)
- [최종 발표](https://youtu.be/TA53IUPUEog)














 
