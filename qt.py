hurt=[" yanjiaochuxie"," biliangkaihua"," koutubaimuo"
       ," dadaozaidi"," yiquandafei"]

class qt:

    def __init__(self,a):
        
        self.own=0
        self.blood=0
        self.name=a
        
    def restart(self):
        
        self.own=0
        self.blood=0
        
    def returnblood(self):
        
        if (not self.name.st) and self.blood:
            self.blood=self.blood-1
        
    def kill(self,m):
        
        if self.own and self.name.st and self.blood<4 and m.st:
             m.qt.killed()
             
    def stand(self):
        
        if self.blood==4 and self.name.st==1:
            self.blood=3

    def killed(self):
        
            print('killed',self.name.name)
            
            if self.blood==4:
                print(hurt[4])
                print(self.name.name,'die')
                '''
                raise Die()
                '''
                self.name.killed()
                
            else:
                print(hurt[self.blood])
                self.blood=self.blood+1

