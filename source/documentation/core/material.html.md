---
layout: documentation
title:  material
module: core
source: lighting.py
related:
   - [ color, core/color.html ]
   - [ lighting, core/lighting.html ]
---

Set the material properties when rendering. After calling `material()` all
subsequent rendering will use the specified material value. Material values
must be in the range 0.0 to 1.0.

### syntax

~~~ python
material(grey)
material(r, g, b)
material(r, g, b, a)
material([r, g, b])
material([r, g, b, a])
~~~

### paramaters

grey | grey-scale value
r    | red value
g    | green value
b    | blue value
a    | alpha (transparency) value

### examples

#### draw a solid white cube

~~~ python
   # using grey-scale value
   material(1.0)
   cube(3.0)

   # using rgb value
   material(1.0, 1.0, 1.0)
   cube(3.0)

   # using rgb list
   material([1.0, 1.0, 1.0])
   cube(3.0)

   # using a variable
   my_material = [1.0, 1.0, 1.0]
   material(my_material)
   cube(3.0)

   # using color alias
   material(white)
   cube(3.0)
~~~
