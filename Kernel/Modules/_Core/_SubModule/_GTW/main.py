# ******************************
# Gateway
# ******************************

class Gateway:
    '''
    OBJECTIVE:
    The objective of this module is to help tarnsfer data in and out of the private node
    
    EXAMPLE:
    
    '''
    def __init__(self, origin='me', destination='openregistry', data={}) -> None:
        self.name = 'Gateway'
        self.origin = origin
        self.destination = destination
        self.data = data

    
    def execute(self):
        return f'EXECUTED {self.name}'
    

