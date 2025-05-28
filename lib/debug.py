#!/usr/bin/env python3

from sqlalchemy import create_engine
from models import Base, Company, Dev

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)
    print("Tables created.")