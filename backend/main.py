import logging

import settings



logging.basicConfig(filename=settings.LOG_FILE, level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info("running server")
    from app.models.user import User
    from app.models.db import database
    from app.models.restaurant import Restaurant
    from app.models.rate import Rate

    Session = database.connect_db()
    session = Session()

    u = User()
    u.name = "test"
    session.add(u)

    r = Restaurant()
    r.name = "test"
    session.add(r)

    session.commit()

    rate = Rate()
    rate.user_id = 1
    rate.restaurant_id = 1
    rate.value = 5
    session.add(rate)
    
    session.commit()
    session.close()