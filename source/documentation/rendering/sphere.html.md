---
layout: documentation
title:  sphere
module: rendering
source: sphere.py
related:
   - [ sphereDetail, rendering/sphere-detail.html ]
   - [ cube, rendering/cube.html ]
---

Draw a sphere.

### syntax 

~~~ python
sphere(radius)
~~~

### parameters

radius | radius of sphere

### optional arguments

style    | rendering style: "wireframe" (default) or "solid"
texture  | [Texture](#) object(s)

### examples

#### draw a wireframe sphere

~~~ python
def draw():
   lighting(False)
   color(1.0, 1.0, 1.0)
   sphere(3.0)
~~~

#### draw a solid sphere

~~~ python
def draw():
   lighting(True)
   material(1.0, 1.0, 1.0)
   sphere(3.0, style='solid')
~~~
