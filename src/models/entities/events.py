from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer

class Events(Base):
  __tablename__ = "events"

  id = Column(String, primary_key=True)
  title = Column(String, nullable=False)
  details = Column(String)
  slug = Column(String, nullable=False)
  maximum_attendees = Column(Integer)

  def __init__(self, id, title, details, slug, maximum_attendees):
    self.id = id
    self.title = title
    self.details = details
    self.slug = slug
    self.maximum_attendees = maximum_attendees

  def __repr__(self):
    return f"Events [title={self.title}, maximum_attendees={self.maximum_attendees}]"
