from Kernel.Modules._Core._SubModule._InputOutputTransformer.Utils.retrieve_module_schema import retrieve_module_schema

# ******************************
# InputOutputTransformer
# ******************************
class InputOutputTransformer:
    '''
    OBJECTIVE:
    The objective of this module is to transform the raw data into the target schema of the module_name provided.
    
    EXAMPLE:
    iot = InputOutputTransformer(
            raw_data={
                'data_type': 'string',
                'data': 'the member is called Mario, lives in london and is 34 years old'
            },
            module_name='@webe/financial_advisor'
        )
    '''
    def __init__(self, raw_data={}, module_name='Core') -> None:
        self.config = 'IOT config'
        self.raw_data = raw_data
        self.module_name = module_name
        self.target_shema = retrieve_module_schema(module_name=self.module_name) # module_name.input_schema

    # TODO: handle file to JSON
    # TODO: handle JSON to file
    # DONE: handle string --> JSON

    def execute(self):
        prompt = f'''
        You should transform this {self.raw_data} 
        into the dictionary with the following schema {self.target_shema}

        instructions:
        - retunr only the dictionary in ```
        '''
        print('EXECTUTED InputOutputTransformer')
        return prompt


if __name__ == '__main__':

    IoT = InputOutputTransformer()
    IoT.target_shema
    