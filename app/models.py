from . import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    choices = db.relationship('Choice', backref='question',lazy=True)

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    weights = db.Column(db.JSON, nullable=False)

class Committee(db.Model):
    # __tablename__ = 'committees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(200), nullable=True)
    image_url = db.Column(db.String(200), nullable=True)
    difficulty_level = db.Column(db.String(50), nullable=True)
    topic_1 = db.Column(db.Text, nullable=True) 
    topic_2 = db.Column(db.Text, nullable=True)

class Submission(db.Model):
    __tablename__ = 'submissions'
    id = db.Column(db.Integer, primary_key=True)
    user_identifier = db.Column(db.String(200), nullable=True)  #Session ID
    choices = db.Column(db.JSON, nullable=False)
    results = db.Column(db.JSON, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())