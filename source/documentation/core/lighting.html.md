---
layout: documentation
title:  lighting
module: core
source: lighting.py
related:
   - [ material, core/material.html ]
---

Enable or disable lighting. By default lighting is disabled.

### syntax

~~~ python
lighting(enable)
~~~

### parameters

enable | `True` or `False`


### examples

#### draw a solid cube 

~~~ python
def draw():
   lighting(True)
   material(1.0, 1.0, 1.0)
   cube(3.0)
~~~

#### draw a wireframe cube
~~~ python
def draw():
   lighting(False)
   color(1.0, 1.0, 1.0)
   cube(3.0)
~~~
