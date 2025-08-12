from vpython import sphere, vector, rate, color
import random

particles = []

# Krijojmë 70 grimca, 50 të kuqe dhe 20 të gjelbra
for _ in range(50):
    p = sphere(
        pos=vector(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)),
        radius=0.2,
        color=color.red
    )
    p.velocity = vector(random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))
    particles.append(p)

for _ in range(20):
    p = sphere(
        pos=vector(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)),
        radius=0.2,
        color=color.green
    )
    p.velocity = vector(random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))
    particles.append(p)

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