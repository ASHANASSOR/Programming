Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> number=float(input('Please enter a floating point number: '))
Please enter a floating point number: 3.678
>>> print('You  entered',number)
You  entered 3.678
>>> num_string=str(number)
>>> integer_part,_,fractional_part=num_string.partition('.')
>>> print('The integer part is:',integer_part)
The integer part is: 3
>>> print('The fractional part is:',fractional_part)
The fractional part is: 678
