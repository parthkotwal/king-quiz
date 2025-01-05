from flask import Blueprint, jsonify, request, render_template
from app import db
from app.models import Question, Choice, Committee, Submission

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/quiz', methods=['GET'])
def quiz():
    return render_template('quiz.html')

@routes.route('/results', methods=['GET'])
def results():
    return render_template('results.html')


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

    return jsonify({'questions':responses})

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
    choice_ids = data.get('choice_ids', [])
    user_identifier = data.get('user_identifier', "Anonymous")

    if not choice_ids or not isinstance(choice_ids, list):
        return {"error": "Invalid input. 'choice_ids' must be a list."}, 400

    choices = Choice.query.filter(Choice.id.in_(choice_ids)).all()
    weights = {}
    for choice in choices:
        for committee, weight in choice.weights.items():
            weights[committee] = weights.get(committee, 0) + weight

    sorted_weights = sorted(weights.items(), reverse=True, key=lambda x: x[1])
    total = sum(weights.values())
    top3_committees = [
        {
            "committee": committee,
            "weight": weight,
            "percentage": round((weight / total) * 100, 2) if total > 0 else 0,
        }
        for committee, weight in sorted_weights[:3]
    ]
    committee_names = [c["committee"] for c in top3_committees]
    committees = Committee.query.filter(Committee.name.in_(committee_names)).all()

    infos = {}
    for comm in committees:
        infos[comm.name] = {
            "weight": next((c["weight"] for c in top3_committees if c["committee"] == comm.name), 0),
            "percentage": next((c["percentage"] for c in top3_committees if c["committee"] == comm.name), 0),
            "link": comm.link,
            "image_url": comm.image_url,
            "difficulty_level": comm.difficulty_level,
            "topics": [comm.topic_1, comm.topic_2],
            "full_name": comm.full_name
        }
    
    submission = Submission(
        user_identifier=user_identifier,
        choices=choice_ids,
        results=infos,
    )
    db.session.add(submission)
    db.session.commit()

    return {"success": True, "committee_info": infos, "submission_id": submission.id}, 200


@routes.route('/api/results', methods=['GET'])
def get_results():
    submission_id = request.args.get('submission_id')
    
    # Fetch the submission
    submission = Submission.query.get(submission_id)
    if not submission:
        return jsonify({'error': 'Submission not found'}), 404

    # Use the precomputed results from the submission
    results = submission.results

    sorted_results = sorted(
        results.items(), 
        key=lambda item: item[1]['weight'], 
        reverse=True
    )

    # Format the response
    response = []
    for committee_name, details in sorted_results[:3]:  # Top 3 only
        committee_obj = Committee.query.filter_by(name=committee_name).first()
        if committee_obj:
            response.append({
                'committee_name': committee_obj.name,
                'percentage': details['percentage'],
                'difficulty': committee_obj.difficulty_level,
                'topics': [committee_obj.topic_1, committee_obj.topic_2],
                'link': committee_obj.link,
                'image_url': committee_obj.image_url, 
                'full_name': committee_obj.full_name
            })

    return jsonify({'results': response})
