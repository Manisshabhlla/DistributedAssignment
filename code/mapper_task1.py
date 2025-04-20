def map(key, value):
    try: 
        fields = value.split("\t")
        timestamp, user_id, action_type, content_id, metadata = fields
        if validate_timestamp(timestamp) and validate_json(metadata): 
            emit(user_id,f"{timestamp}\t{action_type}\t{content_id}\t{metadata}")
        else:
            increment_counter("MalformedRecords")
    except:
        increment_counter("MalformedRecords")