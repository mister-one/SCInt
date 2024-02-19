from Kernel.Modules._Core.DeterministicFunction._search_open_registry import _search
from Kernel.Modules._Core.DeterministicFunction._post import _post
from Kernel.Modules._Core.DeterministicFunction._generate_truth_cert import _generate_truth_cert
from Kernel.Modules._Core.DeterministicFunction._validate_truth_integrity import _validate_truth_integrity


# ******************************
# InputOutputTransformer
# ******************************

class MarketFacilitator():
    '''
    OBJECTIVE:
    The objective of this module is to help you buy and sell items.
    things i can do:
    1. Help you sell goods and services you want to provide
    2. Help you buy goods and services you need
    3. Place offers on your behalf
    4. accept offers on your behalf

    LOGIC:
    1. Buy 
        1.1 Search on OpenRegistry
        1.2 Identify the best item to buy
        1.3 Places offer to TruthCertify

    2. Sell
        1.1 Post a listing to the OpenRegistry
        
    3. Negotiate
        3.1 Process an offer accept_or_reject an offer received by the truth certifier
    
    EXAMPLE:
    iot = InputOutputTransformer(
            raw_data={
                'data_type': 'string',
                'data': 'the member is called Mario, lives in london and is 34 years old'
            },
            module_name='@webe/financial_advisor'
        )
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