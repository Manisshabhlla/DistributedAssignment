def map (key, value): 
    fields = value.split("\t") 
    content_id = fields[^1_3] 
    action_type = fields[^1_2]
    if action_type in [ "like","share"]: 
        emit(content_id,1)