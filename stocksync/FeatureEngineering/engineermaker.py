import pandas as pd
import numpy as np
import warnings
import os

class engineer():
    
    def __init__(self) -> None:
        pass
    
    def load_stock(self, code):
        base_path = os.path.dirname(__file__)
        relative_path = os.path.join(base_path, f'../data/historical_prices/{code}.csv')
        
        if not os.path.exists(relative_path):
            return warnings.warn(f'{code} historical data not available!')
        
        data = pd.read_csv(relative_path)
        return data
    
    def process(self, code):
        '''
        Load, feature engineering stocks
        '''
        
        data = self.load_stock(code)
        
        
        
        pass
    
    