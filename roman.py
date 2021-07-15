number =int(input("enter integer"))
m = [ "", "M", "MM", "MMM" ]
c = [ "", "C", "CC", "CCC", "CD", "D","DC", "DCC", "DCCC", "CM "]
x = [ "", "X", "XX", "XXX", "XL", "L","LX", "LXX", "LXXX", "XC" ]
i = [ "", "I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX"]
T = m[number// 1000]
H= c[(number % 1000) // 100]
tens =  x[(number % 100) // 10]
O = i[number % 10]     
ROMAN = (T + H +tens + O)   
print(ROMAN)