def wave(people):
    result = []
    for i in range(len(people)):
        if people[i] != " ":
            result.append(people[:i] + people[i].upper()+ people[i + 1:])
    return result