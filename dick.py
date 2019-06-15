from turtle import Pen
from time import sleep


pen = Pen()

pen.up()
pen.forward(150)
pen.down()

for i in range(4):
	pen.forward(100)
	pen.left(90)

sleep(1)

pen2 = Pen()

pen2.forward(80)
pen2.up()
pen2.right(90)
pen2.forward(20)
pen2.down()
pen2.right(90)
pen2.forward(80)

sleep(4)
