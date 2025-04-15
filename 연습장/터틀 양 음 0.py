import turtle
t=turtle.Turtle()
t.shape("turtle")
a=turtle.textinput("pyhon turtle grape","숫자를 입력하시오.:")
num=int(a)

if num>0:
   t.goto(100,100)
   t.write("입력된 정수는 양의 정수입니다.")
elif num==0:
     t.goto(100,0)
     t.write("입력된 정수는 0입니다.")
else:
      t.goto(100,-100)
      t.write("입력된 정수는 음의 정수입니다.")
        
