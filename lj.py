
class lj:
    def __init__(self,a):
        
        self.can=0
        self.lj=0
        self.name=a
        
    def restart(self):
        
        self.lj=0
        
    def plus(self):
        
        if self.can and not (self.name.st):
            self.lj=self.lj+1
            print('you have',self.lj)
            
    def kill(self,a):
        
        if self.lj>2 and a.st and self.name.st and self.can:
            a.lj.killed()
            self.lj -=3
            
    def killed(self):
        
        self.name.die=1
    
    def tou(self,m):
        if m.lj.lj and not (m.st or self.name.st):
            self.lj += 1
            print(self.lj)
            m.lj.lj -= 1
