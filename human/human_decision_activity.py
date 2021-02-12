@activity
def human_decision(message, choices):
    """Human decision

    Allows a human to select options from a list

    :parameter message: Message the user gets prompted
    :type message: string

    :parameter choices: Options from the user can select
    :type choices: list of strings

    :return: Decision result
    :rtype: any

    Keywords
        decision, human decision, prompt, multiselect

    Icon
        la la-user
    """
    from easygui import multchoicebox

    title = "Human decision required"

    return multchoicebox(message, title, choices)
