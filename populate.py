from app import create_app, db
from app.models import Question, Choice, Committee

app = create_app()

with app.app_context():
    # Add sample questions
    q1 = Question(text="Favorite chocolate?")
    q2 = Question(text="Where would your ideal vacation be?")
    db.session.add(q1)
    db.session.add(q2)
    db.session.commit()

    c1 = Choice(question_id=q1.id, text="Dark", weights={
        "ICAO": 2, 
        "ABA": 3, 
        "COO": 1,
        'DOJ': 0
        })
    c2 = Choice(question_id=q1.id, text="Milk", weights={
        "ICAO": 3, 
        "ABA": 0, 
        "COO": 2,
        'DOJ': 1
        })
    c3 = Choice(question_id=q1.id, text="White", weights={
        "ICAO": 1, 
        "ABA": 2, 
        "COO": 0,
        'DOJ':3
        })
    c4 = Choice(question_id=q1.id, text="None", weights={
        "ICAO": 0, 
        "ABA": 1, 
        "COO": 3,
        'DOJ':2
        })

    c5 = Choice(question_id=q2.id, text="France", weights={
        "ICAO": 3, 
        "ABA": 0, 
        "COO": 2,
        'DOJ': 1
        })
    c6 = Choice(question_id=q2.id, text="Japan", weights={
        "ICAO": 2, 
        "ABA": 1, 
        "COO": 0,
        'DOJ': 3
        })
    c7 = Choice(question_id=q2.id, text="India", weights={
        "ICAO": 0, 
        "ABA": 2, 
        "COO": 3,
        'DOJ':2
        })
    c8 = Choice(question_id=q2.id, text="Mexico", weights={
        "ICAO": 1, 
        "ABA": 3, 
        "COO": 1,
        'DOJ':0
        })
    db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8])

    com1 = Committee(name="ICAO",full_name="International Civil Aviation Organization", link="https://kingmun.org/committees/icao", image_url="https://files.munnorthwest.org/image/kingmun/777d7cde00dfa6508eeed26cf78c8c72e59beb8c22df6683f06d9e45b300078a/icao.jpg", 
                   difficulty_level="Introductory", topic_1="Ensuring the Health and Safety of Passengers and Crew Onboard Commercial Flights", topic_2="Safely Integrating Unmanned Aircraft Systems into Airspace")
    com2 = Committee(name="ABA",full_name="American Bar Association", link="https://kingmun.org/committees/aba", image_url="https://files.munnorthwest.org/image/kingmun/680a821e8a6384e4c5f5505eb3a31e24a8e0036f1b7a98e1f205e1fb220e95a5/ABA%20Committee%20Photo.jpg", 
                   difficulty_level="Intermediate", topic_1="Protecting Client Confidentiality in the Digital Age", topic_2="Transparency in Corporate Law")
    com3 = Committee(name="COO",full_name="Council of Olympus", link="https://kingmun.org/committees/coo", image_url="https://files.munnorthwest.org/image/kingmun/ef0b354f09d3606e0c763f4b85cfe5e15495bdd531e2eb8a7f970a9272f67b47/Olympusimg.png", 
                   difficulty_level="Advanced", topic_1="Sovereignty of Attica", topic_2="The Trojan War")
    com4 = Committee(name="DOJ",full_name="Department of Justice", link="https://kingmun.org/committees/doj", image_url="https://files.munnorthwest.org/image/kingmun/a40c5bc881e9d1b39d08ce479fdd0ccc4703bac2206fcf164d9217993a90a09a/dojimg.jpeg", 
                   difficulty_level="Advanced", topic_1="United States v. Norfolk Southern Railway", topic_2="United States v. Attempted Assassination")

    db.session.add_all([com1, com2, com3, com4])

    db.session.commit()
    print("Database populated!")