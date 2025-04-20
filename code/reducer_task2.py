def reduce ( key, values): 
    user_id, action_type = key.split("_")
    total_count = sum(values) 
    emit(user_id,f"{action_type}\t{total_count}")