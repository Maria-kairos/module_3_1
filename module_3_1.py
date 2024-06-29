calls = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info(a):
    string = a
    a = len(string)
    b = string.upper()
    c = string.lower()
    d = (a, b, c)
    return (d)
    count_calls()
def is_contains(a, b):
    a = a.lower()
    d = [s.lower() for s in b]
    if d.count(a):
        return (True)
    else:
        return (False)
    count_calls()


print(string_info('Capybara'))
print(string_info('Armagedon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)