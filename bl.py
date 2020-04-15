class bl:
    def __init__(self,a):
        
        self.can=1
        self.bl=0
        self.blood=0
        self.name=a
        
    def ca(self,a):
        if self.bl and self.name.st and a.st:
            a.bl.blood=1
            self.bl -= 1
            print('ca'+a.name)
            
    def ba(self,a):
        if a.bl.blood==1 and self.can and self.name.st and a.st:
            self.bl +=1
            a.bl.blood=2
            print('ba'+a.name)
            
    def xing(self,a):
        if self.bl and self.can and self.name.st and a.st and a.bl.blood==2:
            self.bl -= 1
            print('xing'+a.name)
            a.die=1
            
    def restart(self):
        self.bl=0
        self.blood=0

