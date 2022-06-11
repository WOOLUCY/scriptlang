import pickle
hospitals = ['가나병원', '다라병원', '마바병원']

dic = {'아무병원':'반악ㅇㄹ저배거ㅗㅁㄹ', '노래병원':'ㅂㅈㄷㄼㅈㅇ'}

f = open('test', 'wb') #pickle 사용을 위해 바이너리 쓰기 파일 오픈
pickle.dump(dic, f) #리스트 객체를 파일로 dump
f.close()

f = open('test', 'rb') #pickle 사용을 위해 바이너리 읽기 파일 오픈
dic = pickle.load(f) #파일에서 리스트 load
f.close()

print(dic['아무병원'])