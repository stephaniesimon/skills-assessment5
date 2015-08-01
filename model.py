"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):

    __tablename__ = "models"
    
    model_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    model_year = db.Column(db.Integer, nullable=True)
    model_brand_name = db.Column(db.String(64), nullable=True)
    model_name = db.Column(db.String(64), nullable=True)
   

    def __repr__(self):
        """Provides helpful representation when printing."""
        return "<Model model_id=%s model_name=%s>" % (self.model_id, self.model_name)


class Brand(db.Model):

    __tablename__ = "brands"
    brand_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    brand_name = db.Column(db.Integer, db.ForeignKey('models.model_brand_name'))
    brand_founded = db.Column(db.String(64))
    brand_headquarters = db.Column(db.String(64))
    brand_discontinued = db.Column(db.Integer)
   

    model = db.relationship("Model", backref=db.backref("brands", order_by=brand_id))
   

    def __repr__(self):
        """Provides helpful representation when printing."""
        return "<Brand model_id=%s brand_name=%s>" % (self.brand_id, self.brand_name)


# End Part 1
##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
