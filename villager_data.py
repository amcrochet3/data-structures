"""Functions to parse a file containing villager data."""

def read_file(filename):
    with open(filename, "r") as file:
        return [line.rstrip().split("|") for line in file]


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    return set(line[1] for line in read_file(filename))


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    return sorted(line[0] for line in read_file(filename) if line[1] == search_string or search_string == "All")


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    hobbies = {"Education": [], "Fitness": [], "Fashion": [], "Nature": [], "Play": [], "Music": []}

    for line in read_file(filename):
        name, hobby = line[0], line[3]
        if hobby in hobbies:
            hobbies[hobby].append(name)

    return [hobbies[hobby] for hobby in hobbies]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    return [tuple(line) for line in read_file(filename)]


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    for line in read_file(filename):
        name, motto = line[0], line[4]
        if name == villager_name:
            return motto
        
    return None


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    data = read_file(filename)
    target_personality = None

    for line in data:
        name = line[0]
        if name == villager_name:
            target_personality = line[2]
            break

    if target_personality:
        return set(line[0] for line in data if line[2] == target_personality and villager_name != line[0])
    
    return set()
