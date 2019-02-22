
planets = ['Mars', 'Saturn', 'Earth', 'Jupiter', 'Mercury', 'Neptune', 'Venus', 'Uranus', 'Pluto' ]

#these masses are in kilograms
massofplanet = [.330*(10**24), 4.87*(10**24), 5.97*(10**24), 0.642*(10**24), 1898*(10**24), 568*(10**24), 86.8*(10**24), 102*(10**24), .0146 * (10**24)]


#these radii are in km
radii = [4879/2, 12,104/2, 12,756/2, 6792/2, 142,984/2, 120,536/2, 51,118/2, 49,528/2, 2370/2]

#Calculates weight in kg or lb for each planet
def new_weight():
    G = 6.67408 * (10**(-11))
    planet = input("This program allows you to enter your weight and choose any planet of choice within our Solar System to find out how much you'll weigh there. Which Planet shall we visit?:  {0}".format(planets))
    if planet == 'Mars':
        m = massofplanet[0]
        r = radii[0]
    if planet == 'Saturn':
        m = massofplanet[1]
        r = radii[1]
    if planet == 'Earth':
        m = massofplanet[2]
        r = radii[2]
    if planet == 'Jupiter':
        m = massofplanet[3]
        r = radii[3]
    if planet == 'Mercury':
        m = massofplanet[4]
        r = radii[4]
    if planet == 'Neptune':
        m = massofplanet[5]
        r = radii[5]
    if planet == 'Venus':
        m = massofplanet[6]
        r = radii[6]
    if planet == 'Uranus':
        m = massofplanet[7]
        r = radii[7]
    if planet == 'Pluto':
        print("Sadly Pluto was taken out of the Planetary System by some NASA scientists with nothing to do. They call it a dwarf star. But seeing as we still have lovely pneumonics like My Very Educated Mother Just Servied Us Nine Pizzas to remember the planets, we may as well let Pluto stay in our books.")
        m = massofplanet[8]
        r = radii[8]
    weight = float(input("Please enter your weight: "))
    weight_typ = (input("Is your weight in 'pounds' or 'kilograms'?: "))
    if weight_typ == 'pounds':
        weight = weight/2.2046
        print("Your weight on {0} is: ".format(planet) + str((G * weight * m)/(r**2))+ " lb.")
    else:
        print("Your weight on {0} is: ".format(planet) + str((G * weight * m)/(r**2))+ " kg.")



new_weight()
