class AttributeNotFoundException(Exception):
    "Attribute does not exist in attributes dict."
    pass

class AttributePointsOverflowExeption(Exception):
    "Not enough attribute points to spend."
    pass