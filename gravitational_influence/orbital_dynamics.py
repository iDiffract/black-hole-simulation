# gravitational_influence/orbital_dynamics.py

import numpy as np
import matplotlib.pyplot as plt

class OrbitalDynamics:
    def __init__(self, black_hole_mass):
        self.M_bh = black_hole_mass
        self.G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2

    def orbital_velocity(self, r):
        return np.sqrt(self.G * self.M_bh / r)

    def simulate(self):
        M_sun = 1.989e30  # Solar mass, kg

        # Simulate orbits of stars around the black hole
        num_stars = 100
        star_distances = np.random.uniform(1e16, 1e18, num_stars)  # Random distances in meters
        star_velocities = self.orbital_velocity(star_distances)

        # Plotting the star distribution and velocities
        plt.figure(figsize=(10, 8))
        plt.scatter(star_distances, star_velocities, c='blue', label='Stars')
        plt.xlabel('Distance from Black Hole (m)')
        plt.ylabel('Orbital Velocity (m/s)')
        plt.title('Orbital Velocities of Stars Around a Supermassive Black Hole')
        plt.legend()
        plt.grid(True)
        plt.show()