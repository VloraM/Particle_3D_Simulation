from vpython import sphere, vector, rate, color
import random

particles = []

def create_sphere(position, radius, color_value):
    p = sphere(
        pos=vector(*position),
        radius=radius,
        color=color_value
    )
    p.velocity = vector(
        random.uniform(-0.1, 0.1),
        random.uniform(-0.1, 0.1),
        random.uniform(-0.1, 0.1)
    )
    particles.append(p)
    return p

def create_spheres(n, radius, color_value):
    for _ in range(n):
        create_sphere(
            (random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)),
            radius,
            color_value
        )

create_spheres(50, 0.2, color.red)
create_spheres(20, 0.2, color.green)

while True:
    rate(60)
    for p in particles:
        p.pos += p.velocity
        if abs(p.pos.x) > 5:
            p.velocity.x *= -1
        if abs(p.pos.y) > 5:
            p.velocity.y *= -1
        if abs(p.pos.z) > 5:
            p.velocity.z *= -1
