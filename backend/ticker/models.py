from ticker.database import Base
from sqlalchemy import Column, Integer, String, Double, DateTime
from datetime import datetime

class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    close = Column(Double)
    high = Column(Double)
    low = Column(Double)
    open = Column(Double)
    volume = Column(Integer)
    instrument = Column(String)