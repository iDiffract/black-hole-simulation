# gravitational_influence/spacetime_deformation.py

import numpy as np
import matplotlib.pyplot as plt
from einsteinpy.metric import Schwarzschild
from einsteinpy.geodesic import Timelike

class SpacetimeDeformation:
    def __init__(self, black_hole_mass):
        self.M_bh = black_hole_mass

    def simulate(self):
        time = np.linspace(0, 1e5, 1000)  # Time array

        # Schwarzschild Metric
        metric = Schwarzschild(M=self.M_bh)

        # Initial conditions for the geodesic
        position = [4e3, np.pi/2, 0.]
        momentum = [0., 0., 0.]
        geod = Timelike(metric, position, momentum, time)

        # Plotting
        plt.figure(figsize=(10, 8))
        plt.plot(geod.trajectory[:, 1], geod.trajectory[:, 2], label='Timelike Geodesic')
        plt.xlabel('r (in Schwarzschild radii)')
        plt.ylabel('θ (in radians)')
        plt.title('Spacetime Deformation around a Supermassive Black Hole')
        plt.legend()
        plt.show()