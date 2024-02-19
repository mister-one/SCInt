import random
from typing import final
import os
import json
import re
# ComputationalModel
# DeterministicFuncion
from Kernel.Modules._Core.DeterministicFunction._post import _post
from Kernel.Modules._Core.DeterministicFunction._search_open_registry import _search_open_registry
# Utils
from Kernel.Modules._Core.Utils.ask_chatgpt import ask_chatgpt
# _Submodules
from Kernel.Modules._Core._SubModule._Attention.main import Attention
from Kernel.Modules._Core._SubModule._GTW.main import Gateway
from Kernel.Modules._Core._SubModule._InputOutputTransformer.main import InputOutputTransformer
from Kernel.Modules._Core._SubModule._SPS.main import SecurityProtectionSystem
from Kernel.Modules._Core._SubModule._STMemory.main import ShortTermMemory
from Kernel.Modules._Core._SubModule._LTMemory.main import LongTermMemory

os.environ['modules_path'] = "/Users/alessandro.rea/Desktop/scint-private-node/Kernel/Modules"

# input_string = "Please calculate the sum of 3,4,6,7"
# input_string = "Please calculate the sum of [4245,23523,235235]"
# input_string = "Please calculate the derivate of this equation"
# input_string = "Please calculate the average price by postcode of this data.csv"
# input_string = "Order my favourite pizza" 
# CHAIN --> [ '@mario11/order_pizza', 'sps+iot+sgtw']
# input_string = "increase the financial resilience of this person"


class Core:
    '''
    (input)--> || __pred__ | __exec__ || --> (output)
    
    *********************
    Example_1
    *********************

    input_objective = 'increase the financial resilience of the member'

    executions --> 
        [
            ('_pred', '_exe'),
            ('attention', 'very_important'),
            ('@webe/fin_adv', '__FAILED__'),
            ('ltm', '{age::11, risk_type::medium, location::uk}'),
            ('@webe/fin_adv', 'reccomendation is buy 80% stock and 20% bonds'),
            ('@webe/market_facilitator', 'IoT( 80% stock and 20% bonds )'),
        ]
    
    *********************
    Example_2
    *********************
    input_objective = 'help me buy my an electric bike'

    executions --> 
        [
            ('attention', 'very_important'),
            ('@webe/OptimalBikeFinder', 'IoT MISSING REQUIRED PARAMS'),
            ('ltm', '{age::11, risk_type::medium, location::uk}'),
            ('@webe/OptimalBikeFinder', 'Trek Bike city greavel, electric M'),
            ('@webe/market_facilitator', 'IoT(Trek Bike city greavel)'),
        ]
    '''

    # Attention, InputOutputTransformer, SecurityProtectionSystem, Gateway, LongTermMemory  

    def __init__(self):
        # config
        self.config_path = os.path.join(os.environ['modules_path'], '_Core', 'config.json')
        self.config = self.load_config()
        self.data = [
                ('_pred', '_exe')
                , ('attention', 'very_important')
            ]
        
        
    @property
    def _att(self):
        return Attention()
    
    @property
    def _gtw(self):
        return Gateway()
    
    @property
    def _iot(self):
        return InputOutputTransformer(self.data, self.name)
    
    @property
    def _sps(self):
        return SecurityProtectionSystem(self.data)
    
    @property
    def _stm(self):
        return ShortTermMemory()
    
    @property
    def _ltm(self):
        return LongTermMemory()
    
    def _post(self, diameter):
        # Your code here, you can use the _post function
        return _post(diameter)
    
    @final
    def _search_open_registry(self, question):
        return _search_open_registry(query=question)

    def __repr__(self):
        return f"{self.name}(data={self.data})"

    def test_(self):
        return self._sps.execute()
    
    def load_config(self):
        try:
            with open(self.config_path, 'r') as config_file:
                config_data = json.load(config_file)
                self.name = config_data.get('module').get('name')
                self.objective = config_data.get('module').get('objective')
                self.max_iteration_steps = config_data.get('module').get('max_iteration_steps') or 10
                return config_data
        except FileNotFoundError:
            print(f"Config file not found: {self.config_path}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in config file: {self.config_path}. Error: {e}")
            return None
    
    
    @staticmethod
    def ask_chatgpt(question):
        # You can call the imported function here
        return ask_chatgpt(question)
    

    def _pred(self):

        _available_modules = [
            'att',  # Attention
            'ltm',  # LongTermMemory
            '<eot>',
            ]
        
        _additional_modules = [
            '@mario11/order_pizza',
            '@webe/personal_shopper',
            '@webe/u23g0y8g1',
            '@webe/math_calc'
            ]
        
        _all_modules = _available_modules + _additional_modules

        if re.findall(r'\b(sum|add|plus|\+)\b', self.data[0], flags=re.IGNORECASE):
            self._prediction = '@scint/math_calc'
        else:
            self._prediction = _all_modules[random.randint(0, len(_all_modules) - 1)]

        return None

    
    def _exe(self):
        
        module_privacy_score = 100

        if module_privacy_score < 100:
            # *** // external \\ ***
            _exec_seq = ['sps'] + [self._prediction] + ['gtw']
        else:
            # *** // internal \\ ***
            _exec_seq = [self._prediction]

        _exec_data = []    
        for module in _exec_seq:
            print(f'_iot = Iot({module}, self.data)')
            print(f'_exec_data.append(run_module(module_name, _iot.tranform_data)')
        print(f'self.data.append(_exec_data)')

    
    def execute(self, input):
        # for _iteration_step in range(self._max_iteration_steps):
        #     if self._prediction == '<eot>':
        #         return 'task_completed'
        #     elif _iteration_step == self._max_iteration_steps - 1:
        #         return 'reached_max_iteration'
        #     else:
        #         # 1. ***** // prediction_layer \\ *****
        #         self._pred()
        #         # 2. ***** // execution_layer   \\ *****
        #         self._exe()
        output = f'output of the execution given the input: {input}'
        return output
                

input = 'order my favurite pizza'
c = Core()
c._search_open_registry(1)
c.execute(input)
c._att.execute()
c._gtw.execute()