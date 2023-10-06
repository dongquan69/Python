#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

"""
import system
print("Python version:")
print(system.version)
print("Version info:")
print(system.version_info)
"""

'''
import datetime
now = datetime.datetime.now()
print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
'''

'''
from math import pi
bk = float(input("Nhap ban kinh hinh tron: "))
print("Dien tich hinh tron co ban kinh " + str(bk) + " la: " + str(pi*bk*bk))
'''

'''
ten = input("Nhap ten nguoi dung: ")
ho = input("Nhap ho nguoi dung: ")
print("Ho va ten nguoi dung: " + ho + " " + ten)
'''

'''
values = input("Nhap cac so cach nhau boi dau ,: ")
list = values.split(',')
tuple = tuple(list)
print("List: " + str(list))
print("Tuple: " + str(tuple))
'''

'''
filename = input("Nhap ten tep: ")
extention = filename.split('.')
print("Phan mo rong cua tep: " + repr(extention[-1]))
'''

'''
color_list = ["Red","Green","Blue","Black","Purple","Orange"]
print("%s ,%s" %(color_list[0], color_list[-1]))
'''

'''
exam_st_date = (12,12,2002)
print("Lich kiem tra: %d/%d/%d" %(exam_st_date[0],exam_st_date[1],exam_st_date[2]))
'''

'''
n=int(input("Nhap so nguyen n: "))
n1=int("%s" %(n))
n2=int("%s%s"%(n,n))
n3=int("%s%s%s" %(n,n,n))
print("Tong = " + str(n1+n2+n3))
'''

'''print(abs(-5))
print(abs.__doc__)'''

'''
import calendar
thang = int(input("Nhap thang: "))
nam = int(input("Nhap nam: "))
print(calendar.month(nam,thang))
'''

'''
print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
""")
'''

'''
from datetime import date
d1 = date(2014,7,2)
d2 = date(2014,7,11)
delta = d2 - d1
print(delta.days)
'''

'''from math import pi
r = 6
V = (4/3)* pi * r**3
print("The tich khoi cau = " + str(V))'''

'''def difference(n):
    if n <= 17:
        return 17-n
    else:
        return (n-17)*2
print(difference(5))
print(difference(36))'''

'''def within_hundred(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(within_hundred(900))
print(within_hundred(10000))'''

'''def sum_three(x,y,z):
    sum = x + y + z
    if(x==y==z):
        sum = sum*3
    return sum
print(sum_three(4,25,36))
print(sum_three(25,25,25))'''

'''def new_string(str):
    if len(str) >= 2 and str[:2]=="Is":
        return str
    return "Is" + str
print(new_string("Array"))
print(new_string("IsArray"))'''

'''def copy_string(str, n):
    result = ""
    for i in range(n):
        result = result + str
    return result
print(copy_string("hello",2))'''

'''n = int(input("Nhap so: "))
mod = n%2
if mod >0:
    print("Day la so le")
else:
    print("Day la so chan")'''
    
'''def count_4(nums):
    count=0
    for num in nums:
        if num == 4:
            count+=1
    return count
print(count_4([4,1,4,6,4]))'''

'''def copy_substring(str,n):
    dodai = 2
    if dodai > len(str):
        dodai = len(str)
    substr = str[:dodai]
    result = ""
    for i in range(n):
        result = result + substr
    return result
print(copy_substring("123",2))'''

'''def find_vowel(char):
    vowel = "xinchao"
    return char in vowel
print(find_vowel('a'))
print(find_vowel('b'))'''

def find_value(num):
    group = [1,2,3,4]
    return num in group
print(find_value(2))
print(find_value(5))