class City:
    def __init__ (self, name: str, population: float, percentage: float):
        self.name = name
        self.population = population
        self.percentage = percentage / 100

new_york: City = City('New York (PI)', float(input('População de New York: ')), float(input('Porcentagem de crescimento de New York: ')))
uaua: City = City('Uauá (BA)', float(input('População de Uauá: ')), float(input('Porcentagem de crescimento de Uauá: ')))

def compare_cities (city1: City, city2: City):
    small: float = City
    big: float = City
    year: int = 0
    
    if city1.population > city2.population:
        print(f'A população de {city1.name} é maior do que a de {city2.name}')
        small = city2
        big = city1
    elif city1.population < city2.population:
        print(f'A população de {city2.name} é maior do que a de {city1.name}')
        small = city1
        big = city2
    elif city1.population == city2.population:
        print('As duas cidades tem a mesma população')
        return
    
    while small.population < big.population:
        small.population += small.population * small.percentage
        big.population += big.population * big.percentage
        year += 1
        print(f'População de {small.name} é {small.population} no ano {year}\nPopulação de {big.name} é {big.population} no ano {year}')
    
    print(f'Depois de {year} anos a cidade {small.name} ultrapassa a cidade {big.name}')

compare_cities(uaua, new_york)