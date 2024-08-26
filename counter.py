calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    return string.casefold() in list_to_search


print(string_info('Cat'))
print(string_info('cataclysm'))
print(is_contains('Cat', ['caT', 'cat', 'CAt']))
print(is_contains('Cat', ['colour', 'Cataclysm', 'dog']))
print(calls)
