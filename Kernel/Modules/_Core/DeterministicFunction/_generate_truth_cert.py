import random

statement = {
    "statement": "1+1=2",
    "evidence":{}
}

def _generate_truth_cert(statement):
    random_bool = random.choice([True, False])
    print(statement.get('statement'))
    return random_bool



