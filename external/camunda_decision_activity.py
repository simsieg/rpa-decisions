@activity
def camunda_decision_engine(camunda_engine_URL, decision_key, variable_names, variable_values, output_variable_name):
    """Camunda decision service

    Evaluate a decision table with camunda decision engine.

    :parameter camunda_engine_URL: URL to camunda engine (e.g. http://localhost:8080/engine-rest/)
    :type camunda_engine_URL: string

    :parameter decision_key: Key to identify decision "Decision_0tgwupa"
    :type decision_key: strings

    :parameter variable_names: Names of the input variables of the decision (comma separated list)
    :type variable_names: list of strings

    :parameter variable_values: Values of the corresponding variables of the decision (comma separated list)
    :type variable_values: list of strings

    :parameter output_variable_name: Output variable name of the decision table
    :type output_variable_name: string

    :return: Decision result
    :rtype: any

    Keywords
        decision, decision engine, decision table

    Icon
        la la-server
    """
    import requests

    if len(variable_names) != len(variable_values):
        raise Exception('Same number of input variable names and values required')

    variables = {}
    for i, name in enumerate(variable_names):
        variables[name] = { "value": variable_values[i] }

    task = {
        "variables" : variables
    }

    response = requests.post('{}decision-definition/key/{}/evaluate'.format(camunda_engine_URL, decision_key), json=task)
    
    return list(map(lambda x: x[output_variable_name]["value"], response.json()))
