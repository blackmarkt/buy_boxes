import pandas as pd

from sqlalchemy import create_engine

from qreit.buy_boxes.buy_box import BuyBox

def pull_model_zips(strat):
    engine = create_engine('postgresql+psycopg2://postgres:@localhost/brightforge')
    query = f'SELECT * FROM zip_{strat};'
    df = pd.read_sql_query(query, engine)
    engine.dispose()
    df.rename(columns={'index':'zip'}, inplace=True)
    return df.set_index('zip')

class Prime_BuyBox(BuyBox):
    
    def __init__(self, street, city, state, zip_code, 
                 beds, baths, price, year_built, caprate,
                 pool, power_lines, major_street):
        self.strategy = 'prime'
    
        BuyBox.__init__(self, street, city, state, zip_code, 
                        beds, baths, price, year_built, caprate,
                        pool, power_lines, major_street)

    def _check_beds(self):
        if (self.beds > 1) and (self.beds <= 5):
            return True
        else:
            return False
        
    def _check_baths(self):
        if (self.baths > 1) and (self.baths <= 5):
            return True
        else:
            return False
        
    def _check_price(self):
        if (self.price >= 100000) and (self.price <= 400000):
            return True
        else:
            return False

    def _check_caprate(self):
        if self.caprate > 0.06:
            return True
        else:
            return False

    def _check_zip(self):
        prime_zips_ls = list(pull_model_zips(self.strategy).index)
        if self.zip_code in prime_zips_ls:
            return True
        else:
            return False

    def _check_year_built(self):
        if self.year_built >= 2000:
            return True
        else:
            return False
        
    def _check_pool(self):
        if self.pool:
            return False
        else:
            return True

    def _check_power_lines(self):
        if self.power_lines:
            return False
        else:
            return True
    
    def _check_major_street(self):
        if self.major_street:
            return False
        else:
            return True
        
    def check_buy_box(self):
        if all([self._check_beds(), self._check_beds(), self._check_baths(),
                self._check_price(), self._check_caprate(), self._check_zip(),
                self._check_year_built(), self._check_pool(), self._check_power_lines(),
                self._check_major_street()]):
            return True
        else:
            return False