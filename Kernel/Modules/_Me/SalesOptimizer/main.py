import os
from Kernel.Modules._Core.main import Core


class SalesOptimizer(Core):
    '''
    
    # SalesOptimizer
    # LeadScouter
    # StrategyFinder
    # ContentGenerator
    # MarketingChannelManager
        # EmailManager
        # GoogleAdsManager
    
    '''

    def __init__(self):
        Core.__init__(self)
        self.config_path = os.path.join(os.environ['modules_path'], '_Me', 'SalesOptimizer', 'config.json')
        self.config = self.load_config()

    def execute(self, input):
        print(self._iot.execute())
        return f'executed the SalesOptimizer with input: {input}'

           
so = SalesOptimizer()

so.execute(1)

so._search_open_registry(1)

so._iot.execute()

so._ltm.execute()

so.name

print(so)

