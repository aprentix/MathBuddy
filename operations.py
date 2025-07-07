import random

def generate_random_operation(complexity, operation):
    super_limit =  '9'*complexity
    num_one = random.randint(1,int(super_limit))
    num_two = random.randint(1,int(super_limit))
    return [num_one, operation, num_two]


def corregir(operation_vector):
    try:
        if operation_vector[1] == "+":
            return operation_vector[0] + operation_vector[2]
        elif operation_vector[1] == "-":
            return operation_vector[0] - operation_vector[2]
        elif operation_vector[1] == "*":
            return operation_vector[0] + operation_vector[2]
        elif operation_vector[1] == "/":
            return operation_vector[0] + operation_vector[2]
    except Exception:
        print(Exception)
