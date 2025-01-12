import math

eV_to_J = 1.60218e-19  # Conversion factor from eV to Joules
h = 6.626e-34  # Planck's constant in J·s


# Full periodic table data (Z, A, Ionization Energy in eV)
elements = [
    {"name": "Hydrogen", "Z": 1, "A": 1, "E_electron": 13.6},
    {"name": "Helium", "Z": 2, "A": 4, "E_electron": 24.6},
    {"name": "Lithium", "Z": 3, "A": 7, "E_electron": 5.39},
    {"name": "Beryllium", "Z": 4, "A": 9, "E_electron": 9.32},
    {"name": "Boron", "Z": 5, "A": 11, "E_electron": 8.30},
    {"name": "Carbon", "Z": 6, "A": 12, "E_electron": 11.26},
    {"name": "Nitrogen", "Z": 7, "A": 14, "E_electron": 14.53},
    {"name": "Oxygen", "Z": 8, "A": 16, "E_electron": 13.62},
    {"name": "Fluorine", "Z": 9, "A": 19, "E_electron": 17.42},
    {"name": "Neon", "Z": 10, "A": 20, "E_electron": 21.56},
    {"name": "Sodium", "Z": 11, "A": 23, "E_electron": 5.14},
    {"name": "Magnesium", "Z": 12, "A": 24, "E_electron": 7.64},
    {"name": "Aluminum", "Z": 13, "A": 27, "E_electron": 5.99},
    {"name": "Silicon", "Z": 14, "A": 28, "E_electron": 8.15},
    {"name": "Phosphorus", "Z": 15, "A": 31, "E_electron": 10.49},
    {"name": "Sulfur", "Z": 16, "A": 32, "E_electron": 10.36},
    {"name": "Chlorine", "Z": 17, "A": 35, "E_electron": 12.97},
    {"name": "Argon", "Z": 18, "A": 40, "E_electron": 15.76},
    {"name": "Potassium", "Z": 19, "A": 39, "E_electron": 4.34},
    {"name": "Calcium", "Z": 20, "A": 40, "E_electron": 6.11},
    {"name": "Scandium", "Z": 21, "A": 45, "E_electron": 6.56},
    {"name": "Titanium", "Z": 22, "A": 48, "E_electron": 6.83},
    {"name": "Vanadium", "Z": 23, "A": 51, "E_electron": 6.74},
    {"name": "Chromium", "Z": 24, "A": 52, "E_electron": 6.77},
    {"name": "Manganese", "Z": 25, "A": 55, "E_electron": 7.43},
    {"name": "Iron", "Z": 26, "A": 56, "E_electron": 7.87},
    {"name": "Cobalt", "Z": 27, "A": 59, "E_electron": 7.86},
    {"name": "Nickel", "Z": 28, "A": 58, "E_electron": 7.64},
    {"name": "Copper", "Z": 29, "A": 63, "E_electron": 7.73},
    {"name": "Zinc", "Z": 30, "A": 64, "E_electron": 9.39},
    {"name": "Gallium", "Z": 31, "A": 69, "E_electron": 5.99},
    {"name": "Germanium", "Z": 32, "A": 74, "E_electron": 7.90},
    {"name": "Arsenic", "Z": 33, "A": 75, "E_electron": 9.81},
    {"name": "Selenium", "Z": 34, "A": 79, "E_electron": 9.75},
    {"name": "Bromine", "Z": 35, "A": 80, "E_electron": 11.81},
    {"name": "Krypton", "Z": 36, "A": 84, "E_electron": 14.00},
    {"name": "Rubidium", "Z": 37, "A": 85, "E_electron": 4.18},
    {"name": "Strontium", "Z": 38, "A": 88, "E_electron": 5.69},
    {"name": "Yttrium", "Z": 39, "A": 89, "E_electron": 6.38},
    {"name": "Zirconium", "Z": 40, "A": 91, "E_electron": 6.84},
    {"name": "Niobium", "Z": 41, "A": 93, "E_electron": 6.88},
    {"name": "Molybdenum", "Z": 42, "A": 96, "E_electron": 7.10},
    {"name": "Technetium", "Z": 43, "A": 98, "E_electron": 7.28},
    {"name": "Ruthenium", "Z": 44, "A": 101, "E_electron": 7.36},
    {"name": "Rhodium", "Z": 45, "A": 103, "E_electron": 7.46},
    {"name": "Palladium", "Z": 46, "A": 106, "E_electron": 8.34},
    {"name": "Silver", "Z": 47, "A": 107, "E_electron": 7.58},
    {"name": "Cadmium", "Z": 48, "A": 112, "E_electron": 8.99},
    {"name": "Indium", "Z": 49, "A": 115, "E_electron": 5.79},
    {"name": "Tin", "Z": 50, "A": 119, "E_electron": 7.34},
    {"name": "Antimony", "Z": 51, "A": 122, "E_electron": 8.64},
    {"name": "Tellurium", "Z": 52, "A": 128, "E_electron": 9.01},
    {"name": "Iodine", "Z": 53, "A": 127, "E_electron": 10.45},
    {"name": "Xenon", "Z": 54, "A": 131, "E_electron": 12.13},
    {"name": "Cesium", "Z": 55, "A": 133, "E_electron": 3.89},
    {"name": "Barium", "Z": 56, "A": 137, "E_electron": 5.21},
    {"name": "Lanthanum", "Z": 57, "A": 139, "E_electron": 5.58},
    {"name": "Cerium", "Z": 58, "A": 140, "E_electron": 5.54},
    {"name": "Praseodymium", "Z": 59, "A": 141, "E_electron": 5.47},
    {"name": "Neodymium", "Z": 60, "A": 144, "E_electron": 5.53},
    {"name": "Promethium", "Z": 61, "A": 145, "E_electron": 5.58},
    {"name": "Samarium", "Z": 62, "A": 150, "E_electron": 5.64},
    {"name": "Europium", "Z": 63, "A": 152, "E_electron": 5.67},
    {"name": "Gadolinium", "Z": 64, "A": 157, "E_electron": 6.15},
    {"name": "Terbium", "Z": 65, "A": 159, "E_electron": 5.86},
    {"name": "Dysprosium", "Z": 66, "A": 163, "E_electron": 5.93},
    {"name": "Holmium", "Z": 67, "A": 165, "E_electron": 6.02},
    {"name": "Erbium", "Z": 68, "A": 167, "E_electron": 6.10},
    {"name": "Thulium", "Z": 69, "A": 169, "E_electron": 6.18},
    {"name": "Ytterbium", "Z": 70, "A": 173, "E_electron": 6.25},
    {"name": "Lutetium", "Z": 71, "A": 175, "E_electron": 5.43},
    {"name": "Hafnium", "Z": 72, "A": 178, "E_electron": 6.83},
    {"name": "Tantalum", "Z": 73, "A": 181, "E_electron": 7.55},
    {"name": "Tungsten", "Z": 74, "A": 184, "E_electron": 7.98},
    {"name": "Rhenium", "Z": 75, "A": 186, "E_electron": 7.88},
    {"name": "Osmium", "Z": 76, "A": 190, "E_electron": 8.70},
    {"name": "Iridium", "Z": 77, "A": 192, "E_electron": 9.10},
    {"name": "Platinum", "Z": 78, "A": 195, "E_electron": 9.00},
    {"name": "Gold", "Z": 79, "A": 197, "E_electron": 9.22},
    {"name": "Mercury", "Z": 80, "A": 201, "E_electron": 10.44},
    {"name": "Thallium", "Z": 81, "A": 204, "E_electron": 6.11},
    {"name": "Lead", "Z": 82, "A": 207, "E_electron": 7.42},
    {"name": "Bismuth", "Z": 83, "A": 209, "E_electron": 7.29},
    {"name": "Polonium", "Z": 84, "A": 209, "E_electron": 8.42},
    {"name": "Astatine", "Z": 85, "A": 210, "E_electron": 9.30},
    {"name": "Radon", "Z": 86, "A": 222, "E_electron": 10.74},
    {"name": "Francium", "Z": 87, "A": 223, "E_electron": 4.07},
    {"name": "Radium", "Z": 88, "A": 226, "E_electron": 5.28},
    {"name": "Actinium", "Z": 89, "A": 227, "E_electron": 5.17},
    {"name": "Thorium", "Z": 90, "A": 232, "E_electron": 6.31},
    {"name": "Protactinium", "Z": 91, "A": 231, "E_electron": 5.89},
    {"name": "Uranium", "Z": 92, "A": 238, "E_electron": 6.19},
    {"name": "Neptunium", "Z": 93, "A": 237, "E_electron": 6.27},
    {"name": "Plutonium", "Z": 94, "A": 244, "E_electron": 6.02},
    {"name": "Americium", "Z": 95, "A": 243, "E_electron": 5.97},
    {"name": "Curium", "Z": 96, "A": 247, "E_electron": 5.99},
    {"name": "Berkelium", "Z": 97, "A": 247, "E_electron": 6.23},
    {"name": "Californium", "Z": 98, "A": 251, "E_electron": 6.30},
    {"name": "Einsteinium", "Z": 99, "A": 252, "E_electron": 6.42},
    {"name": "Fermium", "Z": 100, "A": 257, "E_electron": 6.50},
    {"name": "Mendelevium", "Z": 101, "A": 258, "E_electron": 6.58},
    {"name": "Nobelium", "Z": 102, "A": 259, "E_electron": 6.65},
    {"name": "Lawrencium", "Z": 103, "A": 262, "E_electron": 4.9},
    {"name": "Rutherfordium", "Z": 104, "A": 267, "E_electron": 6.00},
    {"name": "Dubnium", "Z": 105, "A": 270, "E_electron": 7.00},
    {"name": "Seaborgium", "Z": 106, "A": 271, "E_electron": 7.60},
    {"name": "Bohrium", "Z": 107, "A": 270, "E_electron": 8.00},
    {"name": "Hassium", "Z": 108, "A": 277, "E_electron": 8.90},
    {"name": "Meitnerium", "Z": 109, "A": 278, "E_electron": 9.00},
    {"name": "Darmstadtium", "Z": 110, "A": 281, "E_electron": 9.50},
    {"name": "Roentgenium", "Z": 111, "A": 282, "E_electron": 10.00},
    {"name": "Copernicium", "Z": 112, "A": 285, "E_electron": 10.50},
    {"name": "Nihonium", "Z": 113, "A": 286, "E_electron": 11.00},
    {"name": "Flerovium", "Z": 114, "A": 289, "E_electron": 11.50},
    {"name": "Moscovium", "Z": 115, "A": 289, "E_electron": 12.00},
    {"name": "Livermorium", "Z": 116, "A": 293, "E_electron": 12.50},
    {"name": "Tennessine", "Z": 117, "A": 294, "E_electron": 13.00},
    {"name": "Oganesson", "Z": 118, "A": 294, "E_electron": 13.50},
]

primordial_molecules = {
    "water": [
        {"element": "Hydrogen", "count": 2},
        {"element": "Oxygen", "count": 1}
    ],
    "methane": [
        {"element": "Carbon", "count": 1},
        {"element": "Hydrogen", "count": 4}
    ],
    "ammonia": [
        {"element": "Nitrogen", "count": 1},
        {"element": "Hydrogen", "count": 3}
    ],
    "carbon_dioxide": [
        {"element": "Carbon", "count": 1},
        {"element": "Oxygen", "count": 2}
    ],
    "hydrogen_cyanide": [
        {"element": "Hydrogen", "count": 1},
        {"element": "Carbon", "count": 1},
        {"element": "Nitrogen", "count": 1}
    ],
    "formaldehyde": [
        {"element": "Carbon", "count": 1},
        {"element": "Hydrogen", "count": 2},
        {"element": "Oxygen", "count": 1}
    ],
    "hydrogen_sulfide": [
        {"element": "Hydrogen", "count": 2},
        {"element": "Sulfur", "count": 1}
    ],
    "carbon_monoxide": [
        {"element": "Carbon", "count": 1},
        {"element": "Oxygen", "count": 1}
    ],
    "diatomic_hydrogen": [
        {"element": "Hydrogen", "count": 2}
    ],
    "diatomic_nitrogen": [
        {"element": "Nitrogen", "count": 2}
    ],
    "diatomic_oxygen": [
        {"element": "Oxygen", "count": 2}
    ],
    "ethanol": [
        {"element": "Carbon", "count": 2},
        {"element": "Hydrogen", "count": 6},
        {"element": "Oxygen", "count": 1}
    ],
    "glucose": [
        {"element": "Carbon", "count": 6},
        {"element": "Hydrogen", "count": 12},
        {"element": "Oxygen", "count": 6}
    ],
    "acetic_acid": [
        {"element": "Carbon", "count": 2},
        {"element": "Hydrogen", "count": 4},
        {"element": "Oxygen", "count": 2}
    ],
    "sulfur_dioxide": [
        {"element": "Sulfur", "count": 1},
        {"element": "Oxygen", "count": 2}
    ],
    "nitric_oxide": [
        {"element": "Nitrogen", "count": 1},
        {"element": "Oxygen", "count": 1}
    ],
    "ozone": [
        {"element": "Oxygen", "count": 3}
    ],
    "propane": [
        {"element": "Carbon", "count": 3},
        {"element": "Hydrogen", "count": 8}
    ],
    "butane": [
        {"element": "Carbon", "count": 4},
        {"element": "Hydrogen", "count": 10}
    ],
    "pentane": [
        {"element": "Carbon", "count": 5},
        {"element": "Hydrogen", "count": 12}
    ],
    "hexane": [
        {"element": "Carbon", "count": 6},
        {"element": "Hydrogen", "count": 14}
    ],
    "benzene": [
        {"element": "Carbon", "count": 6},
        {"element": "Hydrogen", "count": 6}
    ],
    "toluene": [
        {"element": "Carbon", "count": 7},
        {"element": "Hydrogen", "count": 8}
    ],
    "xylene": [
        {"element": "Carbon", "count": 8},
        {"element": "Hydrogen", "count": 10}
    ],
    "ethene": [
        {"element": "Carbon", "count": 2},
        {"element": "Hydrogen", "count": 4}
    ],
    "ethyne": [
        {"element": "Carbon", "count": 2},
        {"element": "Hydrogen", "count": 2}
    ],
    "chloroform": [
        {"element": "Carbon", "count": 1},
        {"element": "Hydrogen", "count": 1},
        {"element": "Chlorine", "count": 3}
    ],
    "carbon_tetrachloride": [
        {"element": "Carbon", "count": 1},
        {"element": "Chlorine", "count": 4}
    ],
    "hydrochloric_acid": [
        {"element": "Hydrogen", "count": 1},
        {"element": "Chlorine", "count": 1}
    ],
    "sodium_chloride": [
        {"element": "Sodium", "count": 1},
        {"element": "Chlorine", "count": 1}
    ],
    "potassium_permanganate": [
        {"element": "Potassium", "count": 1},
        {"element": "Manganese", "count": 1},
        {"element": "Oxygen", "count": 4}
    ],
    "calcium_carbonate": [
        {"element": "Calcium", "count": 1},
        {"element": "Carbon", "count": 1},
        {"element": "Oxygen", "count": 3}
    ],
    "magnesium_sulfate": [
        {"element": "Magnesium", "count": 1},
        {"element": "Sulfur", "count": 1},
        {"element": "Oxygen", "count": 4}
    ],
    "phosphoric_acid": [
        {"element": "Phosphorus", "count": 1},
        {"element": "Hydrogen", "count": 3},
        {"element": "Oxygen", "count": 4}
    ],
    "sulfuric_acid": [
        {"element": "Sulfur", "count": 1},
        {"element": "Hydrogen", "count": 2},
        {"element": "Oxygen", "count": 4}
    ],
    "nitric_acid": [
        {"element": "Nitrogen", "count": 1},
        {"element": "Hydrogen", "count": 1},
        {"element": "Oxygen", "count": 3}
    ],
    "hydrofluoric_acid": [
        {"element": "Hydrogen", "count": 1},
        {"element": "Fluorine", "count": 1}
    ],
    "ammonium_chloride": [
        {"element": "Nitrogen", "count": 1},
        {"element": "Hydrogen", "count": 4},
        {"element": "Chlorine", "count": 1}
    ],
        "acetone": [
        {"element": "Carbon", "count": 3},
        {"element": "Hydrogen", "count": 6},
        {"element": "Oxygen", "count": 1}
    ],
    "formic_acid": [
        {"element": "Carbon", "count": 1},
        {"element": "Hydrogen", "count": 2},
        {"element": "Oxygen", "count": 2}
    ],
    "hydrogen_peroxide": [
        {"element": "Hydrogen", "count": 2},
        {"element": "Oxygen", "count": 2}
    ],
    "propene": [
        {"element": "Carbon", "count": 3},
        {"element": "Hydrogen", "count": 6}
    ],
    "butene": [
        {"element": "Carbon", "count": 4},
        {"element": "Hydrogen", "count": 8}
    ],
    "cyclohexane": [
        {"element": "Carbon", "count": 6},
        {"element": "Hydrogen", "count": 12}
    ],
    "toluene": [
        {"element": "Carbon", "count": 7},
        {"element": "Hydrogen", "count": 8}
    ],
    "chlorine_trifluoride": [
        {"element": "Chlorine", "count": 1},
        {"element": "Fluorine", "count": 3}
    ],
    "nitrogen_trifluoride": [
        {"element": "Nitrogen", "count": 1},
        {"element": "Fluorine", "count": 3}
    ],
    "dichloromethane": [
        {"element": "Carbon", "count": 1},
        {"element": "Hydrogen", "count": 2},
        {"element": "Chlorine", "count": 2}
    ],
    "sodium_hydroxide": [
        {"element": "Sodium", "count": 1},
        {"element": "Oxygen", "count": 1},
        {"element": "Hydrogen", "count": 1}
    ],
    "potassium_chloride": [
        {"element": "Potassium", "count": 1},
        {"element": "Chlorine", "count": 1}
    ],
    "calcium_hydroxide": [
        {"element": "Calcium", "count": 1},
        {"element": "Oxygen", "count": 1},
        {"element": "Hydrogen", "count": 2}
    ],
    "sodium_bicarbonate": [
        {"element": "Sodium", "count": 1},
        {"element": "Carbon", "count": 1},
        {"element": "Oxygen", "count": 3},
        {"element": "Hydrogen", "count": 1}
    ],
    "ethyl_alcohol": [
        {"element": "Carbon", "count": 2},
        {"element": "Hydrogen", "count": 5},
        {"element": "Oxygen", "count": 1}
    ],
    "acetylene": [
        {"element": "Carbon", "count": 2},
        {"element": "Hydrogen", "count": 2}
    ],
    "hydrogen_chloride": [
        {"element": "Hydrogen", "count": 1},
        {"element": "Chlorine", "count": 1}
    ],
    "silicon_dioxide": [
        {"element": "Silicon", "count": 1},
        {"element": "Oxygen", "count": 2}
    ],
    "arsenic_trioxide": [
        {"element": "Arsenic", "count": 1},
        {"element": "Oxygen", "count": 3}
    ],
    "boron_trifluoride": [
        {"element": "Boron", "count": 1},
        {"element": "Fluorine", "count": 3}
    ],
    "phosphine": [
        {"element": "Phosphorus", "count": 1},
        {"element": "Hydrogen", "count": 3}
    ],
    "silane": [
        {"element": "Silicon", "count": 1},
        {"element": "Hydrogen", "count": 4}
    ],
    "diborane": [
        {"element": "Boron", "count": 2},
        {"element": "Hydrogen", "count": 6}
    ],
    "tetrafluoromethane": [
        {"element": "Carbon", "count": 1},
        {"element": "Fluorine", "count": 4}
    ],
    "nitrous_oxide": [
        {"element": "Nitrogen", "count": 2},
        {"element": "Oxygen", "count": 1}
    ],
    "sulfur_hexafluoride": [
        {"element": "Sulfur", "count": 1},
        {"element": "Fluorine", "count": 6}
    ],
    "phosphorus_trichloride": [
        {"element": "Phosphorus", "count": 1},
        {"element": "Chlorine", "count": 3}
    ],
    "methyl_chloride": [
        {"element": "Carbon", "count": 1},
        {"element": "Hydrogen", "count": 3},
        {"element": "Chlorine", "count": 1}
    ],
    "trichloromethane": [
        {"element": "Carbon", "count": 1},
        {"element": "Hydrogen", "count": 1},
        {"element": "Chlorine", "count": 3}
    ],
    "dichlorodifluoromethane": [
        {"element": "Carbon", "count": 1},
        {"element": "Hydrogen", "count": 1},
        {"element": "Chlorine", "count": 2},
        {"element": "Fluorine", "count": 2}
    ],
    "tetrachloromethane": [
        {"element": "Carbon", "count": 1},
        {"element": "Chlorine", "count": 4}
    ],
    "perfluorocyclopropane": [
        {"element": "Carbon", "count": 3},
        {"element": "Fluorine", "count": 6}
    ],
    "tungsten_trioxide": [
        {"element": "Tungsten", "count": 1},
        {"element": "Oxygen", "count": 3}
    ],
    "molybdenum_trioxide": [
        {"element": "Molybdenum", "count": 1},
        {"element": "Oxygen", "count": 3}
    ],
    "chromium_trioxide": [
        {"element": "Chromium", "count": 1},
        {"element": "Oxygen", "count": 3}
    ],
    "germanium_dioxide": [
        {"element": "Germanium", "count": 1},
        {"element": "Oxygen", "count": 2}
    ],
    "antimony_trioxide": [
        {"element": "Antimony", "count": 1},
        {"element": "Oxygen", "count": 3}
    ],
    "bismuth_trioxide": [
        {"element": "Bismuth", "count": 1},
        {"element": "Oxygen", "count": 3}
    ],
    "cobalt_chloride": [
        {"element": "Cobalt", "count": 1},
        {"element": "Chlorine", "count": 2}
    ],
    "nickel_sulfate": [
        {"element": "Nickel", "count": 1},
        {"element": "Sulfur", "count": 1},
        {"element": "Oxygen", "count": 4}
    ],
    "zinc_oxide": [
        {"element": "Zinc", "count": 1},
        {"element": "Oxygen", "count": 1}
    ],
    "copper_sulfate": [
        {"element": "Copper", "count": 1},
        {"element": "Sulfur", "count": 1},
        {"element": "Oxygen", "count": 4}
    ]
}


def calculate_cracking_frequency(energy_ev):
    # Convert energy from eV to Joules
    energy_J = energy_ev * eV_to_J

    # Calculate frequency
    frequency = energy_J / h
    return frequency


# Function to calculate binding energy (semi-empirical mass formula)
def calculate_binding_energy(Z, A):
    if A == 0:
        return 0
    return 15.75 * A - 17.8 * A**(2/3) - 0.711 * (Z * (Z - 1)) / A**(1/3)

# Function to calculate frequency ratio
def calculate_frequency_ratio(Z, A, E_electron, E_bind):
    if E_bind == 0:  # Avoid division by zero
        return float('inf')  # Large value indicates undefined frequency ratio
    Z_A_ratio = Z / A
    return (Z_A_ratio * (E_electron / E_bind))**38

# Represent a molecule as a list of atoms (in terms of their element symbol and count)
def calculate_molecule_properties(molecule):
    molecule_properties = {
        "molecular_weight": 0,
        "total_binding_energy": 0,
        "total_electron_energy": 0,
        "total_frequency_ratio": 0
    }

    for atom in molecule:
        element = next((e for e in elements if e['name'] == atom['element']), None)
        if element:
            Z = element['Z']
            A = element['A']
            E_electron = element['E_electron']
            E_bind = calculate_binding_energy(Z, A)
            freq_ratio = calculate_frequency_ratio(Z, A, E_electron, E_bind)
            
            # Add properties for the molecule
            molecule_properties['molecular_weight'] += A * atom['count']
            molecule_properties['total_binding_energy'] += E_bind * atom['count']
            molecule_properties['total_electron_energy'] += E_electron * atom['count']
            molecule_properties['total_frequency_ratio'] += freq_ratio * atom['count']
        else:
            print(f"Element {atom['element']} not found in the periodic table.")

    return molecule_properties

results = []
print(f"{'Molecule':<20}{'Molecule Cracking Frequency':<30}")
for molecule in primordial_molecules:
    molecule_properties = calculate_molecule_properties(primordial_molecules[molecule])
    print(f"{molecule:<25}{calculate_cracking_frequency(molecule_properties['total_binding_energy']):.2e} Hz")
    for atom in primordial_molecules[molecule]:
        element = next((e for e in elements if e['name'] == atom['element']), None)
        if element:
            Z = element["Z"]
            A = element["A"]
            E_electron = element["E_electron"]
            E_bind = calculate_binding_energy(Z, A)
            freq_ratio = calculate_frequency_ratio(Z, A, E_electron, E_bind)
            results.append({
                "Molecule": molecule,
                "Element": element["name"],
                "Z/A": Z / A,
                "E_bind (eV)": E_bind,
                "E_electron (eV)": E_electron,
                "Freq Ratio (f_electron / f_neutron)": freq_ratio,
            })

# Print results in tabular format for individual atoms
print(f"\n{'Molecule':<24}{'Element':<15}{'Z/A':<10}{'E_bind (eV)':<15}{'E_electron (eV)':<20}{'Freq Ratio':<15}")
print("-" * 65)
for result in results:
    print(f"{result['Molecule']:<24}{result['Element']:<15}{result['Z/A']:<10.3f}{result['E_bind (eV)']:<15.3f}{result['E_electron (eV)']:<20.3f}{result['Freq Ratio (f_electron / f_neutron)']:<15.3e}")
