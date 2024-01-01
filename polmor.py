class UK():

    def captial_city(self):
        print("London is the captial of UK")


    def language(self):
        print("English is th primary language")

class Spain():

    def captial_city(self):
        print("Madrid is the captial of Spain")


    def language(self):
        print("Spanish is th primary language")


def europe(eu):
    eu.captial_city()


queen = UK()
queen.captial_city()

zara = Spain()
zara.captial_city()


for country in (queen,zara):
    country.captial_city()
    country.language()