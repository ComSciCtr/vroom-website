---
layout: documentation
title:  get_resource
module: utils
source: resources.py
tags:   [ utils ]

---

Return a global or application resource.

At some point you will probably need to access data in your program. If
the resource is specified in the application with a relative pathname it
will not work if run from another directory. Specifying a global path 
will work, but fails if the program is run on a different machine.
The `get_resource` function solves this problem by allowing resouces to be
specified relative to the applications `data/` directory. Simply create
a folder in your application's root directory named `data/` and place any
resources you need there. These can then be retrieved by using the relative
path name. For example, if you place a file named `data.txt` in your `data/`
directory you would access it from your program with `get_resource("data.txt")`.
The correct file will be returned regardless of where the program is run from
and can be distributed and run on different machines without issue.

You can also put data resources in vroom's global directory and access it 
from any program even if there is no local `data/` directory. This is useful
for commonly used resources (like textures for point sprite rendering or fonts).

{:.alert.alert-info}
If there is a resource in the global data directory with the same name as one
in the local directory, the local resource will be returned.

### syntax

~~~ python
get_resource(filename)
~~~

### parameters
filename | resource path relative to data directory


