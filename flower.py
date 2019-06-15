from turtle import Pen
from time import sleep

t1 = Pen()
t2 = Pen()

t1.up()
t2.up()

t1.right(90)
t2.right(90)
t1.forward(200)
t2.forward(200)

t1.left(90)

t1.down()
t2.down()

t2.right(90)
t2.forward(200)

t1.left(45)
t2.right(45)

for i in range(3):
	t1.forward(20)
	t2.forward(20)
	t1.left(15)
	t2.right(15)

t1.forward(50)
t2.forward(50)

for i in range(3):
	t1.forward(20)
	t2.forward(20)
	t1.left(15)
	t2.right(15)

t1.left(45)
t2.right(45)

for i in range(5):
	t1.forward(10)
	t2.forward(10)

t1.right(90)
t2.left(90)

for i in range(30):
	t1.forward(10)
	t2.forward(10)

for i in range(6):
	t1.left(15)
	t2.right(15)
	t1.forward(10)
	t2.forward(10)

t2.forward(23)
t1.forward(23)
t2.right(90)
t1.right(90)
t2.forward(50)


sleep(2)
