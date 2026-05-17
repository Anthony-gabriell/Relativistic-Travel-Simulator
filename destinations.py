# A função desse modulo é armazenar o catalogo de destinos espaciais com suas distancias reais em anos-luz

destinations = {

"1": ("Proxima Centauri", 4.24, "light-years"),
"2": ("Alpha Centauri", 4.37, "light-years"),
"3": ("Sirius", 8.60, "light-years"),
"4": ("Vega", 25.00, "light-years"),
"5": ("Andromeda", 2537000.00, "light-years")
}

def get_destinations ():
    return destinations

def list_destinations ():
    for name, (destine, distance, unit) in destinations.items():
        print(f"{name} -  {distance} {unit}")

def get_distance(name):
    return destinations[name]


