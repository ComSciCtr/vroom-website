---
layout:  documentation
title:   setMainMenuTitle
module:  core
source:  application.py
tags:    [ utils, interface ]
related: 
   - [ addMainMenuItem, core/add-main-menu-item.html ]
---

Change what is displayed at the top of the main application menu.  By default
the main menu title is set to *vroom*. Use this function to change it.

{:.alert.alert-info}
The main menu can only be modified in the application's `init()` function.
Calling this function after the application has been initialized will have
no effect. This means that changes made to the main menu during a live-coding
session will not be seen until the program has been restarted.

### syntax

~~~ python
setMainMenuTitle(title)
~~~

### parameters

title | title string 

### examples

~~~ python
def init():
   setMainMenuItem('My Vroom App')
~~~
