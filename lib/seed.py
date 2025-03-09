#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///one_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a game instance
    game = Game(title='Breath of the Wild', genre='Action-adventure', platform='Switch', price=60)
    session.add(game)
    session.commit()

    # Create a review instance
    review = Review(score=10, comment='A classic!', game_id=game.id)
    session.add(review)
    session.commit()
