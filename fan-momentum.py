# Predefined values for dimensions of the fan face
dim1 = 40  # First dimension of the fan face in mm
dim2 = 40  # Second dimension of the fan face in mm
dim3 = 10  # Depth of the fan in mm

# Volumetric flow rate in cubic feet per minute (CFM)
cfm = 7.24  # CFM value of the fan

# Air density in kg/m³ (standard air at sea level)
d = 1.225  # Standard air density

# Conversion factor from ft³/min to m³/s
conversion_factor = 0.0283168  # To convert cubic feet per minute to cubic meters per second

# Calculate the volume of the fan geometry (using symmetry, dividing by 2)
vol = dim1 * (dim2 / 2) * dim3 * 10 ** -9  # Volume in m³

# Calculate the area of the fan face (using symmetry, dividing by 2)
area = dim1 * (dim2 / 2) * 10 ** -6  # Area in m²

# Convert CFM to m³/s
cfm_modified = cfm * conversion_factor  # Volumetric flow rate in m³/s

# Calculate the mass flow rate in kg/s
mass_flow = d * cfm_modified  # Mass flow rate = density × volumetric flow rate

# Calculate the velocity of airflow in m/s
velocity = cfm_modified / area  # Velocity = volumetric flow rate / area

# Calculate the force in Newtons (adjusted for time, divided by 3600 to convert min to seconds)
force = mass_flow * velocity * (1 / 3600)  # Force = mass flow rate × velocity

# Calculate the momentum per unit volume in N/m³
momentum = force / vol  # Momentum = force / volume

# Output the result
print(f"The momentum is {momentum:.4f} N/m³")
