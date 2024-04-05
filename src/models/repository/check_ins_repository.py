from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class CheckInsRepository:
  def insert_check_in(self, attendde_id) -> str:
    with db_connection_handler as database:
      try:
          check_in = (
              CheckIns(
                  CheckIns(attendeeId == attendde_id)
              )
          )
          database.session.add(check_in)
          database.session.commit()
          return attendde_id
      except IntegrityError:
        raise Exception("Participant already checked in!")
      except Exception as exception:
        database.session.rollback()
        raise exception