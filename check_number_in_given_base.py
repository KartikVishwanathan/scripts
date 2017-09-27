'''Inputs are two strings, base and number. Base must satisfy 2 <= base <= 36. 
Number is an alpanumeric string. First check if base is valid, then check if number is valid
in the given base. To do that, note that each digit in the number corresponds to itself while each
letter in the number corresponds to a number. For example a -> 10, b ->11, ...., z -> 35
(Just like extensions of hexadecimal system, allowing letters nt just upto F but till Z.)

If both number and base are valid, convert the number to decimal. '''


def check_number(base, number):
  if not 2 <= int(base) <= 36:
    return 'Invalid Base'
  else:
    valid = True
    validity_checker = [0]*36
    for ch in number:
      if ch in '0123456789':
        index = int(ch)
        validity_checker[index] = ch
        if index >= int(base):
          return 'Invalid Number'
      else:
        ch = ch.lower()
        index = ord(ch) - 87
        validity_checker[index] = ch
        if index >= int(base):
          return 'Invalid number'
  
  if valid:
    result = 0
    for i, ch in enumerate(reversed(number)):
      result = result + validity_checker.index(ch)*int(base)**i
    return result  
