from app import create_app, db
from app.models import Question, Choice, Committee

app = create_app()

with app.app_context():
    # Add sample questions
    q1 = Question(text="333JFSIJ")
    q2 = Question(text="Do you prefer crisis management or long-term planning?")
    db.session.add(q1)
    db.session.add(q2)
    db.session.commit()

    # Add sample choices for question 1
    c1 = Choice(question_id=q1.id, text="Global health", weights={"WHO": 2, "UNEP": 0, "ECOSOC": 0})
    c2 = Choice(question_id=q1.id, text="Economic policy", weights={"WHO": 0, "UNEP": 0, "ECOSOC": 2})
    c3 = Choice(question_id=q1.id, text="Environmental issues", weights={"WHO": 0, "UNEP": 2, "ECOSOC": 0})
    db.session.add_all([c1, c2, c3])

    # Add sample choices for question 2
    c4 = Choice(question_id=q2.id, text="Crisis management", weights={"UNSC": 2, "WHO": 1, "UNEP": 0})
    db.session.add_all([c4])

    com = Committee(name="UNSC", link="https://un.org/securitycouncil", image_url="https://example.com/unsc_logo.png", 
                   difficulty_level="Hard", topic_1="International security, conflict resolution", topic_2="kooko")
    db.session.add(com)

    db.session.commit()
    print("Database populated!")