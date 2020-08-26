from app import db




class Output(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  coordinates = db.Column(db.String(2))
  def __repr__(self):
    return ' '.join('Coordinates:', self.coordinates)
