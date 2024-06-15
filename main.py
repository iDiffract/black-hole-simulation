# main.py

from gravitational_influence import SpacetimeDeformation, OrbitalDynamics

def main():
    M_bh_solar_masses = 1e6  # Mass of the black hole in solar masses
    M_bh = M_bh_solar_masses * 1.989e30  # Convert to kg

    spacetime_deformation_simulator = SpacetimeDeformation(M_bh)
    spacetime_deformation_simulator.simulate()

    orbital_dynamics_simulator = OrbitalDynamics(M_bh)
    orbital_dynamics_simulator.simulate()

if __name__ == "__main__":
    main()