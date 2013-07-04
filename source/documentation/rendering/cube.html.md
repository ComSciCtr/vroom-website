---
layout: documentation
title:  cube
module: rendering
source: cube.py
tags:   [ geometry ]
related:
   - [ sphere, rendering/sphere.html ]
---

Render a cube.

### syntax

~~~ python
cube(size)       # single float value
cube(sx, sy, sz) # multiple float values
~~~

### paramaters

size | size of the cube in all directions
sx   | size of the cube in x-direction
sy   | size of the cube in y-direction
sz   | size of the cube in z-direction

### optional arguments

style    | rendering style: `"wireframe"` (default) or `"solid"`
texture  | [Texture](/documentation/rendering/texture.html) object(s)

### examples

#### draw a wireframe cube

![](holder.js/400x225/social)

~~~ python
def draw():
   lighting(False)
   color(1.0, 1.0, 1.0)
   cube(3.0)
~~~


#### draw a solid cube

![](holder.js/400x225/social)

~~~ python
def draw():
   lighting(True)
   material(1.0, 1.0, 1.0)
   cube(3.0, style='solid')
~~~


#### draw a texture-mapped cube

![](holder.js/400x225/social)

~~~ python
def init():
   Global.texture = Texture.from_file("crate.png")

def draw():
    cube(3.0, texture=Global.texture)
~~~

