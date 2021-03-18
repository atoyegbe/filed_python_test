from app import db 
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import DateTime
from datetime import datetime 
from sqlalchemy.types import ARRAY, String




class Audio(db.Model):
    __abstract__ = True 
    title = db.Column(db.String())
    duration = db.Column(db.Integer, nullable=False)

    def __init__(self, title, duration) -> None:
        self.title = title 
        self.duration = duration 


class Song(Audio):
    __tablename__ = 'songs'
    

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    upload_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)


    def __init__(self, title, duration) -> None:
        super().__init__(title, duration)
        
        self.title = title
        self.duration = duration
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()



class Podcast(Audio):
    __tablenames__ = 'podcasts'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    host = db.Column(db.String(100), nullable=False)
    participants = db.Column(ARRAY(String(100)), nullable=True)
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)


    def __init__(self, title, duration, host, participants):
        super().__init__(title, duration)

        self.title = title 
        self.duration = duration
        self.host = host 
        self.participants = participants

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Audiobook(Audio):
    __tablenames__ = 'audiobooks'

    id = db.Column(db.Integer, unique=True, primary_key=True)
    author = db.Column(db.String(100))
    narrator = db.Column(db.String(100))
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)


    def __init__(self, title, duration, author, narrator):
        super().__init__(title, duration)

        self.title = title
        self.duration = duration
        self.author = author
        self.narrator = narrator
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()




