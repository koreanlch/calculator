import math
import random
print('무엇을 하고 싶습니까?',end="")
d=input()
if(d=='오늘의 운세'):
    result=random.choice(['Good','so so','bad'])
if(d=='계산기'):
    print('원하는 사칙연산을 입력하시오 : ',end="")
    a=input()
    if(a=='덧셈'):
        print('피가수 : ',end="")
        b=input()
        print('가수 : ',end="")
        c=input()
        result=float(b)+float(c)
    if(a=='뺄셈'):
        print('피감수 : ',end="")
        b=input()
        print('감수 : ',end="")
        c=input()
        result=float(b)-float(c)
    if(a=='곱셈'):
        print('피승수 : ',end="")
        b=input()
        print('승수 : ',end="")
        c=input()
        result=float(b)*float(c)
    if(a=='나눗셈'):
        print('피제수 : ',end="")
        b=input()
        print('제수 : ',end="")
        c=input()
        result=float(b)/float(c)
    if(a=='거듭제곱'):
        print('밑 : ',end="")
        b=input()
        print('지수 : ',end="")
        c=input()
        result=float(b)**float(c)
    if(a=='로그'):
        print('밑 : ',end="")
        b=input()
        print('진수 : ',end="")
        c=input()
        result=math.log(float(c),float(b))
    if(a=='원의 넓이'):
        print('반지름 : ',end="")
        b=input()
        result=str(int((float(b)**2)))+'π'
    print('답 : '+str(result))
