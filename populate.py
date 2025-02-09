from app import create_app, db
from app.models import Question, Choice, Committee

app = create_app()

with app.app_context():
    # Questions and Choices
    questions_and_choices = {
        "Let's build your ideal committee! What is the committee's delegate size?": [
            {"text":"15-20", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":5,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":10,
                "ECC":0,
                "SSCC":10,
                "ACC":5,
                "AD-HOC":10,
                "J-UNSC":10,
                "J-DISEC":0
            }},
            {"text":"25-30", "weights":{
                "COP 30":0,
                "IBC":5,
                "H-NAM":5,
                "ITU":0,
                "UNOOSA":10,
                "NASDAQ":10,
                "HUAC":10,
                "C-300":10,
                "SCOTUS":5,
                "ECC":10,
                "SSCC":2,
                "ACC":10,
                "AD-HOC":2,
                "J-UNSC":2,
                "J-DISEC":0
            }},
            {"text":"35-40", "weights":{
                "COP 30":2,
                "IBC":10,
                "H-NAM":10,
                "ITU":2,
                "UNOOSA":5,
                "NASDAQ":0,
                "HUAC":5,
                "C-300":5,
                "SCOTUS":0,
                "ECC":5,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":10
            }},
            {"text":"45+", "weights":{
                "COP 30":10,
                "IBC":0,
                "H-NAM":2,
                "ITU":10,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":5
            }}
        ],
        "Continuing with your dream committee, what would the rules of procedure (ROP) look like?": [
            {"text":"Standard ROP", "weights":{
                "COP 30":10,
                "IBC":10,
                "H-NAM":10,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":8,
                "J-DISEC":8
            }},
            {"text":"Crisis ROP", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"Cabinet ROP", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"I'm all for new and wacky forms of modified ROP!", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }}
        ],
        "Finally, what do you envision most of committee to look like?": [
            {"text":"Crafting Resolution Papers", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"Passing Documents", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"Writing Directives", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }}
        ],
        "What is your favorite subject out of the following?": [
            {"text":"Science", "weights":{
                "COP 30":10,
                "IBC":8,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":3,
                "SCOTUS":0,
                "ECC":3,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"History", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":5,
                "C-300":0,
                "SCOTUS":0,
                "ECC":10,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"Government", "weights":{
                "COP 30":0,
                "IBC":5,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":10,
                "C-300":0,
                "SCOTUS":10,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"Business/Marketing", "weights":{
                "COP 30":0,
                "IBC":8,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":10,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }}
        ],
        "What is your dream vacation destination": [
            {"text":"Cross-Country USA Roadtrip", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"Europe", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"Asia", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"Africa", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }}
        ],
        "": [
            {"text":"", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }}
        ],
        "": [
            {"text":"", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }}
        ],
        "": [
            {"text":"", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }},
            {"text":"", "weights":{
                "COP 30":0,
                "IBC":0,
                "H-NAM":0,
                "ITU":0,
                "UNOOSA":0,
                "NASDAQ":0,
                "HUAC":0,
                "C-300":0,
                "SCOTUS":0,
                "ECC":0,
                "SSCC":0,
                "ACC":0,
                "AD-HOC":0,
                "J-UNSC":0,
                "J-DISEC":0
            }}
        ]
    }
    questions = {}
    for qtext in questions_and_choices:
        question = Question(text=qtext)
        db.session.add(question)
        db.session.flush() # Ensures the questions gets an ID without committing fully
        questions[qtext] = question.id 

    choices = []
    for qtext, choice_list in questions_and_choices.items():
        question_id = questions[qtext]
        for choice_data in choice_list:
            choice = Choice(
                question_id=question_id,
                text=choice_data["text"],
                weights=choice_data["weights"]
            )
            choices.append(choice)

    db.session.add_all(choices)
    db.session.commit()
    print("Questions and choices added successfully!")

    # c1 = Choice(question_id=q1.id, text="Dark", weights={
    #     "ICAO": 2, 
    #     "ABA": 3, 
    #     "COO": 1,
    #     'DOJ': 0
    #     })
    # c2 = Choice(question_id=q1.id, text="Milk", weights={
    #     "ICAO": 3, 
    #     "ABA": 0, 
    #     "COO": 2,
    #     'DOJ': 1
    #     })
    # c3 = Choice(question_id=q1.id, text="White", weights={
    #     "ICAO": 1, 
    #     "ABA": 2, 
    #     "COO": 0,
    #     'DOJ':3
    #     })
    # c4 = Choice(question_id=q1.id, text="None", weights={
    #     "ICAO": 0, 
    #     "ABA": 1, 
    #     "COO": 3,
    #     'DOJ':2
    #     })

    # c5 = Choice(question_id=q2.id, text="France", weights={
    #     "ICAO": 3, 
    #     "ABA": 0, 
    #     "COO": 2,
    #     'DOJ': 1
    #     })
    # c6 = Choice(question_id=q2.id, text="Japan", weights={
    #     "ICAO": 2, 
    #     "ABA": 1, 
    #     "COO": 0,
    #     'DOJ': 3
    #     })
    # c7 = Choice(question_id=q2.id, text="India", weights={
    #     "ICAO": 0, 
    #     "ABA": 2, 
    #     "COO": 3,
    #     'DOJ':2
    #     })
    # c8 = Choice(question_id=q2.id, text="Mexico", weights={
    #     "ICAO": 1, 
    #     "ABA": 3, 
    #     "COO": 1,
    #     'DOJ':0
    #     })
    # db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8])

    committees = [
        # Principal
        Committee(
            name="COP 30", 
            full_name="United Nations Climate Change Conference", 
            link="https://kingmun.org/committees/cop%2030", 
            image_url="https://files.munnorthwest.org/image/kingmun/964d5708af82b6faeef2cc59e128fef44e1310c30e0c5bff666cbca8ac031841/IMG_5705-min.png", 
            difficulty_level="Introductory", 
            topic_1="Combating Climate-Based Food Insecurity", 
            topic_2="Promoting Access to Alternative Energy Sources"
            ),
        Committee(
            name="IBC", 
            full_name="International Bioethics Committee", 
            link="https://kingmun.org/committees/ibc", 
            image_url="https://files.munnorthwest.org/image/kingmun/5cb056e9c67532351f46b85ba232809453e0f535943c1831efca5aff6656e825/IMG_5726.webp", 
            difficulty_level="Intermediate", 
            topic_1="Addressing Research Ethics in Genome Technology", 
            topic_2="Protecting Healthcare Data Privacy in the Digital Era"
            ),
        Committee(
            name="H-NAM", 
            full_name="Historical Non-Aligned Movement", 
            link="https://kingmun.org/committees/h-nam", 
            image_url="https://files.munnorthwest.org/image/kingmun/17c10a57fdefb491b2062fbc559be289d8e2a1b80a5230cddc5dc6a3d5ad53e1/IMG_5702.jpeg", 
            difficulty_level="Advanced", 
            topic_1="Combating the Threat of Nuclear Armament (1964)", 
            topic_2="Facilitating Peaceful Transitions of Power in the Decolonization Era (1964)"
            ),

        # ECOSOC
        Committee(
            name="ITU", 
            full_name="International Telecommunications Union", 
            link="https://kingmun.org/committees/itu", 
            image_url="https://files.munnorthwest.org/image/kingmun/b5c2fc99ec6d41ae4d4d0d98359d5862f2436e37410db90407b8cca876cbd862/itu%20comm%20.jpeg", 
            difficulty_level="Introductory", 
            topic_1="Addressing the Digital Divide", 
            topic_2="Addressing Misinformation in Emergency Responses"
            ),
        Committee(
            name="UNOOSA", 
            full_name="United Nations for Outer Space Affairs", 
            link="https://kingmun.org/committees/unoosa", 
            image_url="https://files.munnorthwest.org/image/kingmun/430fffd1224d99b870ba881d6da50f28ccad9be42b9a4c39db789d4e791b80a5/unoosa%20comm%20pic.jpeg", 
            difficulty_level="Intermediate", 
            topic_1="Expansion of the Global Satellites System", 
            topic_2="Responsibility to Reduce Space Debris"
            ),
        Committee(
            name="NASDAQ", 
            full_name="National Association of Security Dealers Automated Quotations", 
            link="https://kingmun.org/committees/nasdaq", 
            image_url="https://files.munnorthwest.org/image/kingmun/e98880cd5a5f05326e5dcd874f64d13c0cecc4c4378e3ddfe795a9344fdd4a29/NASDAQ%20Photo%20General.jpg", 
            difficulty_level="Advanced", 
            topic_1="Mitigating Fraudulent Market Activity", 
            topic_2="Navigating a Nasdaq-NYSE Merger"
            ),
        
        # Specialized
        Committee(
            name="HUAC", 
            full_name="House Un-American Activities Committee", 
            link="https://kingmun.org/committees/huac", 
            image_url="https://files.munnorthwest.org/image/kingmun/12867126dc81167bd82c00bf2571a19a863625f07b831494889df6c83cc0d97d/huac%20committee%20photo.jpeg", 
            difficulty_level="Introductory", 
            topic_1="The Hollywood Ten Investigations", 
            topic_2="The Alger Hiss Investigations"
            ),
        Committee(
            name="C-300", 
            full_name="Committee of 300", 
            link="https://kingmun.org/committees/c-300", 
            image_url="https://files.munnorthwest.org/image/kingmun/957db87defe28e062fb9e60ab2b0ba4d3b9831b78eca2501e2df479e29ff9b7b/c-300%20committee%20photo.png", 
            difficulty_level="Intermediate", 
            topic_1="Operation Lambda", 
            topic_2=None
            ),
        Committee(
            name="SCOTUS", 
            full_name="Supreme Court of the United States", 
            link="https://kingmun.org/committees/scotus", 
            image_url="https://files.munnorthwest.org/image/kingmun/9fbd3dcb1936e08a6dfa12456b5ddf36bb83736287497d96917be831374afb59/scotus%20committee%20photo.jpg", 
            difficulty_level="Advanced", 
            topic_1="Nuclear Regulatory Commission v. Texas", 
            topic_2="Republic of Hungary v. Simon"
            ),

        # Crisis
        Committee(
            name="ECC", 
            full_name="Epidemic Crisis Committee", 
            link="https://kingmun.org/committees/ecc", 
            image_url="https://files.munnorthwest.org/image/kingmun/b4a36bc02a81c3c3ed0b8ec5195a88f16d4f9a93ee09efff31ad42fabbe99b82/ecc%20committee%20photo%20(1).jpg", 
            difficulty_level="Introductory", 
            topic_1="1500s Sweating Sickness", 
            topic_2=None
            ),
        Committee(
            name="SSCC", 
            full_name="Secret Society Crisis Committee", 
            link="https://kingmun.org/committees/sscc", 
            image_url="https://files.munnorthwest.org/image/kingmun/6e747c592546ca9fc80e950aba40579c6a530eea4d023f6673e885a2b3d5bbfd/sscc%20committee%20photo.jpg", 
            difficulty_level="Intermediate", 
            topic_1="White Lotus Society", 
            topic_2=None
            ),
        Committee(
            name="ACC", 
            full_name="Apocalyptic Crisis Committee", 
            link="https://kingmun.org/committees/acc", 
            image_url="https://files.munnorthwest.org/image/kingmun/6720854a9dd1479d379d95e28deab4e302eda4438bb291a7f2625ad8671320a8/acc%20committee%20photo%20(1).jpg", 
            difficulty_level="Advanced", 
            topic_1="World Order: After the Impact", 
            topic_2=None
            ),
        
        # Joint
        Committee(
            name="AD-HOC", 
            full_name="AD-HOC", 
            link="https://kingmun.org/committees/ad-hoc", 
            image_url="https://files.munnorthwest.org/image/kingmun/0e1764c52a619ffa2c1a5839cfc459053b3e4c935da8744a659f918849f5aa99/adhoc%20committee%20photo.webp", 
            difficulty_level="Advanced", 
            topic_1="[REDACTED]", 
            topic_2=None
            ),
        Committee(
            name="J-UNSC", 
            full_name="Joint United Nations Security Council", 
            link="https://kingmun.org/committees/j-unsc", 
            image_url="https://files.munnorthwest.org/image/kingmun/54da8501d1d57132dd5f5406e0fb9e476524aa5335cb3b5b6df2fb8d0d32d31c/You%20and%20s.%20See.jpeg", 
            difficulty_level="Advanced", 
            topic_1="Civilian Displacement in the Democratic Republic of the Congo", 
            topic_2="Foreign Involvement in the Yemeni Civil War"
            ),
        Committee(
            name="J-DISEC", 
            full_name="Joint Disarmament and International Security Committee", 
            link="https://kingmun.org/committees/j-disec", 
            image_url="https://files.munnorthwest.org/image/kingmun/9ccf2acf90ec7c8239c41c0b7811cd18b689f015076c93bbe1fed993d57fe66f/j-disec%20commmittee%20photo.jpg", 
            difficulty_level="Advanced", 
            topic_1="Regulating Arms Trading in Democratic Republic of the Congo", 
            topic_2="Foreign Involvement in the Yemeni Civil War"
            )
    ]
    db.session.add_all(committees)

    db.session.commit()
    print("Committees added successfully!")