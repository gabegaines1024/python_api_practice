from app.models import Part, CompatibilityRule
from app.database import db

def check_build_compatibility(part_ids):
    """Check if a list of parts are compatible"""
    if not part_ids:
        return {'is_compatible': True, 'issues': []}
    
    parts = Part.query.filter(Part.id.in_(part_ids)).all()
    issues = []
    
    # TODO: Implement actual compatibility checking logic
    # For now, return compatible
    
    return {
        'is_compatible': len(issues) == 0,
        'issues': issues
    }

def check_part_compatibility(part1, part2):
    """Check if two specific parts are compatible"""
    # TODO: Implement pair checking logic
    return {'is_compatible': True, 'reason': None}