from flask import Blueprint, request, jsonify
from app.database import db
from app.models import Part

bp = Blueprint('parts', __name__)

@bp.route('', methods=['GET'])
def get_parts():
    # TODO: Add filtering logic
    parts = Part.query.all()
    return jsonify([p.to_dict() for p in parts])

@bp.route('/<int:part_id>', methods=['GET'])
def get_part(part_id):
    part = Part.query.get_or_404(part_id)
    return jsonify(part.to_dict())

@bp.route('', methods=['POST'])
def create_part():
    data = request.get_json()
    # TODO: Add validation
    part = Part(
        name=data['name'],
        part_type=data['part_type'],
        manufacturer=data.get('manufacturer'),
        price=data.get('price'),
        specifications=data.get('specifications', {})
    )
    db.session.add(part)
    db.session.commit()
    return jsonify(part.to_dict()), 201

@bp.route('/<int:part_id>', methods=['PUT'])
def update_part(part_id):
    part = Part.query.get_or_404(part_id)
    data = request.get_json()
    # TODO: Update fields from data
    db.session.commit()
    return jsonify(part.to_dict())

@bp.route('/<int:part_id>', methods=['DELETE'])
def delete_part(part_id):
    part = Part.query.get_or_404(part_id)
    db.session.delete(part)
    db.session.commit()
    return jsonify({'message': 'deleted'}), 200