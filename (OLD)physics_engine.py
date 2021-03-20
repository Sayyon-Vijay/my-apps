import pygame as pyg
import copy
from math import *


class Objects:
    def __init__(self, x, y, vel_x, vel_y, acc_x, acc_y, mass, e):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.acc_x = acc_x
        self.acc_y = acc_y
        self.mass = mass
        self.e = e


class Vector:
    def __init__(self, x, y, mag):
        self.x = x
        self.y = y
        self.mag = sqrt(x ** 2 + y ** 2)


class ObjectFunctions:
    def __init__(self):
        self.inside = False
        self.collision = False

    def fric_func(self, ob_ject):
        global F_x, F_y, friction_x, friction_y, coeff_fric

        ob_ject.acc_x = 0
        ob_ject.acc_y = 0
        friction_x = coeff_fric * ob_ject.mass * g
        friction_y = coeff_fric * ob_ject.mass * g
        fric_force_x = F_x - friction_x
        fric_force_y = F_y - friction_y

        if ob_ject.y >= 840:
            if ob_ject.acc_x == 0:
                if round(ob_ject.vel_x) == 0:
                    ob_ject.vel_x = 0
                if round(ob_ject.vel_x) > 0:
                    ob_ject.acc_x = -1 * friction_x / ob_ject.mass
                    ob_ject.vel_x += ob_ject.acc_x
                    if ob_ject.vel_x < 0:
                        ob_ject.vel_x = 0
                        ob_ject.acc_x = 0
                if round(ob_ject.vel_x) < 0:
                    ob_ject.acc_x = friction_x / ob_ject.mass
                    ob_ject.vel_x += ob_ject.acc_x
                    if ob_ject.vel_x > 0:
                        ob_ject.vel_x = 0
                        ob_ject.acc_x = 0
            else:
                F_x = fric_force_x
                F_y = fric_force_y

    def movement_func(self, ob_ject, up, down, left, right, extra):
        keys = pyg.key.get_pressed()

        if keys[left]:
            ob_ject.acc_x = -1 * F_x / ob_ject.mass

        if keys[right]:
            ob_ject.acc_x = F_x / ob_ject.mass

        if keys[up]:
            ob_ject.acc_y = -1 * F_y / ob_ject.mass

        if keys[down]:
            ob_ject.acc_y = F_y / ob_ject.mass

        if keys[extra]:
            ob_ject.vel_y = -85
            ob_ject.vel_x = 80

        ob_ject.vel_y += g
        ob_ject.vel_x += ob_ject.acc_x
        ob_ject.vel_y += ob_ject.acc_y
        ob_ject.x += ob_ject.vel_x
        ob_ject.y += ob_ject.vel_y

    def boundary_func(self, ob_ject):
        if ob_ject.x < 50 or ob_ject.x > 1450:
            ob_ject.x = max(50, min(1450, ob_ject.x))
            ob_ject.vel_x = 0
        if ob_ject.y < 50 or ob_ject.y > 840:
            ob_ject.y = max(50, min(840, ob_ject.y))
            ob_ject.vel_y = 0

    # def collision_func(self, ob_ject1, ob_ject2):
    #     ob1_velx = copy.copy(ob_ject1.vel_x)
    #     ob1_vely = copy.copy(ob_ject1.vel_y)
    #     ob2_velx = copy.copy(ob_ject2.vel_x)
    #     ob2_vely = copy.copy(ob_ject2.vel_y)
    #     center_dist = sqrt((ob_ject2.x - ob_ject1.x) ** 2 + (ob_ject2.y - ob_ject1.y) ** 2)
    #     if center_dist <= 100:
    #         ob_ject1.vel_x = ob2_velx
    #         ob_ject1.vel_y = ob2_vely
    #         ob_ject2.vel_x = ob1_velx
    #         ob_ject2.vel_y = ob1_vely

    def gravity_func(self, ob_ject1, ob_ject2):
        pass


if __name__ == "__main__":
    pyg.init()
    win = pyg.display.set_mode((1500, 900))
    pyg.display.set_caption('PHYSICS ENGINE')

    # ___Globals___
    mainloop = True
    jump = False
    F_x = 1250
    F_y = 1750
    coeff_fric = 0.15
    friction_x = 0
    friction_y = 0
    g = 9.8
    G = 6.67 * 10 ** (-11)

    # ___Objects___
    circ = Objects(100, 1250, 0, 0, 0, 0, 100, 0.5)
    circ_2 = Objects(1200, 900, 0, 0, 0, 0, 100, 0.5)
    rect = Objects(0, 890, 0, 0, 0, 0, 100, 0.2)

    A = ObjectFunctions()

    # main game loop
    while mainloop:
        pyg.time.delay(50)

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                mainloop = False

        # ___movements___
        A.movement_func(circ, pyg.K_UP, pyg.K_DOWN, pyg.K_LEFT, pyg.K_RIGHT, pyg.K_SPACE)
        A.movement_func(circ_2, pyg.K_w, pyg.K_s, pyg.K_a, pyg.K_d, pyg.K_LSHIFT)
        win.fill((0, 0, 0))

        # ___boundaries and collision___
        A.boundary_func(circ)
        A.boundary_func(circ_2)
        # A.collision_func(circ, circ_2)

        # __gravity__
        A.gravity_func(circ, circ_2)

        # ___friction___
        A.fric_func(circ)
        A.fric_func(circ_2)

        # ___object animation___
        objct = pyg.draw.circle(win, (100, 100, 255), (round(circ.x), round(circ.y)), 50)
        objet_2 = pyg.draw.circle(win, (255, 100, 100), (round(circ_2.x), round(circ_2.y)), 50)
        floor = pyg.draw.rect(win, (150, 75, 0), (rect.x, rect.y, 1500, 10))

        pyg.display.update()

    pyg.quit()


# __new collision algorithm__

''' If that is the case, then you apply the equations that change their velocities, and THEN, the most important step
Before making them move with their new velocities, you first reset their positions to make sure they will not still overlap after moving dt through time
So, lets say two balls just are currently colliding (their distance is lower thant he sum of their radii)
You handle the collision by changing their velocities
You change their positions to ensure they are just touching each other (sum of the radii is the same as their distance)
And THEN you update the object position with object.position += object.v*dt
This method works pretty well
Check out this thing I made today for a university assignment '''
