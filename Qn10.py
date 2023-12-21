Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=int(input("Please enter a two digit integer:"))
Please enter a two digit integer:23
>>> y=int(str(x) [::-1])
>>> print(x,"reversed is ",y)
23 reversed is  32
>>> t=x+y
>>> print(x,"+",y,"=is",t)
23 + 32 =is 55
