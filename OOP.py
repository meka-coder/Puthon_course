#--------------------------------------------------------------------1
class Game:
  # Write Class Content
  def __init__(self,name,developer,year,price):
    
    self.name = name
    self.developer = developer
    self.year = year
    self.price = price
      
  def price_in_pounds(self):
      
      return (f"price in egypt is {self.price *15.6} Egyptian Pounds")
  
game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")

# Needed Output
# "Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds"

print( f"#" * 50)
#--------------------------------------------------------------------------2

class User:
    # دالة البناء لتعريف البيانات عند إنشاء الكائن
    def __init__(self, name, lname, age, gender):
        self.name = name
        self.lname = lname
        self.age = age
        self.gender = gender

    def full_details(self):
        # تحديد اللقب بناءً على الجنس
        title = "Mr" if self.gender == "Male" else "Mrs"
        
        # أخذ الحرف الأول من الاسم الأخير وتحويله لحرف كبير مع إضافة نقطة
        first_letter_lname = self.lname[0].upper() + "."
        
        # حساب السنوات المتبقية للوصول لسن الـ 40 وتنسيق الرقم ليظهر بخانتين
        years_left = f"{40 - self.age:02d}"
        
        # إرجاع النص المطلوب
        return f"Hello {title} {self.name} {first_letter_lname} [{years_left}] Years To Reach 40"


user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40

#-------------------------------------------------------------------------- 3

print( f"-" * 50)
class Message:
  # Write Class Content
  @staticmethod
  def print_message():
     return  "Hello From Class Message "

print(Message.print_message())

# Output
# Hello From Class Message
print( f"-" * 50)

#--------------------------------------------------------------------------4

class Games:
    def __init__(self, gg):
        self.gg = gg  # تخزين القيمة (سواء كانت نص، رقم، أو قائمة) داخل الكائن

    # تم تحويلها لدالة عادية باستخدام self لتقرأ بيانات الكائن المستدعى
    def show_games(self):
        # فحص إذا كانت القيمة رقماً
        if isinstance(self.gg, int):
            return f"I Have {self.gg} Game."

        # فحص إذا كانت القيمة نصاً
        elif isinstance(self.gg, str):
            return f'I Have One Game Called "{self.gg}"'

        # فحص إذا كانت القيمة قائمة أو مصفوفة ألعاب
        elif isinstance(self.gg, list):
            result = "I Have Many Games:\n"
            for g in self.gg:
                result += f"-- {g}\n"
            return result.strip()  # .strip() لتنظيف الفراغات الزائدة في النهاية

        else:
            return "Unknown format"


# --- تجربة الكود وتشغيله ---

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

# أضفنا print() لرؤية النتيجة لأن الدالة ترجع نصاً (return)
print(my_game.show_games())
print("-" * 30)

print(my_games_names.show_games())
print("-" * 30)

print(my_games_count.show_games())

#---------------------------------------------------------------------- 5 


# Main Class
class Members:

    def __init__(self, n, p):

      self.name = n

      self.permission = p

    def show_info(self):

      return f"Your Name Is {self.name} And You Are {self.permission}"

# Create Admin Class Here
class Admins(Members): 
    
    def __init__(self, name, permission) :

        super().__init__( name,  permission)


# Create Moderators Class Here
class  Moderators(Admins):
    def __init__(self, name, permission) :

      super().__init__( name, permission)

member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator

#------------------------------------------------------------6 

class A:

    def __init__(self, one):

        self.one = one

class B:

    def __init__(self, two):

        self.two = two

class C:

    def __init__(self, three):

        self.three = three

# Write The Class Called "Name" Here
class Text(A,B,C):

        def __init__(self, one,two,three):
            
            A.__init__(self, one)
            B.__init__(self, two)
            C.__init__(self, three)

        def show_name(self):

            return f"the name is {self.one}{self.two}{self.three}"


the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# Ouput
# The Name Is Elzero

