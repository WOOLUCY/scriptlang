# 어디병원: Where The Hospital
![logo](https://user-images.githubusercontent.com/89962345/173218210-ca651684-be63-4a68-974b-10cf2c18b40a.png)
#### 한국공학대학교 게임공학과 2022학년도 1학기 스크립트 언어 텀프로젝트입니다.

## 목차
- [프로그램 개요](#프로그램-개요)
- [사용한 API](#사용한-api)
- [프로그램 기능](#프로그램-기능)
- 프로그램 모듈
- 권고사항
- 기타

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
### 1. OpenAPI 연동 검색 
![search](https://user-images.githubusercontent.com/89962345/173219294-05f6cf11-b9f7-4839-b74f-9b3e2ee25f87.png)
- **시군별, 진료과목별** 필터 검색이 가능합니다.
- **병원명** 을 입력해 원하는 병원을 검색할 수 있습니다.
- 검색할때마다 **REST API** 이용합니다.
- **필터 리셋** 기능을 버튼으로 지원합니다.

### 2. 병원 정보 출력
![show](https://user-images.githubusercontent.com/89962345/173219403-ba239528-ac8a-4df3-860f-c50a0c0f7606.png)
- 리스트에서 선택한 병원 정보 출력
- 병원 정보는 병원명, 의료기관종별명, 전화번호, 도로명 주소, 지번 주소, 진료 과목, 의료인수, 입원실수, 병상수를 포함합니다.

### 3. 링크
![link](https://user-images.githubusercontent.com/89962345/173219519-489d3d60-5e17-42fd-a274-6a154cae2c66.png)
- 선택한 병원의 검색결과 링크로 이동합니다.
- 구글 검색결과, 네이버 검색 결과, 네이버 지도 검색 결과를 지원합니다.

### 4. 북마크
![bookmark](https://user-images.githubusercontent.com/89962345/173219601-ed6258e9-33c9-40e1-9351-82186837c4ab.png)
- 선택한 병원을 북마크에 저장할 수 있습니다.
- 북마크에 저장할 때, 메모를 추가할 수 있습니다.
- 북마크에 저장한 병원을 다시 제거할 수 있습니다.
- 버튼 이미지로 해당 병원이 북마크에 포함되어있는지 확인할 수 있습니다.

|미포함 시|포함 시|
|-------|--------|
|![white_bookmark](https://user-images.githubusercontent.com/89962345/173219703-abad93c0-37f1-4c2c-9296-6389f844555d.png)|![bookmark](https://user-images.githubusercontent.com/89962345/173219704-b1a5c0c5-184d-4f1f-bdb4-e0eda3a8cd05.png)|







