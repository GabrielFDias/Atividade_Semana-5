import datetime
from datetime import date

class MyCalendar:
    def __init__(self, dt1=None, dt2=None, dt3=None, tamanho_lista=None):
        self.datas = []
        self.dt1=dt1
        self.dt2=dt2
        self.dt3=dt3
        self.tamanho_lista=tamanho_lista
        
        if type(dt1) == date:
            self.datas.append(dt1)
        else:
            try:
                dt1 = datetime.datetime.strptime(dt1, '%d/%m/%Y')
                self.datas.append(dt1)
            except:
                pass

        if type(dt2) == date:
            self.datas.append(dt2)
        else:
            try:
                dt2 = datetime.datetime.strptime(dt2, '%d/%m/%Y')
                self.datas.append(dt2)
            except:
                pass

        if type(dt3) == date:
            self.datas.append(dt3)
        else:
            try:
                dt3 = datetime.datetime.strptime(dt3, '%d/%m/%Y')
                self.datas.append(dt3)
            except:
                pass


    def add_holiday(self, dt3=None, dt4=None): 
        if dt3 in self.datas:
            return
        
        if dt4 in self.datas:
            return

        try:
            if datetime.datetime.strptime(dt3, '%d/%m/%Y') in self.datas:
                return
        except:
            pass
        
        try:
            if datetime.datetime.strptime(dt4, '%d/%m/%Y') in self.datas:
                return
        except:
            pass

        if type(dt3) == date:
            self.datas.append(dt3) 
        else:
            try:
                dt3 = datetime.datetime.strptime(dt3, '%d/%m/%Y')
                self.datas.append(dt3)
            except:
                pass

        if type(dt4) == date:
            self.datas.append(dt4)
        else:
            try:
                dt4 = datetime.datetime.strptime(dt4, '%d/%m/%Y')
                self.datas.append(dt4)
            except:
                pass                           
                         
            
    def check_holiday(self, dt=None):
        self.dt1='15/01/2021'
        self.dt2='15/02/2021'
        self.dt3=date(2021, 2, 15)
        self.dt4=date(2021, 2, 15)  
        self.holidays = [self.dt1,self.dt2,self.dt3,self.dt4]
        
        if dt in self.holidays:
            return True
        else:
            return False







                
        

        
        
        
