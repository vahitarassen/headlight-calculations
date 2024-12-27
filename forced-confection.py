# Given data
mu = 1.51 * 10**-5  # kg/(m·s) (Dynamic viscosity)
Cp = 1.006 * 10**3  # J/(kg·K) (Specific heat capacity)
v = 26.8  # m/s (Velocity)
L = 0.15  # m (Diameter of lens)
k = 2.122 * 10**-2  # W/(m·K) (Thermal conductivity)
rho = 1.514  # kg/m^3 (Density)

# Calculating Prandtl number (Pr)
Pr = (mu * Cp) / k
print(f"Prandtl Number (Pr) = {Pr:.4f}")

# Calculating Reynolds number (Re)
Re = (rho * v * L) / mu
print(f"Reynolds Number (Re) = {Re:.4f}")

# Calculating Nusselt number (Nu)
Nu = 0.027 * (Re**0.805) * (Pr**(1/3))
print(f"Nusselt Number (Nu) = {Nu:.4f}")

# Calculating heat transfer coefficient (h)
h = (Nu * k) / L
print(f"Heat Transfer Coefficient (h) = {h:.4f} W/(m²·K)")
