Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> o=int(input("Please enter a three digit integer:"))
Please enter a three digit integer:123
>>> r=int(str(o) [::-1])
>>> print("You entered(:",o)
You entered(: 123
>>> print(o,"reversed is ",r)
...             
123 reversed is  321
