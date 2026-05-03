import sys
import logging
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)
Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)

try:
    engine = create_engine('sqlite:///todolist.db', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    logger.info("Database setup completed successfully.")

except SQLAlchemyError as e:
    logger.error(f"Error creating engine: {e}")
    sys.exit(1)
