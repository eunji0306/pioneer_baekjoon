m=input()
c=''

#ord() 문자를 아스키 코드로 변환, chd() 아스키를 문자로 변환
for i in m:
    if i in 'ABC':
        c+=chr(ord(i)+23)
    else:
        c+=chr(ord(i)-3)
print(c)
