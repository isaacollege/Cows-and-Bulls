def count_cows(guess, answer):
    """
    Count how many cows the user has scored (numbers in the wrong place)
    """
    return sum(i in guess and guess[n] != i for n, i in enumerate(answer))

    
def count_bulls(guess, answer):
    """
    Count how many bulls the user has scored (numbers in the right place)
    """
    return sum(guess[n] == i for n, i in enumerate(answer))
