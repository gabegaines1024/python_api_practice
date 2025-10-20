def validate_part_data(data):
    """Validate part data before creating/updating"""
    if not data.get('name'):
        return False, 'Name is required'
    
    if not data.get('part_type'):
        return False, 'Part type is required'
    
    # TODO: Add more validation rules
    
    return True, None

def validate_build_data(data):
    """Validate build data before creating/updating"""
    if not data.get('name'):
        return False, 'Build name is required'
    
    return True, None