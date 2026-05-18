from physics import *
from destinations import get_destinations, get_distance, list_destinations

print("================================================")
print("         RELATIVISTIC TRAVEL SIMULATOR          ")
print("================================================")
print("# -- Welcome to your Space Travel Simulator -- #")
print("================================================")
print("")
print("Available destinations")
print("")
list_destinations()
print("")
destine = input("Select your destination:")
print("")
velocity = float(input("White your velocity:"))

if validate_velocity(velocity):
    print("Valid velocity. Calculating...")

    result_lorentz = lorentz_factor(velocity)
    print(result_lorentz)

    result_destine = get_distance(destine)
    distance = result_destine[1]
    result_time_earth = time_on_earth(distance, velocity)
    print(result_time_earth)

    result_traveler = time_for_traveler(distance, velocity)
    print(result_traveler)

    result_contracted = contracted_distance(distance, velocity)
    print(result_contracted)

    massKg = 1
    result_energy = relativistic_energy(velocity, massKg)
    print(result_energy)

else:
    print("Invalid velocity. Must be between 0 and 1.")







