import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11 

# 1 == Earth, 2 == Moon
# m == Mass, v == Velocity, r == distance, p == point
m1, m2 = 5.97e24, 7.35e22 

moon_velocity = 1022
# Earth velocity is opposite to Moon's and scaled by mass ratio
# momentum = mass * velocity
# total momentum = momentum of earth + momentum of moon = 0
# m1 * v1 + m2 * v2 = 0
# thus: m1 * v1 = -m2 *v2
# or: v1 = - v2 * m2) / m1

earth_velocity = -moon_velocity * m2 / (m1 + m2)
moon_velocity = moon_velocity * m1 / (m1 + m2)  # Adjust Moon velocity relative to center of mass

v1 = np.array([0.0, earth_velocity])
v2 = np.array([0.0, moon_velocity])
#v1, v2 = np.array([0.0, 0.0]), np.array([0.0, 1022.0])
# The Moon is 384,400 km away from Earth
p1, p2 = np.array([0.0, 0.0]), np.array([3.844e8, 0.0])

dt = 50
steps = 100000
positions_earth = []
positions_moon = []
positions_earth.append(p1.copy())
positions_moon.append(p2.copy())

for i in range(steps):
    # p2 - p1 results in a vector pointing from Earth to the Moon
    r_vector = p2 - p1
    r_magnitude = np.linalg.norm(r_vector) 
    
    f_magnitude = G * m1 * m2 / r_magnitude**2

    r_unit_vector = r_vector / r_magnitude
    f_vector = f_magnitude * r_unit_vector

    a1 = f_vector / m1
    a2 = -f_vector / m2 

    v1 += a1 * dt
    v2 += a2 * dt
    
    p1 += v1 * dt
    p2 += v2 * dt

    positions_earth.append(p1.copy())
    positions_moon.append(p2.copy())

positions_earth = np.array(positions_earth)
positions_moon = np.array(positions_moon)

plt.plot(positions_earth[:, 0], positions_earth[:, 1], label="Earth's Orbit")
plt.plot(positions_moon[:, 0], positions_moon[:, 1], label="Moon's Orbit")
plt.scatter(0, 0, color="blue", label="Earth", s=100)  # Earth at the center
plt.scatter(positions_moon[0, 0], positions_moon[0, 1], color="gray", label="Moon at start", s=50)

plt.xlabel("x position (m)")
plt.ylabel("y position (m)")
plt.legend()
plt.grid(True)
plt.title("Earth-Moon Gravitational Interaction")
plt.axis('equal')  # Make the plot aspect ratio 1:1
plt.show()

