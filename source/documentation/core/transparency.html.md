---
layout: documentation
title:  transparency
module: core
source: lighting.py
related: 
   - [ color, core/material.html ]
---

Enable or disable transparency. Transparency is disabled by default.

### syntax

~~~ python
transparency(enable)
~~~

### parameters

enable | `True` or `False`

### examples

#### draw a transparent sphere

~~~ python
def draw():
   lighting(False)
   transparency(True)
   color(0.0, 1.0, 0.0, 0.3)
   sphere(3.0)
~~~
