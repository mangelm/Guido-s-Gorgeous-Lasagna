"""Guido's Gorgeous Lasagna"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """
    Return bake time remaining.

    This function takes the expected bake time to cooking the lasagna and substract the elapsed bake time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Return preparation time in minutes.

    This function takes the number of layers of the lasagna and multiplies it by the extra time we need to cook the lasagna.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return elapsed_bake_time + (number_of_layers * PREPARATION_TIME)
    