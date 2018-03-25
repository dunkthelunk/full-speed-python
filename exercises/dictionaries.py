ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Gabriel": 10,
    "Maria": 12,
}

def averageOfValues(dicti):
    vals = dicti.values()
    return sum(vals)/len(vals)

def maxVal(dicti):
    return max(dicti, key=dicti.get)

def add_n_to_values(dicti, n):
    return dict([(x,y+n) for x in dicti.keys() for y in dicti.values() if dicti[x] == y])

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

def mean_age(dicti):
    ageList = [dicti[x]["age"] for x in dicti.keys()]
    return sum(ageList)/len(ageList)

def students_with_given_address(dicti, address):
    return [x for x in dicti.keys() if dicti[x]["address"] == address]
