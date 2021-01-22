from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from homework12.models import Base

engine = create_engine("sqlite:///db.sqlite")
Session = sessionmaker(bind=engine)

Base.prepare(engine, reflect=True)
