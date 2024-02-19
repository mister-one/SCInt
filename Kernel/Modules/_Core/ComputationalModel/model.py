from Kernel.CoreMentalModel.InputOutputTransformer.model import InputOutputTransformer
from Kernel.CoreMentalModel.GTW.model import GTW
from Kernel.CoreMentalModel._BaseMentalModel.model import BaseMentalModel
from Kernel.Utils.generate_message_template import generate_message_template


class CoreMentalModel(BaseMentalModel):
    def __init__(self, input_data=None):
        super().__init__()
        self.input_data = input_data
        self.pulse()
        self.input()
        self.optimization_function()
        self.logical_resoning()
        

    # -------------------
    # 0. Pulse
    def pulse(self):
        # self.pulse_type = "trigger_only"
        # self.pulse_frequency = None
        # self.remaining_lifespan = float("inf")
        return None

    # -------------------
    # 1. Inputs + context
    def input(self):
        self.input_schema: dict = {
            "$schema": "1-0-0",
            "type": "dict",
            "properties": {"input_data": {"type": "JSON|list|.txt"}},
            "required": ["input_data"],
            "allowadditionalProperties": False,
        }
        print(f'input received {self.input_data}')


    # -------------------
    # 2. Loss fucntion/ Optimization objective
    def optimization_function(self):
        self.optimization_objective: str = """
        OBJECTIVE: Given the request return the best answer possible
        FEATURES:
          1. MAX(response_speed)
          2. MAX(response_accuracy)
          3. MIN(cost)
        """
        print(f"My objective is to {self.optimization_objective}")

    # -------------------
    # 3. Architecure / LS (logical-steps) / Logical reasoning
    def logical_resoning(self):
        self.logic_steps = [
            "<step_0> given the request use @utils.ask_chatgpt to see if it can give a correct answer to the question",
            "<step_1> in case the response to <step_0> is not good then decide which MentalModel to call next"
            "<step_2> contact the relevant provider",
            "<step_3> return the response",
            "<step_time_error> Keep track of how long is it taking to recive the response and if its taking more than 10min then quit",
        ]
        """
        1. Call LLM with the Query::"What are my benefits?"
        2. The answer get appended in Inbound Queue and the
            2.1 ATT
            2.2 GTW
        3. 
        """
        # self.nn_parameters = {"temperature": 1.3, "bias": 0, "variance": 1}

        # self.logic_structure = [
        #     {
        #         "_layer_priority": "0", 
        #         "node_step_id": "step_0", 
        #         "_conditions": []
        #     },
        #     {
        #         "_layer_priority": "1",
        #         "config": {
        #             "trigger": "hierarchy_default",
        #             "retries": 10,
        #             "_conditions_chaining": "condition_1 OR (condition_2 and condition_3)",
        #         },
        #         "node_step_id": "step_1",
        #         "_conditions": [
        #             {
        #                 "condition_id": 1,
        #                 "condition_type": "hierarchical_dependency",
        #                 "condition_origin": "step_0",
        #                 "condition_logic": "Await previous task completion but execute anyway",
        #             }
        #         ],
        #     },
        # ]
    

    # -------------------
    # 4. Output
    def return_output(self):
        pass
        # self.outputs_schema: dict = {
        #     "$schema": "1-0-0",
        #     "type": "object",
        #     "properties": {
        #         "input_name": {"type": "string", "example": "What is 2 + 2?"},
        #         "bannerId": {"type": "string"},
        #     },
        #     "required": ["bannerId"],
        #     "allowadditionalProperties": True,
        # }



# input_message = {
#     "raw_input_source": ["Antonio cameo", "luciano ++ Moggi"], 
#     "target_schema": ["first_name", "last_name"]
#     }

# i = InputOutputTransformer(input_message)

# i.step_0().get("message")


# g = GTW()
# g.data


# g.optimization_objective

c = CoreMentalModel({"What is the score of the user?"})

c.logic_steps

c.start_thinking()
