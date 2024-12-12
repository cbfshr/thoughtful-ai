# Thoughtful AI - Robotic Automation Factory - Sort Packages

# Constants defined for determining if a package is bulky or not
BULKY_PACKAGE_VOLUME = 1000000 # 1,000,000 cm^3
BULKY_PACKAGE_DIMENSION = 150 # 150 cm
PACKAGE_VOLUME_UNITS = "cm^3"
PACKAGE_DIMENSION_UNITS = "cm"

# The is_bulky_package function takes in the dimensions of a package and determines whether it is bulky or not depending on the following criteria:
# - A package is bulky if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ (see BULKY_PACKAGE_VOLUME)
# - ...or when one of its dimensions is greater or equal to 150 cm. (see BULKY_PACKAGE_DIMENSION)
def is_package_bulky(width, height, length):
    # Convert ints to floats
    if type(width) is int:
        width = float(width)
    if type(height) is int:
        height = float(height)
    if type(length) is int:
        length = float(length)

    # Type Validation
    if type(width) is not float or type(height) is not float or type(length) is not float:
        raise Exception("Width, Height, and Length must be numbers.") 

    # Width, Height, Length Validation
    if width <= 0 or height <= 0 or length <= 0:
        raise Exception("Width, Height, and Length cannot be less than or equal to 0.") 

    volume = width * height * length

    print(f"Determining if package is BULKY...\n- Width: {width}{PACKAGE_DIMENSION_UNITS}\n- Height: {height}{PACKAGE_DIMENSION_UNITS}\n- Length: {length}{PACKAGE_DIMENSION_UNITS}\n- Volume: {volume}{PACKAGE_VOLUME_UNITS}")

    if volume >= BULKY_PACKAGE_VOLUME:
        print(f"Package is BULKY\n")
        return True

    if width >= BULKY_PACKAGE_DIMENSION or height >= BULKY_PACKAGE_DIMENSION or length >= BULKY_PACKAGE_DIMENSION:
        print(f"Package is BULKY\n")
        return True

    print(f"Package is NOT bulky\n")
    return False

# Constants defined to determine the mass at which a package is considered heavy
HEAVY_PACKAGE_MASS = 20 # 20 kg
PACKAGE_MASS_UNITS = "kg"

# The is_package_heavy function takes in the mass of a package and determines whether or not it classifies as a heavy package based on the following criteria:
# - A package is **heavy** when its mass is greater or equal to 20 kg. (units are centimeters for the dimensions and kilogram for the mass)
def is_package_heavy(mass):
    # Convert ints to floats
    if type(mass) is int:
        mass = float(mass)
        
    # Type Validation
    if type(mass) is not float:
        raise Exception("Mass must be a number.") 

    # Width, Height, Lenght Validation
    if mass <= 0:
        raise Exception("Mass cannot be less than or equal to 0.") 

    print(f"Determining if package is HEAVY...\n- Mass: {mass}{PACKAGE_MASS_UNITS}")

    # If the mass of the package exceeeds
    if mass >= HEAVY_PACKAGE_MASS:
        print(f"Package is HEAVY\n")
        return True
    
    print(f"Package is NOT heavy\n")
    return False

# Constants for defining the package status strings
PACKAGE_STANDARD = "STANDARD"
PACKAGE_SPECIAL = "SPECIAL"
PACKAGE_REJECTED = "REJECTED"

# The sort function dispatches the packages in the following stacks:
# - STANDARD: standard packages (those that are not bulky or heavy) can be handled normally.
# - SPECIAL: packages that are either heavy or bulky can't be handled automatically.
# - REJECTED: packages that are both heavy and bulky are rejected.
#
# Returns a string matching the name of the stack where the package should go
def sort(width, height, length, mass):
    print(f"\n\n--------------------\nSorting Package...\n--------------------")

    is_bulky = is_package_bulky(width, height, length)
    is_heavy = is_package_heavy(mass)

    if is_bulky and is_heavy:
        return PACKAGE_REJECTED
    elif is_bulky or is_heavy:
        return PACKAGE_SPECIAL
    else:
        return PACKAGE_STANDARD
