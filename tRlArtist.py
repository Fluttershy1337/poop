from turtle import Pen
from time import sleep


pen = Pen()

pen.right(60)
pen.forward(60)
pen.right(120)
pen.forward(60)
pen.right(120)
pen.forward(60)
pen.left(120)
pen.up()
pen.forward(55)
pen.down()

for i in range(4):
	pen.forward(35)
	pen.up()
	pen.forward(15)
	pen.left(90)
	pen.forward(15)
	pen.down()

pen.forward(15)
pen.right(90)
pen.up()
pen.forward(10)
pen.down()
pen.forward(120)
pen.right(90)
pen.forward(65)
pen.right(90)
pen.forward(120)
pen.right(90)
pen.forward(65)

sleep(7)
