from fractions import Fraction
from decimal import Decimal, ROUND_HALF_UP
from settings import signs
import random

def novice_gen(hard):
    example = [random.randrange(1, (10 * hard)), random.randrange(1, (10 * hard))]
    sign = random.choice(signs)
    if sign != '/':
        my_message = str(example[0]) + ' ' + str(sign) + ' ' + str(example[1])
        answer = eval(str(example[0]) + str(sign) + str(example[1]))
    else:
        my_message = str(example[0]) + ' ' + str(sign) + ' ' + str(example[1])
        answer = str(eval(str(example[0]) + '//' + str(example[1]))) +'(' +str(example[0] % example[1]) + ')'
    return [my_message, answer]
def lover_gen(hard):
    example = [random.randrange(1, (10 * hard)), random.randrange(1, (10 * hard)), random.randrange(1, (10 * hard)), random.randrange(1, (10 * hard))]
    sign = random.choice(signs)
    example3 = [str(example[0]) + '/' + str(example[1]), str(example[2]) + '/' + str(example[3])]
    if sign == '+':
        my_message = str(example3[0]) + ' + ' + str(example3[1])
        answer = Fraction(Fraction(example[0], example[1]) + Fraction(example[2], example[3]))
    elif sign == '-':
        my_message = str(example3[0]) + ' - ' + str(example3[1])
        answer = Fraction(Fraction(example[0], example[1]) - Fraction(example[2], example[3]))
    elif sign == '*':
        my_message = str(example3[0]) + ' * ' + str(example3[1])
        answer = Fraction(Fraction(example[0], example[1]) * Fraction(example[2], example[3]))
    elif sign == '/':
        my_message = str(example3[0]) + ' / ' + str(example3[1])
        answer = Fraction(Fraction(example[0], example[1]) / Fraction(example[2], example[3]))
    return [my_message, answer]
def master_gen(hard):
    example = [random.randrange(1, (10 * hard)), random.randrange(1, (10 * hard)), random.randrange(1, (10 * hard)), random.randrange(1, (10 * hard))]
    example3 = [Decimal(str(example[0]) + '.' + str(example[1])), Decimal(str(example[2]) + '.' + str(example[3]))]
    sign = random.choice(signs)
    if sign != '/':
        my_message = str(example3[0]) + ' ' + str(sign) + ' ' + str(example3[1])
        answer = Decimal(eval(str(example3[0]) + str(sign) + str(example3[1])))
        answer = answer.quantize(Decimal("1.0"), ROUND_HALF_UP)
    else:
        my_message = str(example3[0]) + ' ' + str(sign) + ' ' + str(example3[1])
        answer = Decimal(eval(str(example3[0]) + '/' + str(example3[1])))
        answer = answer.quantize(Decimal("1.0"), ROUND_HALF_UP)
    return [my_message, answer]
