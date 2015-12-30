from app import app

from sqlalchemy import func
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
TablePrefix = app.config['DATABASE_TABLE_PREFIX']

class Course(Base):
    __tablename__ = '%s%s' % (TablePrefix, 'Course')

    id = Column(Integer, primary_key=True)

    description = Column(String)
    image_url = Column(String)
    label = Column(String(127), nullable=False, unique=True)

    @property
    def serialize(self):
        # Returns object data in a serializable format
        return {
               'id': self.id,
            'label': self.label
        }
