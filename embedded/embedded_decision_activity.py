@activity
def internal_decision(path, variable_names, variable_values, output_variable_name):
    """Internal decision engine

    Evaluate a decision table with pyDMNrules decision engine.

    :parameter path: File path to the decision table (.xlsx Excel worksheet)
    :type path: string

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
        la la-th
    """
    import pyDMNrules

    dmnRules = pyDMNrules.DMN()

    if len(variable_names) != len(variable_values):
        raise Exception('Same number of input variable names and values required')

    status = dmnRules.load(path)
    if 'errors' in status:
        raise Exception('{} has errors: {}'.format(path, str(status['errors'])))

    data = {}
    for i, name in enumerate(variable_names):
        data[name] = variable_values[i]

    return dmnRules.decide(data)[1]['Result'][output_variable_name]

 
