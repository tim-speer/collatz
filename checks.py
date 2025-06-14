def check_int(n):
    if not isinstance(n, int):
        raise TypeError('n needs to be an integer')


def check_pos_int(n):
    check_int(n)
    if n <= 0:
        raise ValueError('n needs to be a positive integer')   


def check_pos_odd_int(n):
    check_pos_int(n)
    if n % 2 == 0:
        raise ValueError('n needs to be an odd integer')

