# Dictionary of gravity ratios for each planet
GRAVITY_RATIOS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def planetary_weight():
    earth_weight = float(input("Enter a weight on Earth: "))  # Get user input
    planet = input("Enter a planet: ")  # Get the planet name

    # Calculate weight on the chosen planet
    if planet in GRAVITY_RATIOS:
        new_weight = round(earth_weight * GRAVITY_RATIOS[planet], 2)
        print(f"The equivalent weight on {planet}: {new_weight}")
    else:
        print("Invalid planet name. Please try again.")

# Run the function
planetary_weight()
