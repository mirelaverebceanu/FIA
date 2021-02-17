from p5 import Vector
import numpy as np

CANVAS_RES = (800, 600)
PERCEPTION = 150
MAX_SPEED = 5
MAX_FORCE = 0.3


def edges(current):
    current.pos[0] %= CANVAS_RES[0]
    current.pos[1] %= CANVAS_RES[1]

def align(current, boids):
    steering = Vector(*np.zeros(2))
    total = 0
    avg_vector = Vector(*np.zeros(2))
    for boid in boids:
        if np.linalg.norm(np.array(boid.pos) - np.array(current.pos)) < PERCEPTION:
            avg_vector += Vector(*boid.vel)
            total += 1
    if total > 0:
        avg_vector /= total
        avg_vector = Vector(*avg_vector)
        avg_vector = avg_vector / np.linalg.norm(avg_vector) * MAX_SPEED
        steering = avg_vector - Vector(*current.vel)
    return steering

def cohesion(current, boids):
    steering = Vector(*np.zeros(2))
    total = 0
    center_of_mass = Vector(*np.zeros(2))
    for boid in boids:
        if np.linalg.norm(np.array(boid.pos) - np.array(current.pos)) < PERCEPTION:
            center_of_mass += Vector(*boid.pos)
            total += 1
    if total > 0:
        center_of_mass /= total
        center_of_mass = Vector(*center_of_mass)
        vec_to_com = center_of_mass - Vector(*current.pos)
        if np.linalg.norm(vec_to_com) > 0:
            vec_to_com = (vec_to_com / np.linalg.norm(vec_to_com)) * MAX_SPEED
        steering = vec_to_com - Vector(*current.vel)
        if np.linalg.norm(steering) > MAX_FORCE:
            steering = (steering / np.linalg.norm(steering)) * MAX_FORCE

    return steering

def separation(current, boids):
    steering = Vector(*np.zeros(2))
    total = 0
    avg_vector = Vector(*np.zeros(2))
    for boid in boids:
        distance = np.linalg.norm(np.array(boid.pos) - np.array(current.pos))
        if current.pos != boid.pos and distance < PERCEPTION:
            diff = Vector(*current.pos) - Vector(*boid.pos)
            diff /= distance
            avg_vector += diff
            total +=1
    if total > 0:
        avg_vector /= total
        avg_vector = Vector(*avg_vector)
        if np.linalg.norm(steering) > 0:
            avg_vector = (avg_vector / np.linalg.norm(steering)) * MAX_SPEED
        steering = avg_vector - Vector(*current.vel)
        if np.linalg.norm(steering) > MAX_FORCE:
            steering = (steering / np.linalg.norm(steering)) * MAX_FORCE

    return steering

def apply_behaviour(current, boids):
    alignment = align(current, boids)
    cohesionment = cohesion(current, boids)
    separationment = separation(current, boids)

    current.acceleration = Vector(*np.zeros(2))

    current.acceleration += alignment
    current.acceleration += cohesionment
    current.acceleration += separationment

def update_rock(current, boids):
    apply_behaviour(current, boids)

    position = Vector(*current.pos)
    velocity = Vector(*current.vel)
    acceleration = Vector(*((np.random.rand(2) - 0.5)/2))

    position += velocity
    velocity += acceleration

    if np.linalg.norm(velocity) > MAX_SPEED:
        velocity = velocity / np.linalg.norm(velocity) * MAX_SPEED

    current.acceleration = Vector(*np.zeros(2))