import mc_pgzrun
import random

WIDTH=800
HEIGHT=450
suan=[]
state=0
start=Actor('start')
start.x=400
start.y=370
view_now=Actor('view_now')
view_now.x=400
view_now.y=400

ind=1
coppers=[]
for i in range(3):
    v=random.randint(1,2)
    if v==1:
        co=Actor('front')
    if v==2:
        co=Actor('back')
    co.x=ind*WIDTH/4
    co.y=200
    coppers.append(co)
    ind+=1

def draw():
    global state,suan
    screen.blit('table',(0,0))
    if state==0:
        screen.draw.text('智能算命v1.0.0\n2022/7/24-刘文景\n点击开始即可开始',(300,10),fontname='msyh.ttc',color='black')
        start.draw()
    if state==1:
        for i in coppers:
            i.draw()
        view_now.draw()
        screen.draw.text('正在运行.\n洗手，诚心诚意\n心中默念要占卜的事情',(300,10),fontname='msyh.ttc',color='black')
    if state==2:
        for g in suan:
            g.draw()
        start.draw()
            
def on_mouse_down(pos):
    global state,suan,start,view_now,restart
    if start.collidepoint(pos)and state==0:
        state=1
        start.image='restart'
    elif start.collidepoint(pos)and state==2:
        state=1
    elif view_now.collidepoint(pos) and state==1:
        m=0
        n=0
        c=''
        num=[]
        for x in range(6):
            for i in range(3):
                b=random.randint(0,1)
                c+=str(b)
            for y in c:
                if y=='1':
                    n+=1
            if n==1 or n==0:
                m=1
            elif n==2 or n==3:
                m=0
            num.append(m)
            c=''
            n=0
        index=0
        for i in range(6):
            f=Actor(str(num[index]))
            f.x=400
            f.y=300-50*index
            suan.append(f)
            index+=1
        state=2

def update():
    global state
    if state==1:
        for i in coppers:
            v=random.randint(1,2)
            if v==1:
                i.image='front'
            if v==2:
                i.image='back'

mc_pgzrun.go()








