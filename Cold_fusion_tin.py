import math

#constants
TIN_FUEL_CONSTANT = 3.5e22  # atoms ( Tin has a similar atomic density to Lithium, but a different atomic mass)
TIN_MASS = 118.71  # g/mol ( Tin has a higher atomic mass than Lithium)
TIN_SPECIFIC_HEAT_CAPACITY = 0.227  # J/g°C ( Tin has a lower specific heat capacity than Lithium)
HEAT_TRANSFER_COEFFICIENT = 66.6  # W/m²K ( Tin has a lower thermal conductivity than Lithium)
INITIAL_TEMPERATURE = 231.9  # °C ( Tin has a lower melting point than Lithium)
BASE_ENERGY_OUTPUT = 1040  # W ( Tin has a lower energy density than Lithium)

def calculate_temperature_increase(energy_output, volume):
    # Calculate the temperature increase
    temperature_increase = (energy_output / (TIN_MASS * TIN_SPECIFIC_HEAT_CAPACITY)) * (1 / (HEAT_TRANSFER_COEFFICIENT * volume))
    return temperature_increase

def calculate_number_of_atoms(volume):
    # Calculate the number of atoms of lithium held in a certain volume
    number_of_atoms = TIN_FUEL_CONSTANT * volume
    return number_of_atoms

def calculate_reaction_temperature(energy_output, volume):
    # Calculate the reaction temperature
    temperature_increase = calculate_temperature_increase(energy_output, volume)
    reaction_temperature = INITIAL_TEMPERATURE + temperature_increase
    return reaction_temperature

def adjust_energy_output(volume):
    # Adjust the energy output based on the volume
    adjusted_energy_output = BASE_ENERGY_OUTPUT * (1 + (volume / 0.1))
    return adjusted_energy_output

def cold_fusion_reaction(volume):
    # Calculate the adjusted energy output
    energy_output = adjust_energy_output(volume)

    # Calculate the temperature increase
    temperature_increase = calculate_temperature_increase(energy_output, volume)

    # Calculate the number of atoms of lithium held in a certain volume
    number_of_atoms = calculate_number_of_atoms(volume)

    # Calculate the reaction temperature
    reaction_temperature = calculate_reaction_temperature(energy_output, volume)

    return energy_output, temperature_increase, number_of_atoms, reaction_temperature

# Test the function
volume = 7.6e21  # m³ for the inner core of the planet Earth.
energy_output, temperature_increase, number_of_atoms, reaction_temperature = cold_fusion_reaction(volume)

print("Energy Output:", energy_output, "W")
print("Temperature Increase:", temperature_increase, "°C")
print("Number of Atoms:", number_of_atoms)
print("Reaction Temperature:", reaction_temperature, "°C")
