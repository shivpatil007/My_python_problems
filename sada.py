districtCount = int(input())
alpha1 = input()
alpha2 = input()
alpha3 = input()
alpha4 = input()
dig1 = int(input())
dig2 = int(input())
dig3 = int(input())
dig4 = int(input())
total = 0
total += districtCount
a = ord(alpha2)-ord(alpha1)+1
print("-------------")
print(a)
b = ord(alpha4)-ord(alpha3)+1
print(b)
total *= a*b*(dig1+1) * (dig2+1) * (dig3+1) * (dig4+1)
print(total)
