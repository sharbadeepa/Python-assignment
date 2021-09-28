import re
def Password(pas):
    passwd = 'Geek12'
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
      
    # compiling regex
    pat = re.compile(reg)
      
    # searching regex                 
    mat = re.search(pat, passwd)
      
    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")
if __name__ == '__main__':
    Password('passwd')


def isomorphic(a,b):
    iso_s = {}
    iso_t = {}
   
    for i, value in enumerate(a):
        iso_s[value]= iso_s.get(value,[]) + [i]
    for j, value in enumerate(b):
        iso_t[value]= iso_t.get(value,[]) + [j]
    
    if sorted(iso_s.values()) == sorted(iso_t.values()):
       
        return True
    else:
        return False
isomorphic('bar', 'foo')
isomorphic('add','egg')

# second
def number(n):
    num=int(n/3)
    x=[]
    div=[]
    for i in range(1,num):
        b=2**i
        x.append(b)
        if b > num :
            break
    print(x)
    for j in x:
        if n%j==0:
            div.append(j)
            print(div)
            print(len(div))
print(number(n=int(input('Enter the Number'))))

def list_new(a):
    
    import numpy as np
    # a = [[1,2,3],[2,3,4],[4,5,6]]
    print(type(a))
    new = np.array(a)
    x_tanspos = np.transpose(new)
    list_x_tanspos = x_tanspos.tolist()
    print(type(list_x_tanspos))
    if list_x_tanspos == sorted(list_x_tanspos):
    print("Everyone can see the screen")
    else:
    print("Everyone cannot see the screen")



list_new([[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 10, 4, 4],
[6, 6, 7, 6, 5, 5]])

   


from datetime import datetime
def datenew(dates):
    dates = ["23 Jun 2018", "2 Dec 2017", "11 Jun 2018", "01 Jan 2019", "10 Jul 2016", "01 Jan 2007"]
    for i in range(len(dates)):
        print(dates[i])
if __name__ == '__main__':
    dates = ["23 Jun 2018", "2 Dec 2017", "11 Jun 2018", 
            "01 Jan 2019", "10 Jul 2016", "01 Jan 2007"]  
    dates.sort(key = lambda date:datetime.strptime(date, "%d %b %Y"))
    print(dates)
    datenew(dates)



class Solution:
    def strWithout3a3b(self, A, B):
    ans = []

    while A or B:
    if len(ans) >= 2 and ans[-1] == ans[-2]:
    writeA = ans[-1] == 'b'
    else:
    writeA = A >= B

    if writeA:
    A -= 1
    ans.append('a')
    else:
    B -= 1
    ans.append('b')

    return "".join(ans)
S1 = Solution()
print(S1.strWithout3a3b(A=int(input("ENTER THE NUMBER ")),B=int(input("Enter the number "))))

def num_split(num):
    num = str(num)

    num = [c for c in num]
    num = num[::-1]
    num_lis = []
    f = 1
    for i in range(len(num)):
        num_lis.append(int(num[i])*f)
        f *= 10
        print(num_lis[::-1])




num_split(599)

