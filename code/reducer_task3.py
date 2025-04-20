def reduce (key, values): 
    total_interactions = sum (values)
    if total_interactions &gt; TRENDING_THRESHOLD: 
        emit(key, total_interactions)