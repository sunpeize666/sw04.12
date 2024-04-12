fac=1
input_num=int(input("점수 입력 :"))
num=input_num#初始值
while input_num >= 1:#条件式
    
    fac = fac * input_num
    input_num = input_num - 1 #증감식
print(f"{num}! = {fac}")
#5! = 120
