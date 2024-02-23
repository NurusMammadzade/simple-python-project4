import turtle as ts
import colorsys as cs
for i in range(60):
   ts.tracer(40)
   ts.speed(2)
   ts.pensize(1)
   ts.color(cs.hsv_to_rgb(i/10, 0.7, 1))
   ts.bgcolor("black")
   ts.right(1)
   ts.left(15)
   ts.circle(30)
   ts.right(3)
   ts.left(30)
   ts.circle(95)
   
   ts.right(6)
   ts.left(60)
   ts.circle(180)
ts.done()