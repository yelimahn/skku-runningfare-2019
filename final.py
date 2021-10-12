from tkinter import *

w=Tk()
w.title('웅앵 퍼스널컬러 진단테스트')
w.geometry('800x400')

spring=0
summer=0
fall=0
winter=0

spextra='신록이나 컬러풀한 꽃들의 산뜻발랄한 이미지.\n따뜻한 계열의 옐로베이스로 브라이트 톤이 어울리는 타입!'
suextra='여름의 햇볕이 물에 반사한 스모키한 이미지.\n블루 베이스로 파스텔, 소프트 톤이 어울리는 타입!'
faextra='가을의 낙엽, 과실, 자연의 나무들의 리치한 이미지.\n옐로 베이스로 깊고 수수하고 풍성한 칼라가 어울리는 타입!'
wiextra='순백의 눈으로 뒤덮인 설산의 차갑지만 포근한 이미지.\n차가운 계열의 블루 베이스로,\n무채색, 비비드톤, 콘트라스트 감이 있는 컬러가 어울리는 타입!'
neextra='웜톤과 쿨톤을 모두 가지고 있는 축복받은 톤.\n베스트를 찾기엔 어려워도 워스트는 없는, 사계절의 요정!'

spring1=PhotoImage(file='1-1.png')
summer1=PhotoImage(file='1-2.png')
fall1=PhotoImage(file='1-3.png')
winter1=PhotoImage(file='1-4.png')

spring2=PhotoImage(file='2-1.png')
summer2=PhotoImage(file='2-2.png')
fall2=PhotoImage(file='2-3.png')
winter2=PhotoImage(file='2-4.png')

spring3=PhotoImage(file='3-1.png')
summer3=PhotoImage(file='3-2.png')
fall3=PhotoImage(file='3-3.png')
winter3=PhotoImage(file='3-4.png')

spring4=PhotoImage(file='4-1.png')
summer4=PhotoImage(file='4-2.png')
fall4=PhotoImage(file='4-3.png')
winter4=PhotoImage(file='4-4.png')

spring5=PhotoImage(file='5-1.png')
summer5=PhotoImage(file='5-2.png')
fall5=PhotoImage(file='5-3.png')
winter5=PhotoImage(file='5-4.png')

def next1():
    label1.config(text='핑크 색상의 립스틱과 오렌지 색상의 립스틱 중\n어떤 것을 발랐을 때 피부가 더 화사해 보이나요?')
    label2.config(text='')
    label3.config(text='')
    btn1.config(text='핑크',font=('DX영화자막 M',20),bg='pink',command=next2)
    btn2.config(text='오렌지',font=('DX영화자막 M',20),bg='orange',command=next3)

        
def next2():
    label1.config(text='흰 A4용지를 얼굴에 비춰보세요.\n분홍/푸른 빛이 도나요? 아니면 초록/노란 빛이 도나요?')
    btn1.config(text='분홍/푸른빛',font=('DX영화자막 M',20),bg='skyblue',command=next4)
    btn2.config(text='초록/노란빛',font=('DX영화자막 M',20),bg='yellow',command=next5)
   
def next3():
    label1.config(text='흰 A4용지를 얼굴에 비춰보세요.\n분홍/푸른 빛이 도나요? 아니면 초록/노란 빛이 도나요?')
    btn1.config(text='분홍/푸른빛',font=('DX영화자막 M',20),bg='blue',command=next6)
    btn2.config(text='초록/노란빛',font=('DX영화자막 M',20),bg='yellow',command=next7)


def next4():
    label1.config(text='골드 색상의 액세서리와 실버 색상의 액세서리 중\n무엇이 더 잘 어울리나요?')
    btn1.config(text='골드',font=('DX영화자막 M',20),bg='gold',command=next8)
    btn2.config(text='실버',font=('DX영화자막 M',20),bg='silver',command=next9)
    
    
def next5():
    label1.config(text='골드 색상의 액세서리와 실버 색상의 액세서리 중\n무엇이 더 잘 어울리나요?')
    btn1.config(text='골드',font=('DX영화자막 M',20),bg='gold',command=next10)
    btn2.config(text='실버',font=('DX영화자막 M',20),bg='silver',command=next11)

    
def next6():
    label1.config(text='골드 색상의 액세서리와 실버 색상의 액세서리 중\n무엇이 더 잘 어울리나요?')
    btn1.config(text='골드',font=('DX영화자막 M',20),bg='gold',command=next12)
    btn2.config(text='실버',font=('DX영화자막 M',20),bg='silver',command=next13)


def next7():
    label1.config(text='골드 색상의 액세서리와 실버 색상의 액세서리 중\n무엇이 더 잘 어울리나요?')
    btn1.config(text='골드',font=('DX영화자막 M',20),bg='gold',command=next14)
    btn2.config(text='실버',font=('DX영화자막 M',20),bg='silver',command=next15)


def next8():
    btn1.destroy()
    btn2.destroy()
    label1.destroy()
    label2.destroy()
    global tone1
    tone1='쿨'
    choi.pack(pady=5)
    btn0.pack(pady=5)

def next9():
    btn1.destroy()
    btn2.destroy()
    label1.destroy()
    label2.destroy()
    global tone1
    tone1='쿨'
    choi.pack(pady=5)
    btn0.pack(pady=5)

def next10():
    btn1.destroy()
    btn2.destroy()
    label1.destroy()
    label2.destroy()
    global tone1
    tone1='웜'
    choi.pack(pady=5)
    btn0.pack(pady=5)

def next11():
    btn1.destroy()
    btn2.destroy()
    label1.destroy()
    label2.destroy()
    global tone1
    tone1='쿨'
    choi.pack(pady=5)
    btn0.pack(pady=5)

def next12():
    btn1.destroy()
    btn2.destroy()
    label1.destroy()
    label2.destroy()
    global tone1
    tone1='웜'
    choi.pack(pady=5)
    btn0.pack(pady=5)
    

def next13():
    btn1.destroy()
    btn2.destroy()
    label1.destroy()
    label2.destroy()
    global tone1
    tone1='쿨'
    choi.pack(pady=5)
    btn0.pack(pady=5)

def next14():
    btn1.destroy()
    btn2.destroy()
    label1.destroy()
    label2.destroy()
    global tone1
    tone1='웜'
    choi.pack(pady=5)
    btn0.pack(pady=5)

def next15():
    btn1.destroy()
    btn2.destroy()
    label1.destroy()
    label2.destroy()
    global tone1
    tone1='웜'
    choi.pack(pady=5)
    btn0.pack(pady=5)

def start():
    btn_spr1.pack(pady=5,side=LEFT)
    btn_sum1.pack(pady=5,side=LEFT)
    btn_fal1.pack(pady=5,side=LEFT)
    btn_win1.pack(pady=5,side=LEFT)
    btn0.destroy()

def spr1():
    btn_spr1.destroy()
    btn_sum1.destroy()
    btn_fal1.destroy()
    btn_win1.destroy()
    global spring
    spring=spring+1
    btn_spr2.pack(pady=5,side=LEFT)
    btn_sum2.pack(pady=5,side=LEFT)
    btn_fal2.pack(pady=5,side=LEFT)
    btn_win2.pack(pady=5,side=LEFT)
    

def sum1():
    btn_spr1.destroy()
    btn_sum1.destroy()
    btn_fal1.destroy()
    btn_win1.destroy()
    global summer
    summer=summer+1
    btn_spr2.pack(pady=5,side=LEFT)
    btn_sum2.pack(pady=5,side=LEFT)
    btn_fal2.pack(pady=5,side=LEFT)
    btn_win2.pack(pady=5,side=LEFT)


def aut1():
    btn_spr1.destroy()
    btn_sum1.destroy()
    btn_fal1.destroy()
    btn_win1.destroy()
    global fall
    fall=fall+1
    btn_spr2.pack(pady=5,side=LEFT)
    btn_sum2.pack(pady=5,side=LEFT)
    btn_fal2.pack(pady=5,side=LEFT)
    btn_win2.pack(pady=5,side=LEFT)

def win1():
    btn_spr1.destroy()
    btn_sum1.destroy()
    btn_fal1.destroy()
    btn_win1.destroy()
    global winter
    winter=winter+1
    btn_spr2.pack(pady=5,side=LEFT)
    btn_sum2.pack(pady=5,side=LEFT)
    btn_fal2.pack(pady=5,side=LEFT)
    btn_win2.pack(pady=5,side=LEFT)

def spr2():
    btn_spr2.destroy()
    btn_sum2.destroy()
    btn_fal2.destroy()
    btn_win2.destroy()
    global spring
    spring=spring+1
    btn_spr3.pack(pady=5,side=LEFT)
    btn_sum3.pack(pady=5,side=LEFT)
    btn_fal3.pack(pady=5,side=LEFT)
    btn_win3.pack(pady=5,side=LEFT)

def sum2():
    btn_spr2.destroy()
    btn_sum2.destroy()
    btn_fal2.destroy()
    btn_win2.destroy()
    global summer
    summer+=1
    btn_spr3.pack(pady=5,side=LEFT)
    btn_sum3.pack(pady=5,side=LEFT)
    btn_fal3.pack(pady=5,side=LEFT)
    btn_win3.pack(pady=5,side=LEFT)


def aut2():
    btn_spr2.destroy()
    btn_sum2.destroy()
    btn_fal2.destroy()
    btn_win2.destroy()
    global fall
    fall+=1
    btn_spr3.pack(pady=5,side=LEFT)
    btn_sum3.pack(pady=5,side=LEFT)
    btn_fal3.pack(pady=5,side=LEFT)
    btn_win3.pack(pady=5,side=LEFT)

def win2():
    btn_spr2.destroy()
    btn_sum2.destroy()
    btn_fal2.destroy()
    btn_win2.destroy()
    global winter
    winter+=1
    btn_spr3.pack(pady=5,side=LEFT)
    btn_sum3.pack(pady=5,side=LEFT)
    btn_fal3.pack(pady=5,side=LEFT)
    btn_win3.pack(pady=5,side=LEFT)

def spr3():
    btn_spr3.destroy()
    btn_sum3.destroy()
    btn_fal3.destroy()
    btn_win3.destroy()
    global spring
    spring=spring+1
    btn_spr4.pack(pady=5,side=LEFT)
    btn_sum4.pack(pady=5,side=LEFT)
    btn_fal4.pack(pady=5,side=LEFT)
    btn_win4.pack(pady=5,side=LEFT)

def sum3():
    btn_spr3.destroy()
    btn_sum3.destroy()
    btn_fal3.destroy()
    btn_win3.destroy()
    global summer
    summer+=1
    btn_spr4.pack(pady=5,side=LEFT)
    btn_sum4.pack(pady=5,side=LEFT)
    btn_fal4.pack(pady=5,side=LEFT)
    btn_win4.pack(pady=5,side=LEFT)


def aut3():
    btn_spr3.destroy()
    btn_sum3.destroy()
    btn_fal3.destroy()
    btn_win3.destroy()
    global fall
    fall+=1
    btn_spr4.pack(pady=5,side=LEFT)
    btn_sum4.pack(pady=5,side=LEFT)
    btn_fal4.pack(pady=5,side=LEFT)
    btn_win4.pack(pady=5,side=LEFT)

def win3():
    btn_spr3.destroy()
    btn_sum3.destroy()
    btn_fal3.destroy()
    btn_win3.destroy()
    global winter
    winter+=1
    btn_spr4.pack(pady=5,side=LEFT)
    btn_sum4.pack(pady=5,side=LEFT)
    btn_fal4.pack(pady=5,side=LEFT)
    btn_win4.pack(pady=5,side=LEFT)

def spr4():
    btn_spr4.destroy()
    btn_sum4.destroy()
    btn_fal4.destroy()
    btn_win4.destroy()
    global spring
    spring=spring+1
    btn_spr5.pack(pady=5,side=LEFT)
    btn_sum5.pack(pady=5,side=LEFT)
    btn_fal5.pack(pady=5,side=LEFT)
    btn_win5.pack(pady=5,side=LEFT)

def sum4():
    btn_spr4.destroy()
    btn_sum4.destroy()
    btn_fal4.destroy()
    btn_win4.destroy()
    global summer
    summer+=1
    btn_spr5.pack(pady=5,side=LEFT)
    btn_sum5.pack(pady=5,side=LEFT)
    btn_fal5.pack(pady=5,side=LEFT)
    btn_win5.pack(pady=5,side=LEFT)


def aut4():
    btn_spr4.destroy()
    btn_sum4.destroy()
    btn_fal4.destroy()
    btn_win4.destroy()
    global fall
    fall+=1
    btn_spr5.pack(pady=5,side=LEFT)
    btn_sum5.pack(pady=5,side=LEFT)
    btn_fal5.pack(pady=5,side=LEFT)
    btn_win5.pack(pady=5,side=LEFT)

def win4():
    btn_spr4.destroy()
    btn_sum4.destroy()
    btn_fal4.destroy()
    btn_win4.destroy()
    global winter
    winter+=1
    btn_spr5.pack(pady=5,side=LEFT)
    btn_sum5.pack(pady=5,side=LEFT)
    btn_fal5.pack(pady=5,side=LEFT)
    btn_win5.pack(pady=5,side=LEFT)

def spr5():
    btn_spr5.destroy()
    btn_sum5.destroy()
    btn_fal5.destroy()
    btn_win5.destroy()
    global spring
    global extra
    spring=spring+1
    if spring>summer and spring>fall and spring>winter:
        tone2='봄'
        extra=spextra
    elif summer>spring and summer>fall and summer>winter:
        tone2='여름'
        extra=suextra
    elif fall>spring and fall>summer and fall>winter:
        tone2='가을'
        extra=faextra
    elif winter>spring and winter>fall and winter>summer:
        tone2='겨울'
        extra=wiextra
    else:
        tone2='뉴트럴'
        extra=neextra
    end1=Label(w,text="당신은 %s %s톤입니다" %(tone2,tone1),font=('DX영화자막 M',30))
    end2=Label(w,text="%s" %extra,font=('DX영화자막 M',20))
    end1.pack(pady=5)
    end2.pack(pady=5)
    choi.destroy()

def sum5():
    btn_spr5.destroy()
    btn_sum5.destroy()
    btn_fal5.destroy()
    btn_win5.destroy()
    global summer
    global extra
    summer+=1
    if spring>summer and spring>fall and spring>winter:
        tone2='봄'
        extra=spextra
    elif summer>spring and summer>fall and summer>winter:
        tone2='여름'
        extra=suextra
    elif fall>spring and fall>summer and fall>winter:
        tone2='가을'
        extra=faextra
    elif winter>spring and winter>fall and winter>summer:
        tone2='겨울'
        extra=wiextra
    else:
        tone2='뉴트럴'
        extra=neextra
    end1=Label(w,text="당신은 %s %s톤입니다" %(tone2,tone1),font=('DX영화자막 M',30))
    end2=Label(w,text="%s" %extra,font=('DX영화자막 M',20))
    end1.pack(pady=5)
    end2.pack(pady=5)
    choi.destroy()

def aut5():
    btn_spr5.destroy()
    btn_sum5.destroy()
    btn_fal5.destroy()
    btn_win5.destroy()
    global fall
    global extra
    fall+=1
    if spring>summer and spring>fall and spring>winter:
        tone2='봄'
        extra=spextra
    elif summer>spring and summer>fall and summer>winter:
        tone2='여름'
        extra=suextra
    elif fall>spring and fall>summer and fall>winter:
        tone2='가을'
        extra=faextra
    elif winter>spring and winter>fall and winter>summer:
        tone2='겨울'
        extra=wiextra
    else:
        tone2='뉴트럴'
        extra=neextra
    end1=Label(w,text="당신은 %s %s톤입니다" %(tone2,tone1),font=('DX영화자막 M',30))
    end2=Label(w,text="%s" %extra,font=('DX영화자막 M',20))
    end1.pack(pady=5)
    end2.pack(pady=5)
    choi.destroy()

def win5():
    btn_spr5.destroy()
    btn_sum5.destroy()
    btn_fal5.destroy()
    btn_win5.destroy()
    global winter
    global extra
    winter+=1
    if spring>summer and spring>fall and spring>winter:
        tone2='봄'
        extra=spextra
    elif summer>spring and summer>fall and summer>winter:
        tone2='여름'
        extra=suextra
    elif fall>spring and fall>summer and fall>winter:
        tone2='가을'
        extra=faextra
    elif winter>spring and winter>fall and winter>summer:
        tone2='겨울'
        extra=wiextra
    else:
        tone2='뉴트럴'
        extra=neextra
    end1=Label(w,text="당신은 %s %s톤입니다" %(tone2,tone1),font=('DX영화자막 M',30))
    end2=Label(w,text="%s" %extra,font=('DX영화자막 M',20))
    end1.pack(pady=5)
    end2.pack(pady=5)
    choi.destroy()

label1=Label(w,text='웅앵 퍼스널컬러 진단테스트를 시작하겠습니다.',font=('DX영화자막 M',20))
label2=Label(w,text='본인과 가장 가깝다고 생각되는 항목을 선택해주십시오.',font=('DX영화자막 M',20))
label3=Label(w,text='시작하려면 아래 시작버튼을 눌러주세요.',font=('DX영화자막 M',20))
btn1=Button(w,text='시작',font=('DX영화자막 M',20),bg='gray', command=next1)
btn2=Button(w,text='안할래요',font=('DX영화자막 M',20),bg='gray', command=quit)

choi=Label(w,text='본인과 가장 어울리는 색깔을 클릭해주세요.',font=('DX영화자막 M',20))
btn0=Button(w,text='시작',font=('DX영화자막 M',20),bg='gray',fg='white',command=start)

btn_spr1=Button(w,image=spring1,command=spr1)
btn_sum1=Button(w,image=summer1,command=sum1)
btn_fal1=Button(w,image=fall1,command=aut1)
btn_win1=Button(w,image=winter1,command=win1)

btn_spr2=Button(w,image=spring2,command=spr2)
btn_sum2=Button(w,image=summer2,command=sum2)
btn_fal2=Button(w,image=fall2,command=aut2)
btn_win2=Button(w,image=winter2,command=win2)

btn_spr3=Button(w,image=spring3,command=spr3)
btn_sum3=Button(w,image=summer3,command=sum3)
btn_fal3=Button(w,image=fall3,command=aut3)
btn_win3=Button(w,image=winter3,command=win3)

btn_spr4=Button(w,image=spring4,command=spr4)
btn_sum4=Button(w,image=summer4,command=sum4)
btn_fal4=Button(w,image=fall4,command=aut4)
btn_win4=Button(w,image=winter4,command=win4)

btn_spr5=Button(w,image=spring5,command=spr5)
btn_sum5=Button(w,image=summer5,command=sum5)
btn_fal5=Button(w,image=fall5,command=aut5)
btn_win5=Button(w,image=winter5,command=win5)

label1.pack()
label2.pack()
label3.pack()
btn1.pack()
btn2.pack()

w.mainloop()
