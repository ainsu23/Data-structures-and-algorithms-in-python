# 1. Problem:
# Alice has some cards with numbers written on them. She arranges the cards in
# decreasing order, and lays them out face down in a sequence on a table. She
# challenges Bob to pick out the card containing a given number by turning over
# as few cards as possible. Write a function to help Bob locate the card.

# 2. Come up with some inputs and outputs. Try to cover edge cases.
# Se crea una lista para insertar los posibles tests
tests = []
# query is the first element

tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})
# cards does not contain query
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})
# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})
# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

### Linear Search Algorithm:  it involves searching through a list in a linear
# fashion i.e. element after element.

# Mientras la posición de la lista no sea igual al largo de cartas, compara si
# el valor de la carta en la posición es igual al valor de la carta esperada,
# si es cierto devuelve la posición, si no incrementa y repite, si lo anterior,
# no ocurre devuelve -1
def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

# Se recorre tests y compara, si es igual incrementa variable paso
paso = 0
for num_test in tests:
    if (locate_card(**num_test["input"]) == num_test["output"]):
        paso += 1

# Imprime número de tests exitosos.
print("número de tests exitosos: {} de un total de {}".format(paso, len(tests)))



### Binary search: In fact, if we pick the middle card, we can reduce the number
# of additional cards to be tested to half the size of the list. Then, we can
# simply repeat the process with each half. This technique is called binary search.
# Here's a visual explanation of the technique:
# Here's how binary search can be applied to our problem:

# 1. Find the middle element of the list.
# 2. If it matches queried number, return the middle position as the answer.
# 3. If it is less than the queried number, then search the first half of the list
# 4. If it is greater than the queried number, then search the second half of the list
# 5. If no more elements remain, return -1.

def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

# Se recorre tests y compara, si es igual incrementa variable paso
paso = 0
for num_test in tests:
    if (locate_card(**num_test["input"]) == num_test["output"]):
        paso += 1

# Imprime número de tests exitosos.
print("número de tests exitosos: {} de un total de {}".format(paso, len(tests)))
