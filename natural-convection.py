# Given data
mu = 1.665 * 10**-5  # kg/(m·s) (Dynamic viscosity)
Cp = 1.005 * 10**3  # J/(kg·K) (Specific heat capacity)
Ts = 273.15  # K (Surface temperature of housing)
T_inf = 263.15  # K (Ambient temperature)
L = 0.15  # m (Diameter of housing)
k = 2.359 * 10**-2  # W/(m·K) (Thermal conductivity)
nu = 1.243 * 10**-5  # m^2/s (Kinematic viscosity)
g = 9.806  # m/s^2 (Acceleration due to gravity)

# Calculating Prandtl number (Pr)
Pr = (mu * Cp) / k
print(f"Prandtl Number (Pr) = {Pr:.4f}")

# Correct formula for thermal expansion coefficient (β)
T_avg = (Ts + T_inf) / 2
beta = 1 / T_avg
print(f"Thermal Expansion Coefficient (β) = {beta:.4f}")

# Calculating Grashof number (Gr_L)
Gr_L = (g * beta * (Ts - T_inf) * L**3) / nu**2
print(f"Grashof Number (Gr_L) = {Gr_L:.4f}")

# Calculating Rayleigh number (Ra_L)
Ra_L = Gr_L * Pr
print(f"Rayleigh Number (Ra_L) = {Ra_L:.4f}")

# Calculating Nusselt number (Nu)
Nu = (0.6 + (0.387 * Ra_L**(1/6)) / ((1 + (0.559 / Pr)**(9/16))**(8/27)))**2
print(f"Nusselt Number (Nu) = {Nu:.4f}")

# Calculating heat transfer coefficient (h)
h = (Nu * k) / L
print(f"Heat Transfer Coefficient (h) = {h:.4f} W/(m²·K)")
