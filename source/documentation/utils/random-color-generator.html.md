---
layout: documentation
title:  random_color_generator
module: utils
source: generators.py
tags:   [ utils, random, color ]
related:
   - [ random_color, utils/random-color.html ]
---

Random color generator. The `random_color()` function is useful for generating
a single random color. However, if you a dealing with a large number of objects the
`random_color_generator` function can be used to generate a large number of
random color values at once.

By default points will be generated in the range [-1.0, 1.0]. This can be changed
by specifying a `start` and/or `stop` value. Note that points are generated in a
cube.

{:.alert .alert-error}
Since this function returns a generator object you will need to wrap it in a
`list()` or call the `next()` method on the generator. See the
[examples](#examples) section below for usage.

### syntax

~~~ python
random_vertex_generator(n, start=-1.0, stop=1.0):
~~~

### parameters

n     | number of vertices

### optional arguments

start | minimum for vertex data
stop  | maximum for vertex data

### return

Generator object for vertices.

### examples

#### random points

![](holder.js/400x225/social)

~~~ python
def init():
   vertices = random_vertex_generator(1000)
   Global.points = PointCloud(vertices)

def draw():
   Global.points.draw()
~~~

#### random cubes

![](holder.js/400x225/social)

~~~ python
def init():
   Global.vertices = random_vertex_generator(1000, -100, 100)

def draw():
   draw(sphere, 3.0).for_each(Global.vertices)
~~~
