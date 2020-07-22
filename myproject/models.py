from myproject import db

class State(db.Model):

    __tablename__ ='states'

    id = db.Column(db.Integer,primary_key=True)

    name = db.Column(db.Text)

    #one -to - one with party
    party = db.relationship("Party",backref='states',uselist=False)

    #one-to many relationship with politicians
    politician = db.relationship("Politician",backref='states',lazy='dynamic')

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        if self.party:
            return f" State : {self.name} is won by : {self.party.name}"
        return f"State : {self.name} is not called yet!!"

class Politician(db.Model):

    __tablename__ = 'politicians'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    state= db.Column(db.Text)

    state_id = db.Column(db.Integer,db.ForeignKey('states.id'))

    def __init__(self,name,state,state_id):
        self.name=name
        self.state=state
        self.state_id=state_id

    def __repr__(self):
        return f"Politician : {self.name} from the state of {self.state}"

class Party(db.Model):

    __tablename__='parties'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)

    state_id = db.Column(db.Integer,db.ForeignKey('states.id'))

    def __init__(self,name,state_id):
        self.name=name
        self.state_id=state_id

    def __repr__(self):
        return f"Party : {self.name}"
