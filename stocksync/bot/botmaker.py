
import pandas as pd

from ..stocksearch import stocksearcher
from ..FeatureEngineering import engineer


class bot():
    def __init__(self, code) -> None:
        self.code = code
        # self.future_days = future_days

    def find_matched_stock(self, n=10):
        '''
        Find the top n similar stock interms of their business and financial performance
        
        Args:

        '''
        
        searcher = stocksearcher()
        tops = searcher.search(self.code, n=n)
        self.top_target_stocks = tops
    
    def process_stocks(self):
        '''
        Load these top similar stocks, chunk into pieces, and do feature engineering.
        '''
        
        feature_engineer = engineer()
        
        feature_list = []
        
        for stock in self.top_target_stocks:
            features  = feature_engineer.process(stock)
            feature_list.append(features)
            
        features = pd.concat(feature_list, axis=0).reset_index(drop=True)
        
        pass
        
        
        