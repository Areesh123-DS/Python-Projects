

from datetime import datetime
def date():
    x=datetime.now()
    z=x.strftime('%d-%b-%Y')#%date,%month,%Year
    return z

class Address:
    def __init__(self,hn,stno,area,city,country):
        self.__houseno=hn
        self.__streetno=stno
        self.__city=city
        self.__country=country
        self.__area=area
    def __str__(self):
        vstr=" "
        vstr=str(self.__houseno)
        vstr+="-"
        vstr+=str(self.__streetno)
        vstr+="-"
        vstr+=str(self.__area)
        vstr+=","
        vstr+=str(self.__city)
        vstr+=","
        vstr+=str(self.__country)
        return vstr
    @property
    def HnNo(self):
        return self.__houseno
    @HnNo.setter
    def HnNo(self,d):
        self.__houseno=d
    @property
    def StNo(self):
        return self.__street
    @StNo.setter
    def street(self,d):
        self.__street=d
    @property
    def City(self):
        return self.__city
    @City.setter
    def City(self,d):
        self.__city=d
    @property
    def Country(self):
        return self.__country
    @Country.setter
    def Country(self,d):
        self.__country=d
    @property
    def Area(self):
        return self.__area
    @Area.setter
    def Area(self,d):
        self.__area=d
class Name:
    def __init__(self,fn,ln):
        self.__firstname=fn
        self.__lastname=ln
    def __str__(self):
        vstr=" "
        vstr=str(self.__firstname)
        vstr+=" "
        vstr+=str(self.__lastname)
        return vstr

    @property
    def fn(self):
        return self.__firstname
    @fn.setter
    def fn(self,d):
        self.__firstname=d
    @property
    def ln(self):
        return self.__lastname
    @ln.setter
    def ln(self,d):
        self.__lastname=d

class BillItem:
    amount=0
    def __init__(self,qt,particular,rt):
        self.__quantity=qt
        self.__particular=particular
        self.__rate=rt
        BillItem.amount=self.__quantity*self.__rate
    def __str__(self):
        BillItem.amount=self.__quantity*self.__rate
        return f"{self.__particular}              {self.__rate}          {self.__quantity}          {BillItem.amount}"

    @property
    def Qt(self):
        return self.__quantity
    @Qt.setter
    def Qt(self,q):
        self.__quantity=q
    @property
    def Prt(self):
        return self.__particular
    @Prt.setter
    def Prt(self,g):
        self.__particular=g
    @property
    def Rt(self):
        return self.__rate
    @Rt.setter
    def Rt(self,g):
        self.__rate=g

class Bill:
    __serial_no=0
    def __init__(self,d,n,ad,no,itm,total=0):
        self.__date=d
        self.__name=n
        self.__address=ad
        self.__item=[]
        self.__item.extend(itm)
        self.__total=0

        Bill.__serial_no+=1
    def __str__(self):

        rs=f"MOBILO\nMobile City\nDeals in all kinds of Mobile sets & Accessories\nCell No: 0321-0000000\nCASHMEMO\nNo:_{Bill.getNo()}_\nDate:__{self.__date}__\nCustomer Name:\n__{self.__name}__\nCustomer Address:\n__{self.__address}__\nParticulars     Rate    Quantity     Amount "
        for itm in self.__item:
            rs+='\n'+str(itm)
        return rs + "\n"+f"Total : __{self.total_amount()}__"+"\n"+"Signature___" "\n"+"Address: Basement # 2, Allahwala Plaza, Markaz K8, Islamabad"
    def total_amount(self):
        total = 0
        for itm in self.__item:
            total += BillItem.amount
        return total
    def __del__(self):
        Bill.__serial_no-=1
    def getNo():
      return Bill.__serial_no
    getNo = staticmethod(getNo)


def main():
    n=Name(input("Enter Firstname: "),input("Enter Lastname: "))
    a=Address(int(input("Enter Houseno: ")),int(input("Enter Street no.: ")),input("Enter Area: "),input("Enter City: "),input("Enter Country: "))
    no_items = int(input("How many items customer wants?: "))
    items = []
    for i in range(no_items):
        p = input(f"Particulars : ")
        r = int(input(f"Rate for item{i+1} : "))
        q = int(input(f"Quantity for item{i+1}: "))
        items.append(BillItem(q,p,r))

    n1=Bill.getNo()
    t=Bill(date(),n,a,n1,items,0)
    s=t.total_amount()
    del(t)
    m=Bill(date(),n,a,n1,items,s)
    print(f"{m}")
main()
