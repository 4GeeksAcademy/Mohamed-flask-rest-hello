from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[int] = mapped_column(String(100), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    # One-to-many relationships
    Posts = db.relationship('Post', backref='user')
    Likes = db.relationship('Like', backref='user')
    Comments = db.relationship('Comment', backref='user')
    Stories = db.relationship('Story', backref='user')


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(200), nullable= False)
    image_url: Mapped[str] = mapped_column(String(20), nullable=False)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'), nullable=False)
    

class Like(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.Foreignkey('user.id'),nullable=False)
    post_id: Mapped[int] = mapped_column(db.Foreignkey('post_id'),nullable=False)

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key= True)
    text: Mapped[str] = mapped_column(String(200), nullable=False)
    user_id: Mapped[int] = mapped_column(db.Foreignkey('user.id'),nullable=False)
    post_id: Mapped[int] = mapped_column(db.Foreignkey('post_id'),nullable=False)

class Story(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.foreignkey('user_id',nullabld= False))

    











    


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    

