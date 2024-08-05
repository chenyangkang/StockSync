


import gzip
import pickle
import os

class stocksearcher():
    
    def __init__(self) -> None:
        self.distance_matrix = self.load_distance_matrix()
        self.distance_matrix = self.distance_matrix.set_index('code')
        pass

    def load_distance_matrix(self):
        
        base_path = os.path.dirname(__file__)
        relative_path = os.path.join(base_path, '../data/nasdaq_stock_info/matrix.pkl.gz')
        
        with gzip.open(relative_path, 'rb') as f:
            a = pickle.load(f)
            
        return a
            
    def search(self, code, n):
        '''
        search the top n similar stocks
        '''

        res = list(self.distance_matrix[code].sort_values().iloc[1:n+1].index)
        return res
    
            
        