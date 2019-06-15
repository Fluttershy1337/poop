from turtle import Pen
from time import sleep

t1 = Pen()
t2 = Pen()

t1.up()
t2.up()

t1.right(90)
t2.right(90)

for i in range(25):
	t1.forward(8)
	t2.forward(8)

t1.left(90)

t1.down()
t2.down()

t2.right(90)
t2.forward(200)

for i in range(15):
	t1.forward(6)
	t2.forward(6)
	t1.left(6)
	t2.right(6)


for i in range(6):
	t1.forward(6)
	t2.forward(6)

for i in range(15):
	t1.forward(6)
	t2.forward(6)
	t1.left(6)
	t2.right(6)

for i in range(8):
	t1.forward(6)
	t2.forward(6)

t1.right(90)
t2.left(90)

for i in range(45):
	t1.forward(6)
	t2.forward(6)

for i in range(15):
	t1.left(6)
	t2.right(6)
	t1.forward(4)
	t2.forward(4)


for i in range(3):
	t2.forward(6)
	t1.forward(6)

t2.right(90)
t1.left(90)

for i in range(20):
	t1.left(4.5)
	t2.right(4.5)
	t1.forward(5)
	t2.forward(5)


sleep(2)
