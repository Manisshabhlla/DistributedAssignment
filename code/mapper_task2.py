def map (key, value): 
    fields = value.split("\t") 
    user_id, action_type = fields [^1_1], fields[^1_2] 
    emit(f"{user_id}_{action_type}",1)