
class SecurityProtectionSystem:

    def __init__(self, data=None) -> None:
        self.name = 'SecurityProtectionSystem'
        self.objective = 'Make sure that private information is protected'
        self.data = data


    def execute(self):
        output = f'Executed {self.name}'
        return output
    

