import math

# Esse modulo vai realizar todos os calculos fisicos relativisticos
def lorentz_factor(velocity):
    return  1 / math.sqrt(1 - velocity**2)

def time_on_earth(distance, velocity):
    return distance / velocity

def time_for_traveler(distance, velocity):
    return time_on_earth(distance, velocity) / lorentz_factor(velocity)

def contracted_distance(distance, velocity):
    return distance / lorentz_factor(velocity)

def relativistic_energy(velocity, mass_kg):
    return ((lorentz_factor(velocity)) - 1) * mass_kg * (3e8)**2

# Validação da velocidade antes de qualquer calculo
def validate_velocity(v):
    return 0 < v < 1

