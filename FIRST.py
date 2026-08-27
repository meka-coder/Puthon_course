# -------------------
# -- Concatenation --
# -------------------

msg = "I Love"
lang = "Python"
print(msg + " " + lang)

full = msg + " " + lang
print(full)

a = "First \
Second \
Third"

b = "A \
B \
C"
name ="osama"
age = "38"
country = "algeria"
print(a + "\n" + b)

print("Hello " + "1" + " World")  # Error
#---------------------------------------------------------------------------2
#-------------------2.1
#"Hello, My Name Is Osama And Iam 38 Years Old and I Live in Egyptprint


print(type(name))
print(type(age))
print(type(country))


#-----------------2.2
print(''' "Hello 'Osama', How You Doing \\
""" Your Age Is "38"" +
And Your Country Is: Egypt ''')
#-----------------2.3
#name = 'Elzero'
# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"
name ='Elzero'
print(f''' {name[1]} 
 {name[2]} 
 {name[-1]} ''')

 #-----------------2.4
 

# Needed Output
# "lze"
# "Ezr"
# "rzE"
 
print(f''' {name[1:4]} 
 {name[0:5:2]} 
 {name[-2::-2]} ''')

#-----------------2.5 
a = "#@#@Elzero#@#@"
# Needed Output
# Elzero
print(a.strip("#@"))

#-----------------2.6 
num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500
print(num1.zfill(4)) 
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

#-----------------2.7
name_one = "Osama"
name_two = "Osama_Elzero"

# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero
print(name_one.center(36, "@").rstrip("@"))
print(name_two.center(28, "@").rstrip("@")) 

#-----------------2.8 
name_one = "OSamA"
name_two = "osaMA"

# Needed Output
# osAMa
# OSAma 
print(name_one.swapcase())
print(name_two.swapcase()) 

#-----------------2.9 
msg = "I Love Python And Although Love Elzero Web School"

# Needed Output
# 2 

print(msg.count("Love")) 

#-----------------2.10
name3= "Elzero"

# Needed Output
# 2

print(name3.index("z")) 

#-----------------2.11,12
msg2 = "I <3 Python And Although <3 Elzero Web School"

# Needed Output
# I Love Python And Although <3 Elzero Web School 
print(msg2.replace("<3","love"))

#-----------------2.13
name = "Osama"
age = 38
country = "Egypt"

# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt
print("My Name Is %s, And My Age Is %d, And My Country Is %s".format(name, age, country))

#-----------------3.1
#1+2j

# Print Imaginary Part Here
# Print Real Part Here
num31= 1+2j

print(num31.imag)
print(num31.real)

#-----------------3.2
num32 = 10

# Needed Ouput
# 10.0000000000

print(float(num32))

#-----------------3.3
num33 = 159.650

# Needed Output
# 159
# <class 'int'>
print(int(num33))
print(type(int(num33)))

#-----------------3.4 
#100 ? 115 = -15
#50 ? 30 = 1500
#21 ? 4 = 1
#110 ? 11 = 10
#97 ? 20 = 4
print(100 - 115)
print(50 * 30)
print(21 % 4)
print(110 / 11)
print(97 // 20)
#------------------------3.lessen 21

mylist =["one", "two","one", 1 , 100.5 ,True ] 

print(mylist[1])
print(mylist[-1])
print(mylist[-3])

print(mylist[1:4])
print(mylist[:5])
print(mylist[1:])

print(mylist[:6:2])

#mylist[1]=2
#mylist[-1]= False
#mylist[1:4]=[]
mylist[2:5]=["three",3,True]
print(mylist)

print(type(mylist[1]))

#------------------------3.lesson 22

myfreind= ["ali", "mouhammed", "sami"]
myoldfriend=["yassine","mimoune","azize"]

myfreind.append("ahmed")
myfreind.append(True)
myfreind.append(100.520)
myfreind.append(myoldfriend)

print(myfreind)
print(myfreind[2])
print(myfreind[6])
print(myfreind[5])
print(myfreind[6][2])

a=[1,2,3]
b=["e","b",6]
c=[7,8,True]

a.extend(b)
a.extend(c)
print(a)

x=[1,2,3,"osama",True,"osama","osama"]
x.remove("osama")
print(x)#[1, 2, 3, True, 'osama', 'osama']

y=[1, 2, 100, 120 ,-10 , 17,29]
yy=["a","r","q","c"] 

y.sort()
yy.sort()
print(y)#[-10, 1, 2, 17, 29, 100, 120]
print(yy)#['a', 'c', 'q', 'r']

y.sort(reverse=True)
print(y)#[120, 100, 29, 17, 2, 1, -10]

z=[1,"ttt",True,155]
z.reverse()
print(z)#[155, True, 'ttt', 1]

#------------------------3.2-1

frinds=["ibrahim","mohammed","bilal","jamal","hosine"]
print(frinds[0])
print(frinds[-4])
print(frinds[0:5:3])
print(frinds[0:5:2])

#------------------------3.2.3

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"
n=len(friends)
print(friends[1:-1])
print(friends[-2:])

#------------------------3.2.4

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# ["Osama", "Ahmed", "Sayed", "ibrahim", "ibrahim"]

friends[3:5]=["ibrahim", "ibrahim"]
print(friends)

#------------------------3.2.5

friends = ["Osama", "Ahmed", "Sayed"]

# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends.append("Salem")
print(friends )
friends.insert(0,"Nasser")
print(friends)

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]

friends.remove("Nasser" )
friends.remove("Osama" )
friends.remove("Salem" )
print(friends )

#------------------------3.2.6

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)
print(friends)


#------------------------3.3.1 Tuples  

# Needed Output

# "Osama"
# <class 'tuple'> 

my_name = "ibrahimandsalsabil",
print(my_name)
print(type(my_name))

#-------------------------3.3.2 

fr1ends1 = ("Osama", "Ahmed", "Sayed")

# Needed Output

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements

print(fr1ends1)
print(type(fr1ends1))
print(len(fr1ends1))

#-------------------------3.3.3

my_tuple = (1, 2, 3, 4)

# Needed Output

# 1
# 2
# 4

a,b,_,c = my_tuple
print(a)
print(b)
print(c)

#-------------------------4.1 Set and Set Methode

my_list = [1, 2, 3, 3, 4, 5, 1]
# Needed Output

# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4

list_to_set = list(set(my_list))
print(list_to_set)
print(type(list_to_set))
print(list_to_set[0:4])

#--------------------------4.2

nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}

nums_letters1 = nums.union(letters)
print(nums_letters1)
nums_letters2 = nums | letters
print(nums_letters2)
nums_letters3= {*nums, *letters}
print(nums_letters3)

#--------------------------4.3

# قم بإنشاء Set تحتوي على العناصر 1, 2, 3
# في السطر الأول قم بطباعة محتوى ال Set
# قم بإفراغ محتوى ال Set كاملا بسطر واحد فقط ثم قم بطباعة المحتوى في السطر الثاني لتتأكد من أنها فارغة تماما
# قم بإضافة عنصرين “A”, “B” لهذه ال Set ثم إطبع محتواها في السطر الثالث
# قم بمحاولة إزالة العنصر “C” طبعا العنصر غير موجود تأكد أنه لن يخرج لك خطأ عندما تحاول إزالة العنصر الغير موجود
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3}
# set()
# {"A", "B"}

print(my_set)
my_set.clear()
print(my_set)

my_set.update({"A", "B"})
print(my_set)

letters.discard("C")
print(letters)

#--------------------------4.4

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

# Needed Output

print(set_one.issubset(set_two))

#--------------------------5

# Create Dictionary Here

My_Dic = { 
    "C":70,
    "HTML": 90,
    "CSS": 80,
    "Python": 30,
    "AI": 20
}

# Needed Output
#"HTML Progress Is 90%"
#"CSS Progress Is 80%"
#"Python Progress Is 30%"
#"AI Progress Is 20%"

print(f"HTML Progress is {My_Dic['HTML']}%")
print(f"CSS Progress is {My_Dic['CSS']}%")
print(f"Python Progress is {My_Dic['Python']}%")
print(f"AI Progress is {My_Dic['AI']}%")

#--------------------------6.1

name = input('What\'s Your name :')
name = name.strip().capitalize() 
print(f"Hello {name}, Happy To See You Here.")

#--------------------------6.2

age = input('What\'s Your Age')
age = int(age) # age = int(input('What\'s Your Age'))
if age < 16 : 
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else :
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")

#--------------------------6.3

name  = input('What\'s Your name :')
name  = name.strip().title() 
last_name = input('What\'s Your Last Name :')
last_name = last_name.strip().title() 
print(f"Hello {name}, Happy To See You Here.")
print(f"Hello {last_name}, Happy To See You Here.")  


#--------------------------6.4

email  = input('What\'s Your email :')
email  = email.strip().lower()

print(f"Hello {email[:email.index('@')].title()}, Happy To See You Here.")
print(f"Email Service Provider Is {email[email.index('@') + 1:email.index('.')]}")  
print(f"Top Level Domain Is {email[email.index('.') + 1:]}")

#--------------------------6.5

# 1. إنشاء قائمة فارغة وتحديد الحد الأقصى (4 أصدقاء)
my_friends = []
MAX_FRIENDS = 4

# حلقة تكرارية تستمر طالما أن عدد العناصر في القائمة أقل من 4
while len(my_friends) < MAX_FRIENDS:
    
    # 2. طلب إدخال الاسم وإزالة المسافات الزائدة من البداية والنهاية
    aa = input("What's the name of your friend? ").strip()
    
    # شرط إضافي: التأكد من أن المستخدم لم يضغط Enter بدون كتابة شيء
    if not aa:
        print("Please enter a valid name.")
        continue

    # 3. إذا كان الاسم كاملاً حروفاً كبيرة -> مرفوض
    if aa.isupper():
        print("Name of your friend is not valid (All Caps).")
        
    # 4. إذا كان الاسم كاملاً حروفاً صغيرة -> تكبير أول حرف وإضافته
    elif aa.islower():
        aa = aa.capitalize()  # capitalize تجعل أول حرف كبير والباقي صغير
        my_friends.append(aa)
        print(f"Your friend's name '{aa}' has been added to the list.")
        print("Warning: The first letter of your friend's name has been changed to a capital letter.")
        
    # 5. إذا كان أول حرف كبيراً والباقي صغيراً -> إضافة مباشرة
    elif aa[0].isupper() and (len(aa) == 1 or aa[1:].islower()):
        my_friends.append(aa)
        print(f"Your friend's name '{aa}' has been added to the list directly.")
        
    # في حال لم يطابق الشروط (مثلاً حروف مبعثرة كبيراً وصغيراً بشكل عشوائي)
    else:
        print("Name of your friend is not valid.")

    # 6. حساب وطباعة الأماكن المتبقية في القائمة
    remaining_places = MAX_FRIENDS - len(my_friends)
    print(f"The remaining places are: {remaining_places}")
    print("-" * 30)  # خط فاصل لتنظيم شكل المخرجات

# رسالة نهائية عند امتلاء القائمة وخروج البرنامح من الحلقة
print("The list is full! Your friends are:", my_friends)


#-------------------------------------6.6.1


students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

for mainKey , mainValue in students.items():

    print("-" * 50)
    print(f'"-- Student Name => {mainKey}"')
    print("-" * 50)
    for secondKey , secondValue in mainValue.items():
      print(f'"- {secondKey} => {secondValue} Points"')
    
#-------------------------------------6.6.2
for student in students: 

  
    if students[student]["percentage"] == "A":
        students[student]["percentage"] = 100
        
    print("-" * 50)
    print(f"Skills and Progress For {student} Is: ")
    print("-" * 50)

    for percentage in students[student]:
        print(f"{percentage} => {students[student][percentage]}")
      
    print("-" * 50)


#------------------------------6.6.3

myF= open(r"C:\Users\hp\Desktop\python\assign.py", "w")

#print(myF.name)
#print(myF.mode)
#print(myF.encoding)

my_f=open(r"C:\Users\hp\Desktop\python\ibrahim.txt", "w")

#print(my_f.name)
#print(my_f.mode)
#print(my_f.encoding)

my_f=open(r"C:\Users\hp\Desktop\python\ibrahim.txt", "a")

for i in range(50):
    file_num = i + 1  # لتبدأ الأرقام من 1 إلى 50
    
    if file_num == 25:
        # إذا وصلنا للملف رقم 25، ننشئه باسم special-text ونتركه فارغاً
        myF = open(rf"C:\Users\hp\Desktop\python\special-text.txt", "w")
        myF.close()  # إغلاقه مباشرة ليبقى فارغاً
    else:
        # بقية الملفات يتم تسميتها txt ثم رقم الملف
        myF = open(rf"C:\Users\hp\Desktop\python\txt{file_num}.txt", "w")
        myF.write(f"Elzero Web School => {file_num}")
        myF.close()  # إغلاق الملف لحفظ البيانات


import os 
print(os.getcwd())

print(os.path.abspath(__file__))

print(myF.name)

ff= os.path.dirname(os.path.abspath(__file__))

print(len(os.listdir(ff)))

txt1 = open(r"C:\Users\hp\Desktop\python\txt1.txt","a")

for i in range(50):

    txt1.write("\n Appended => Elzero Web School")
    

txtt= open(r"C:\Users\hp\Desktop\python\txtt.txt","r")

line = txtt.readlines()

num_lines = len(line) 
print(num_lines)

txtt.seek(0)

num_words =txtt.read()
print(len(num_words.split()))

txtt.seek(0)

num_letters = txtt.read()
print(len(num_letters))

txtt.seek(0)

num_l_char = num_letters.count("l")
print(num_l_char)


#------------------------------7.1.1

value = (0,1,2)
if any(value):
    myVar=0

my_list = [True , 1 , 1 , ["A","B",0] , 10.5 , myVar]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

    print("Good")

else:

    print("Bad")

#Good becoose all variables of our list is not zero  


#------------------------------7.1.2

v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

print(sum(my_range, v))

print(pow(v, v,v))


#------------------------------7.1.3

n =  20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")

# Output => Good

#-------------------------------8 

from datetime import datetime

# جلب الوقت والتاريخ الحالي لليوم
now = datetime.now()

# طباعة التاريخ بأكثر من طريقة حسب التنسيقات المطلوبة
print(f'# Today Is "{now.strftime("%Y, %m, %d")}"\n')

print(now.strftime('"%Y-%m-%d"'))          # صيغة: "2026-06-25"
print(now.strftime('"%b %d, %Y"'))          # صيغة: "Jun 25, 2026"
print(now.strftime('"%d - %b - %Y"'))       # صيغة: "25 - Jun - 2026"
print(now.strftime('"%d / %b / %y"'))       # صيغة: "25 / Jun / 26"
print(now.strftime('"%d / %B / %Y"'))       # صيغة: "25 / June / 2026"
print(now.strftime('"%a, %d %B %Y"'))       # صيغة: "Thu, 25 June 2026"


#-------------------------------------------9.1

def reverse_string(my_string):
    
    index = len(my_string) - 1
    
    while index >= 0:
        
        yield my_string[index]
        
        index -= 1

# Reverse The String
for c in reverse_string("Elzero"):
    print(c, end="")

#-----------------------------------9.2

def NewDecorator(fun):

    print("Sugar Added From Decorators")

    fun() 

    print("#" * 50)


@NewDecorator
def make_coffe():
    print("Coffe Created")

@NewDecorator
def make_coffe():
    print("Coffe Created")

#------------------------------------9.3

def myDecorator(func):  # Decorator

  def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

    if num1 < 0 or num2 < 0:

      print("Beware One Of The Numbers Is Less Than Zero")

    func(num1, num2)  # Execute Function

  return nestedFunc  # Return All Data

def myDecoratorTwo(func):  # Decorator

  def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

    print("Coming From Decorator Two")

    func(num1, num2)  # Execute Function

  return nestedFunc  # Return All Data

@myDecorator
@myDecoratorTwo

def calculate(n1, n2):

  print(n1 + n2)

calculate(-5, 90)





















































