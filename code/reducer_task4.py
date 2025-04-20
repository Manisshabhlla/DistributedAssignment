def reduce(key, values): 
    activity_data = []
    profile_data = None
    for value in values:
        if value.startswith("activity"): 
            activity_data.append(value.split("\t")[^1_1])
        elif value.startswith("profile"): 
            profile_data = value.split("\t") [^1_1]
    if profile_data:
        for activity in activity_data: 
            emit(key, f"{activity}\t{profile_data}")