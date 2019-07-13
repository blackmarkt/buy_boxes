import numpy as np
from qreit.metros.census_tract import get_census_tract

class BuyBox:
    
    def __init__(self, street, city, state, zip_code, 
                 beds, baths, price, year_built, caprate,
                 pool, power_lines, major_street):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.beds = beds
        self.baths = baths
        self.price = price
        self.year_built = year_built
        self.caprate = caprate
        self.pool = pool
        self.power_lines = power_lines
        self.major_street = major_street
        
    def pull_census_tract(self):
        try:
            self.census_tract = get_census_tract(self.street, self.city, self.state, self.zip_code)
            if self.census_tract:
                pass
            else:
                self.census_tract = np.nan
        except:
            self.census_tract = np.nan