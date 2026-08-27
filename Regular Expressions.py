#----------------------------------------------------------
#لديك ال String التالي كما في المثال والمطلوب جلب ال Matches كما في الصورة
#قم بكتابة ال Regular Expression Code لعمل المطلوب
#"eeeeE llllLl lllzzZzzzz eroe operationr pollo "
import re
myString = "eeeeE llllLl lllzzZzzzz eroe operationr pollo "
#matches = re.search(r'\b[a-zA-Z]{5,}\b', myString)
matches = re.search(r'E\s|l\s|z\s|e\s|r\s|o$', myString)
print(matches)
#قم بالصاق هذالكود في الموقع pythex و سترى النتيجة امامك التي يريدها الزيرو
#print(matches.span())
#print(matches.string)
#print(matches.group())

#-------------------------------------------------------------

myStr1 = "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"
matches1 = re.search(r'(?<=L)Elzero(?=111\b)', myStr1)
print(matches1)

#--------------------------------------------------------------

myStr2 = "+(0100) 600-1234 \
+(0100) 60-1234\
(0100) 6000-1234\
01006001234\
0100 600 1234\
(0100) 600-1\
(0100) 600-12"
matches2 = re.search(r'^(\+)?(\([0-9]+\))\s([0-9]+)\-([0-9]{4})$', myStr2)
print(matches2)

#--------------------------------------------------------------



myStr3 = "http://www.elzero.org:8888/link.php\
https://elzero.org:8888/link.php\
http://www.elzero.com/link.py\
https://elzero.com/link.py\
http://www.elzero.net\
https://elzero.net"
matches3 = re.search(r'^(\+)?(\([0-9]+\))\s([0-9]+)\-([0-9]{4})$', myStr3)
print(matches3)


#----------------------------------------------------------------

myStr4 = "http\
https\
abcd\
abcd"
matches4 = re.search(r'^(https?://)?(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})?(:[0-9]+)?(/[a-zA-Z0-9-_.]+)*$', myStr4)
print(matches4)