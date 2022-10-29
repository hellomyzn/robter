import logging

import settings



logging.basicConfig(filename=settings.LOG_FILE, level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info("running server")
    from app.models.user import User
    from app.models.db import database
    from app.models.restaurant import Restaurant
    Session = database.connect_db()
    session = Session()
    u = User()
    u.name = "test"
 
    r = Restaurant()
    r.name = "test"
    session.add(r)


    session.add(u)
    session.commit()
    session.close()