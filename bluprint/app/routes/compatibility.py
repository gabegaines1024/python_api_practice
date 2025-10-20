from flask import Blueprint, request, jsonify
from app.database import db
from app.models import CompatibilityRule
from app.services.compatibility_service import check_build_compatibility

bp = Blueprint('compatibility', __name__)

@bp.route('/check', methods=['POST'])
def check_compatibility():
    data = request.get_json()
    part_ids = data.get('part_ids', [])
    result = check_build_compatibility(part_ids)
    return jsonify(result)

@bp.route('/rules', methods=['GET'])
def get_rules():
    rules = CompatibilityRule.query.filter_by(is_active=True).all()
    return jsonify([r.to_dict() for r in rules])

@bp.route('/rules', methods=['POST'])
def create_rule():
    data = request.get_json()
    rule = CompatibilityRule(
        part_type_1=data['part_type_1'],
        part_type_2=data['part_type_2'],
        rule_type=data['rule_type'],
        rule_data=data['rule_data']
    )
    db.session.add(rule)
    db.session.commit()
    return jsonify(rule.to_dict()), 201