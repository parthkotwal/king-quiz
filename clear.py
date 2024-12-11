from app import create_app, db
from app.models import Question, Choice, Committee

def clear_db():
    with create_app().app_context():
        db.session.query(Question).delete()
        db.session.query(Choice).delete()
        db.session.query(Committee).delete()
        db.session.commit()
        print("All data cleared from the database!")

clear_db()