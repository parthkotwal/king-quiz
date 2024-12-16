import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from app import create_app, db
from app.models import Question, Choice, Committee

def menu():
    print("\n--- Menu ---")
    print("1. Add Question")
    print("2. Add Choice")
    print("3. Add Committee")
    print("4. View Questions")
    print("5. View Choices")
    print("6. View Committees")
    print("7. Remove Question")
    print("8. Remove Choice")
    print("9. Remove Committee")
    print("10. Clear Database")
    print("11. Exit")

def add_question(session):
    text = input("Enter question text: ")
    new_question = Question(text=text)
    session.add(new_question)
    session.commit()
    print("Question added successfully!")

def add_choice(session):
    question_id = int(input("Enter the question ID to associate with this choice: "))
    question = session.get(Question, question_id)
    if not question:
        print("Question not found!")
        return

    text = input("Enter choice text: ")
    weights = input("Enter weights as JSON (e.g., {'WHO': 2, 'UNEP': 1}): ")
    try:
        weights_dict = eval(weights)
        new_choice = Choice(question_id=question.id, text=text, weights=weights_dict)
        session.add(new_choice)
        session.commit()
        print("Choice added successfully!")
    except Exception as e:
        print(f"Invalid weights format: {e}")

def add_committee(session):
    name = input("Enter committee name: ")
    link = input("Enter committee link (optional): ")
    image_url = input("Enter image URL (optional): ")
    difficulty_level = input("Enter difficulty level (optional): ")
    topic_1 = input("Enter topic 1 (optional): ")
    topic_2 = input("Enter topic 2 (optional): ")

    new_committee = Committee(
        name=name, link=link, image_url=image_url,
        difficulty_level=difficulty_level, topic_1=topic_1, topic_2=topic_2
    )
    session.add(new_committee)
    session.commit()
    print("Committee added successfully!")

def view_questions(session):
    questions = session.execute(select(Question)).scalars().all()
    for question in questions:
        print(f"ID: {question.id}, Text: {question.text}")

def view_choices(session):
    choices = session.execute(select(Choice)).scalars().all()
    for choice in choices:
        print(f"ID: {choice.id}, Text: {choice.text}, Question ID: {choice.question_id}, Weights: {choice.weights}")

def view_committees(session):
    committees = session.execute(select(Committee)).scalars().all()
    for committee in committees:
        print(f"ID: {committee.id}, Name: {committee.name}, Link: {committee.link}, Difficulty: {committee.difficulty_level}")

def remove_question(session):
    question_id = int(input("Enter question ID to remove: "))
    question = session.get(Question, question_id)
    if question:
        session.delete(question)
        session.commit()
        print("Question removed successfully!")
    else:
        print("Question not found!")

def remove_choice(session):
    choice_id = int(input("Enter choice ID to remove: "))
    choice = session.get(Choice, choice_id)
    if choice:
        session.delete(choice)
        session.commit()
        print("Choice removed successfully!")
    else:
        print("Choice not found!")

def remove_committee(session):
    committee_id = int(input("Enter committee ID to remove: "))
    committee = session.get(Committee, committee_id)
    if committee:
        session.delete(committee)
        session.commit()
        print("Committee removed successfully!")
    else:
        print("Committee not found!")

def clear_database(session):
    confirmation = input("Are you sure you want to clear the database? (yes/no): ")
    if confirmation.lower() == "yes":
        db.drop_all()
        db.create_all()
        print("Database cleared and schema recreated!")
    else:
        print("Operation canceled.")

def main():
    app = create_app()
    Session = sessionmaker(bind=db.engine)
    with app.app_context():
        session = Session()
        try:
            while True:
                menu()
                choice = input("Enter your choice: ")
                if choice == "1":
                    add_question(session)
                elif choice == "2":
                    add_choice(session)
                elif choice == "3":
                    add_committee(session)
                elif choice == "4":
                    view_questions(session)
                elif choice == "5":
                    view_choices(session)
                elif choice == "6":
                    view_committees(session)
                elif choice == "7":
                    remove_question(session)
                elif choice == "8":
                    remove_choice(session)
                elif choice == "9":
                    remove_committee(session)
                elif choice == "10":
                    clear_database(session)
                elif choice == "11":
                    print("Exiting program.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        finally:
            session.close()

if __name__ == "__main__":
    main()