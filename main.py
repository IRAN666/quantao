
import random
from yufa import yufa,plus
from qt import qt
from lj import lj
from bl import bl


hurt=[" yanjiaochuxie"," biliangkaihua"," koutubaimuo"
       ," dadaozaidi"," yiquandafei"]
place={}

class tk:
    def __init__(self,a):
        
        self.can=1
        self.tk=0
        self.blood=0
        self.name=a
        
    def gain(self):
        if self.can==1 and self.tk==0:
            self.tk=1
            self.name.xue+=1
            print('tk '+self.name.name)
    def duang(self,a):
        if self.tk and self.name.st and a.st:
            a.tk.blood+=1
            print('duang'+a.name)
            if a.tk.blood==3:
                a.killed()
            
            
    def restart(self):
        self.tk=0
        self.blood=0

class ren:
    
    def __init__(self,name):
        
        self.name=name
        self.jibie=1
        self.st=0
        self.qt=qt(self)
        self.lj=lj(self)
        self.bl=bl(self)
        self.tk=tk(self)
        self.wz=0
        self.die=0
        self.xue=2
        print("\n"*5)
        self.sjwz()

    def killed(self):

        if self.xue==1:
            self.die=1
        else:
            self.xue-=1
            self.restart()
    def sjwz(self):
        
        i=0
        while 1:
            if i in place.values() :
                i=i+1
            else:
                place[self]=i
                break
                
    def up(self):
        
        self.jibie=self.jibie+1
        if self.jibie==2:
            self.lj.can=1
        elif self.jibie==3:
            self.bl.can=1
        elif self.jibie==3:
            self.tk.can=1
        
        
    def restart(self):
        
        self.qt.restart()
        self.lj.restart()
        self.bl.restart()
        self.tk.restart()
        self.st=0
        self.sjwz()
        
    def re_up(self):
        
        if self.die:
            self.die=0
            self.restart()                        
        else:
            self.restart()
            self.up()
            print(self.name,'up')
    

    
    def inputbox(self):
        
        while 1:
            try:
                thing=input('please  '+self.name+'  input>')
                thing=yufa(thing)
                t=thing[0]
                r=thing[1]
                
                if t==101:
                    self.qt.kill(r)
                elif t==100 :
                    if not r.st:
                        r.qt.own=1
                        print('qt')
                elif t==-11 :
                    r.st=1
                    print('st')
                elif t==-21 :
                    r.st=0
                    print('xt')
                    self.sjwz()
                elif t==-31 :
                    self.wz=r.wz
                elif t==-32 :
                    self.sjwz()
                elif t==102:
                    r.qt.stand()
                elif t==103:
                    r.qt.returnblood()                    
                elif t==200:
                    r.lj.plus()
                elif t==201:
                    self.lj.kill(r)
                elif t==202:
                    self.lj.tou(r)
                elif t==300:
                    if self.bl.can and not r.st:
                        r.bl.bl=1
                        print('bl')
                elif t==301:
                    self.bl.ca(r)
                elif t==302:
                    self.bl.ba(r)
                elif t==303:
                    self.bl.xing(r)
                elif t==400:
                    self.tk.gain()
                elif t==401:
                    self.tk.duang(r)
                
                break
                
            except AttributeError:
                print('???')
                
    
def rand_a_or_b(m,n):
    
    
    if random.randint(1,10)>5:
        a.inputbox()
    else:
        b.inputbox()



while 1:
    one,two=input('> '),input('> ')
    if not input('not '+one+' and '+two+' ?'):
        break


a=ren(one)
b=ren(two)
plus(one,a)
plus(two,b)

while 1:
    
    rand_a_or_b(a,b)
    if a.die or b.die:
        print('somebody die')
        if a.die:
            print(a.name,'die')
        if b.die:
            print(b.name,'die')
        a.re_up()
        b.re_up()

    if input('not continue?'):
        break
print('0.1.1')
