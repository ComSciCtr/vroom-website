---
layout:  documentation
title:   addMainMenuItem
module:  core
source:  application.py
tags:    [ utils, interface ]
related: 
   - [ setMainMenuTitle, core/set-main-menu-title.html ]
---

Add a button to the main application menu. The application menu can be brought
up by pressing the right mouse button. Adding buttons to this menu allows you
to interact with your program. 

For example, you could add a button to clear the screen of objects added by the
user. Or, you could start/stop an animation by adding a toggle button. See the
[examples](#examples) section below for more ideas.


{:.alert.alert-info}
The main menu can only be modified in the application's `init()` function.
**Calling this function after the application has been initialized will have
no effect.** This means that changes made to the main menu during a live-coding
session will not be seen until the program has been restarted.

### syntax

~~~ python
addMainMenuItem(label, callback)
~~~

### parameters

label    | button label string
callback | callback function

{:.alert.alert-warning}
The callback function will receive either a `Button` or `ToggleButton` object.

### optional arguments

type | button type: "button" (default) or "toggle"


### examples

#### basic push-button callback

Add a button to the main menu with the label "Clear Points". When the button is
clicked the `clear` function will be called. 

~~~ python
def init():
   Global.points = []
   addMainMenuItem('ClearPoints', clear)

def clear(button):
   Global.points = []
~~~

#### toggle-button callback

Add a toggle button with the label "Enable Lighting". When the button is clicked the
function `toggleLighting` will be called. Toggle buttons are created by adding the
additional `type` argument.

~~~ python
def init():
   Global.lighting = False
   addMainMenuItem('Enable Lighting', toggleLighting, type="toggle")

def toggleLighting(toggle):
   Global.lighting = toggle.getToggle() 
~~~

#### lambda function callback

You can even use a lambda function if you want. This example passes a lambda function
which toggles a [BooleanOption](/documentation/boolean-option.html) variable to turn
lighting on or off.

~~~ python
def init():
   Global.lighting = BooleanOption()
   addMainMenuItem('Enable Lighting', lambda x: Global.lighting.toggle(), type="toggle")

def display():
   lighting(Global.lighting)
   # render stuff...
~~~

