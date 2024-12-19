from app import create_app, db
from app.models import Question, Choice, Committee

app = create_app()

with app.app_context():
    # Add sample questions
    q1 = Question(text="Cats or dogs?")
    q2 = Question(text="Favorite ice cream flavor?")
    db.session.add(q1)
    db.session.add(q2)
    db.session.commit()

    c1 = Choice(question_id=q1.id, text="Cat", weights={"UNSC": 2, "APEC": 0, "GA": 0})
    c2 = Choice(question_id=q1.id, text="Dogs", weights={"UNSC": 0, "APEC": 1, "GA": 2})
    c3 = Choice(question_id=q1.id, text="None", weights={"UNSC": 0, "APEC": 2, "GA": 0})

    c4 = Choice(question_id=q2.id, text="Chocolate", weights={"UNSC": 2, "APEC": 1, "GA": 0})
    c5 = Choice(question_id=q2.id, text="Vanilla", weights={"UNSC": 2, "APEC": 1, "GA": 0})
    c6 = Choice(question_id=q2.id, text="Coffee", weights={"UNSC": 2, "APEC": 1, "GA": 0})
    c7 = Choice(question_id=q2.id, text="Coffee", weights={"UNSC": 2, "APEC": 1, "GA": 0})
    db.session.add_all([c1, c2, c3, c4, c5, c6, c7])

    com = Committee(name="UNSC", link="", image_url="", 
                   difficulty_level="Introductory", topic_1="Terrorism", topic_2="Corruption")
    com2 = Committee(name="APEC", link="", image_url="", 
                   difficulty_level="Intermediate", topic_1="Climate", topic_2="Hunger")
    com3 = Committee(name="GA", link="", image_url="", 
                   difficulty_level="Advanced", topic_1="Education", topic_2="Recession")
    db.session.add_all([com, com2, com3])

    db.session.commit()
    print("Database populated!")