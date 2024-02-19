from Kernel.Modules._Core.DeterministicFunction._search_open_registry import _search
from Kernel.Modules._Core.DeterministicFunction._post import _post
from Kernel.Modules._Core.DeterministicFunction._generate_truth_cert import _generate_truth_cert
from Kernel.Modules._Core.DeterministicFunction._validate_truth_integrity import _validate_truth_integrity

# ******************************
# InputOutputTransformer
# ******************************

class RealEstateAgent():
    '''
    OBJECTIVE:
    the objective of this module is to help you find the

    LOGIC:
    
    EXAMPLE:
    
    '''
    def __init__(
            self, 
            item={}, 
            action='buy',
            strategy='best_price',
            requires_explicit_authorization = True
            ) -> None:
        self.item = item
        self.action = action
        self.strategy = strategy
        self.requires_explicit_authorization = requires_explicit_authorization


    def retrive_market_items(self):
        pass

    def run(self):
        if self.action == 'buy':
            print('buy')
        elif self.action == 'sell':
            print('selling')


mf = MarketFacilitator()
mf.run()

_search('1')