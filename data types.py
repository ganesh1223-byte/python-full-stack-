Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #data types
>>> a = 9
>>> type(a)
<class 'int'>
>>> b=0.7
>>> type(b)
<class 'float'>
>>> c='ganesh'
>>> type(c)
<class 'str'>
>>> d="esu"
>>> type(d)
<class 'str'>
>>> e='''ganeshuuu'''
>>> type(e)
<class 'str'>
>>> f=2+3j
>>> type(f)
<class 'complex'>
>>> #data types conversions
>>> int(2)
2
>>> int(2.3)
2
>>> int('rythm')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    int('rythm')
ValueError: invalid literal for int() with base 10: 'rythm'
>>> int(2+5j)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    int(2+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> int(True)
1
>>> int(False)
0
>>> float(3)
3.0
float(4.5)
4.5
float('ganesh')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float('ganesh')
ValueError: could not convert string to float: 'ganesh'
float()
0.0
float(3+6j)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    float(3+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(Flase)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    float(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
float(False)
0.0
str(1)
'1'
str(2.5)
'2.5'
str('fwgd')
'fwgd'
str(13+8j)
'(13+8j)'
str(True)
'True'
str(False)
'False'
complex(2)
(2+0j)
complex(3.5)
(3.5+0j)
complex('typsv')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    complex('typsv')
ValueError: complex() arg is a malformed string
complex(2+4j)
(2+4j)
complex(True)
(1+0j)
KeyboardInterrupt
complex(False)
0j
bool(2)
True
bool(2.5)
True
bool('gan')
True
bool(3+5j)
True
bool(True)
True
bool(False)
False
