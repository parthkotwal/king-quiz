from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import create_app

app = create_app()

@app.route('/api/health',methods=['GET'])
def health_check():
    return {"status":"ok"}, 200

if __name__ == "__main__":
    app.run(debug=True)