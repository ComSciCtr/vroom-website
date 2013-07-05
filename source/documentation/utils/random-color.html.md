---
layout: documentation
title:  random\_color
module: utils
source: generators.py
tags: [ utils, random ]
related:
   - [ random_color_generator, utils/random-color-generator.html ]
---

Return a random [r,g,b] color value.

### syntax

~~~ python
random_color()
~~~

### returns

3-element list containing (r,g,b) values between 0.0 and 1.0

### examples

#### draw a random colored cube

![](holder.js/400x225/social)

~~~ python
def draw():
   color(random_color())
   cube(3.0)
~~~

#### assign random colors to new objects

![](holder.js/400x225/social)

~~~ python
def init():
   Global.points = [] 
   Global.colors = [] 

def draw():
   for (color, point) in zip(Global.colors, Global.points):
      color(color)
      pushMatrix()
      translate(point)
      sphere(3.0)
      popMatrix()

def button_press(pos, button):
   Global.points.append(pos)
   Global.colors.append(random_color()
~~~



