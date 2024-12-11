from flask import Blueprint, jsonify, request
from app import db
from app.models import Question, Choice, Committee

routes = Blueprint('routes', __name__)

@routes.route('/api/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    responses = []
    for question in questions:
        choices = Choice.query.filter_by(question_id=question.id).all()
        responses.append({
            'id': question.id,
            'text': question.text,
            'choices': [{'id':choice.id, 'text':choice.text} for choice in choices]
        })

    return jsonify(responses)

@routes.route('/api/question/<int:question_id>', methods=['DELETE'])
def delete_question(question_id:int):
    try:
        question = Question.query.get(question_id)
        if not question:
            return jsonify({"error": "Question not found"}), 404
        
        Choice.query.filter_by(question_id=question_id).delete()

        # Delete the question
        db.session.delete(question)
        db.session.commit()

        return jsonify({"message": f"Question {question_id} and its choices deleted!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
@routes.route('/api/submit', methods=['POST'])
def submit_responses():
    data = request.json
    choice_ids = data.get('choice_ids',[])
    if not choice_ids or not isinstance(choice_ids, list):
        return {"error": "Invalid input. 'choice_ids' must be a list."},400
    
    choices = Choice.query.filter(Choice.id.in_(choice_ids)).all()
    weights = {}
    for choice in choices:
        for committee, weight in choice.weights.items():
            weights[committee] = weight+weights.get(committee,0)
    sorted_weights = sorted(weights.items(),reverse=True, key=lambda x: x[1])
    total = sum(weights.values())
    top3 = [{ 
        "committee": committee, "weight": weight, 
        "percentage": round((weight / total) * 100, 2) if total > 0 else 0 
        } for committee, weight in sorted_weights[:3]]

    infos = {}
    for comm in top3:
        name = comm["committee"]
        weight = comm["weight"]
        percentage = comm["percentage"]

        details = Committee.query.filter_by(name).first()
        if details:
            infos[name] = {
                "weight": weight,
                "percentage": percentage,
                "link": details.link,
                "image_url": details.image_url,
                "difficulty_level": details.difficulty_level,
                "topic_1": details.topic1,
                "topic_2": details.topic2
            }

    return {"committee_info": infos}, 200