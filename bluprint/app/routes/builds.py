from flask import Blueprint, request, jsonify
from app.database import db
from app.models import Build
from app.services.compatibility_service import check_build_compatibility

bp = Blueprint('builds', __name__)

@bp.route('', methods=['GET'])
def get_builds():
    builds = Build.query.all()
    return jsonify([b.to_dict() for b in builds])

@bp.route('/<int:build_id>', methods=['GET'])
def get_build(build_id):
    build = Build.query.get_or_404(build_id)
    return jsonify(build.to_dict())

@bp.route('', methods=['POST'])
def create_build():
    data = request.get_json()
    part_ids = data.get('parts', [])
    
    # Check compatibility
    compat = check_build_compatibility(part_ids)
    
    build = Build(
        name=data['name'],
        description=data.get('description'),
        parts=part_ids,
        total_price=0,  # TODO: Calculate from parts
        is_compatible=compat['is_compatible'],
        compatibility_issues=compat.get('issues', [])
    )
    db.session.add(build)
    db.session.commit()
    return jsonify(build.to_dict()), 201

@bp.route('/<int:build_id>', methods=['PUT'])
def update_build(build_id):
    build = Build.query.get_or_404(build_id)
    data = request.get_json()
    # TODO: Update fields
    db.session.commit()
    return jsonify(build.to_dict())

@bp.route('/<int:build_id>', methods=['DELETE'])
def delete_build(build_id):
    build = Build.query.get_or_404(build_id)
    db.session.delete(build)
    db.session.commit()
    return jsonify({'message': 'deleted'}), 200