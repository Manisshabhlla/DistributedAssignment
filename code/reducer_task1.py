def reduce(key, values):
    for value in values: 
        emit(key, value)