---
layout:  documentation
title:   addMainMenuItem
module:  core
source:  application.py
tags:    [ utils, interface ]
related: 
   - [ setMainMenuTitle, core/set-main-menu-title.html ]
---

Add a button to the main application menu.

{:.alert.alert-info}
The main menu can only be modified in the application's `init()` function.
Calling this function after the application has been initialized will have
no effect. This means that changes made to the main menu during a live-coding
session will not be seen until the program has been restarted.

### syntax

~~~ python
addMainMenuItem(label, callback)
~~~

### parameters

label    | button label string
callback | callback function


### optional arguments

type | button type: "button" (default) or "toggle"


### examples

#### basic push-button callback

Add a button to the main menu with the label "Reset Navigation". When the button is
clicked the function `resetNavigation` will be called. 

~~~ python
def init():
   addMainMenuItem('Reset Navigation', resetNavigation)
~~~

#### toggle-button callback

~~~ python
def init():
   addMainMenuItem('Enable Lighting', toggleLighting, type="toggle")
~~~

#### lambda function callback

~~~ python
def init():
   addMainMenuItem('Enable Lighting', lambda x: Global.lighting.toggle(), type="toggle")
~~~
