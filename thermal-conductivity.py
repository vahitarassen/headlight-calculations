# Given data
L1 = 10**-4  # m (Anodized layer thickness)
L2 = 3 * 10**-3  # m (Aluminum layer thickness)
k1 = 1.62  # W/(m·K) (Anodized layer thermal conductivity)
k2 = 202.4  # W/(m·K) (Aluminum layer thermal conductivity)

# Equivalent thermal conductivity calculation
numerator = 2 * L1 + L2
denominator = (2 * L1) / k1 + L2 / k2
k_eq = numerator / denominator

# Output the result
print(f"Equivalent Thermal Conductivity (k_eq) = {k_eq:.4f} W/(m·K)")
