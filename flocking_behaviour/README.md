# Laboratory work Nr 1 - Expert System
## Tabel of Content
1. [ Description ](#desc)
2. [ Getting Started](#start)
3. [ How to run](#running)

<a name="desc"></a>
## 1. Description
The basic flocking model consists of three simple steering behaviors which describe how an individual boid maneuvers based on the positions and velocities its nearby flockmates:
Separation: steer to avoid crowding local flockmates
Alignment: steer towards the average heading of local flockmates
Cohesion: steer to move toward the average position of local flockmates
<a name="start"></a>
## 2.  Getting Started
### This is a system created using Python language, therefore for local running you should:
pip install SimpleGUICS2Pygame
and 
Simply change:
```python
import simplegui
```
by
```python
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
```
<a name="running"></a>
## 3. How to run

python main.py