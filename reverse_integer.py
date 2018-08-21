# Given a 32-bit signed integer, reverse digits of an integer.


def reverse(x):

    sign = x / abs(x)
    x *= sign

    ret = 0

    while x > 0:
        pop = x % 10
        x = x // 10
        ret *= 10
        ret += pop

    return int(ret * sign)

