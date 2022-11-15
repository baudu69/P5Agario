# P5 
p5.py is a python library for creative coding, with a focus on making coding accessible for  beginners, and anyone else! p5.py is free and open-source because I believe software, and the tools to learn it, should be accessible to everyone.

Using the metaphor of a sketch, p5.py has a full set of drawing functionality. However, you’re not limited to your drawing canvas. You can use every python thinks text, input, video, webcam, and sound...

P5.ps is based on pygame (opengl) graphic lib and is inspired by p5.js and other systems like arduino and prossessing.

# Get Started

## install
You must configure a project with the pygame dependency. In your terminal :
```bash
python -m venv venv 
venv\Scripts\activate
pip install pygame
```

## First sketch

in your favorite editor, start main.py :
```python
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    print("Setup END-----------")


def run():
    core.cleanScreen()

core.main(setup, run)

```
end run
```bash
python main.py
```
You get a black screen of 400x400 pixel.

## First draw
Draw a white circle center in 200x200
in your favorite editor, start main.py :
```python
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    print("Setup END-----------")


def run():
    core.cleanScreen()
	core.Draw.circle((255,255,255),(200,200),10)

core.main(setup, run)

```
end run
```bash
python main.py
```
You get a black screen of 400x400 pixel with a white circle.
### the useful functions for the drawing are : 
- core.Draw.rect(color,rect,width)
- core.Draw.cricle(color, center, radius, width)
- core.Draw.polyline(color, points, width)
- core.Draw. line(color, start_position, end_position, width)
- core.Draw.ellipse(color,rect,width)
- core.Draw.arc(color, rect, start_angle, stop_angle, width)
- core.Draw.lines(color, closed, points, width)
- core.Draw.polygon(color, points, width)
- core.Draw.text(color, texte, position, size, font)

### Color :
colors are defined by tuples of 3 or 4 elements : (R,G,B) or (R,G,B,A)


## Variables
You can use python variables and their operations. However, if you want to keep data over time and between frames, you have to use global variables. 

To make it easier to understand the code and to manipulate the data, P5 provides a way to keep the data as dictionary:
```python
core.memory(key,value)
```
Example :
Draw a circle in 200x200 store in P5 memory
```python
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
	core.memory("position",(200,200))
    print("Setup END-----------")


def run():
    core.cleanScreen()
	core.Draw.circle((255,255,255),core.memory("position"),10)

core.main(setup, run)

```

## Input
### Keybord
it is possible to detect the typing of one or more keys on the keyboard.
- press:

```python
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    print("Setup END-----------")


def run():
    core.cleanScreen()
	if core.getKeyPressList("SPACE"):
		core.Draw.circle((255,255,255),(200,200),10)

core.main(setup, run)

```

- release:

```python
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    print("Setup END-----------")


def run():
    core.cleanScreen()
    if core.getKeyReleaseList("SPACE"):
        core.Draw.circle((255,255,255),(200,200),10)

core.main(setup, run)

```
### Mouse
It is possible to interact with the mouse:
```python
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    core.memory("Center", Vector2(200,200))
    print("Setup END-----------")


def run():
    core.cleanScreen()
    if core.getMouseLeftClick():
        core.memory("Centre",Vector2(core.getMouseLeftClick()))
    
    core.Draw.circle((255,255,255),core.memory("Center"), 10)
	
core.main(setup, run)

```



## Texture
It is possible to display textures and its box.
The following example displays the image "soleil.png". 

```python
from pygame.math import Vector2
import core

def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [400, 400]
    core.memory("texture",core.Texture("./soleil.png",Vector2(200,200)))
    print("Setup END-----------")


def run():
    core.cleanScreen()
    if not core.memory("texture").ready:
        core.memory("texture").load()
		
    core.memory("texture").box = True #Display box
    core.memory("texture").show()

core.main(setup, run)

```


