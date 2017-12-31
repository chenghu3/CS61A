def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    "*** YOUR CODE HERE ***"
    number = 0
    def take():
        nonlocal number
        if number == len(snacks):
            number = 0
        snack = snacks[number]
        number += 1
        return snack
    return take

    # offical answer:
    # index = 0
    # def vender():
    #     nonlocal index
    #     result = snacks[index]
    #     index = (index + 1) % len(snacks)
    #     return result
    # return vender
