from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete
from datetime import date
from S2_data import Hold, Bane, Booking, Base

from sqlalchemy.engine import Engine
from sqlalchemy import event


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


Database = 'sqlite:///S2.db'  # first part: database type, second part: file path


def create_test_data():  # Used to test database functions before gui is ready.
    with Session(engine) as session:
        new_items = []
        new_items.append(Hold(erfaring=1, størrelse=12))
        new_items.append(Hold(erfaring=0, størrelse=10))
        new_items.append(Hold(erfaring=2, størrelse=7))
        new_items.append(Bane(kapacitet=20, sværhedsgrad=0))
        new_items.append(Bane(kapacitet=10, sværhedsgrad=2))
        new_items.append(Bane(kapacitet=18, sværhedsgrad=1))
        a_date = date(day=10, month=12, year=2022)
        new_items.append(Booking(date=a_date, hold_id=2, bane_id=1))
        session.add_all(new_items)
        session.commit()


def select_all(classparam):
    # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))  # very useful for converting into our data class
        result = []
        for record in records:
            # print(record)
            result.append(record)
    return result


def get_record(classparam, record_id):
    # return the record in classparams table with a certain id
    with Session(engine) as session:
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()  # very useful for converting into our data class
    return record


def create_record(record):
    # create a record in the database
    with Session(engine) as session:
        record.id = None
        session.add(record)
        session.commit()  # makes changes permanent in database


# region hold
def update_hold(hold):
    # update a record in the hold table
    with Session(engine) as session:
        session.execute(update(Hold).where(Hold.id == hold.id).values(erfaring=hold.erfaring, størrelse=hold.størrelse))
        session.commit()  # makes changes permanent in database


def delete_hard_hold(hold):
    # delete a record in the hold table
    with Session(engine) as session:
        session.execute(delete(Hold).where(Hold.id == hold.id))
        session.commit()  # makes changes permanent in database


def delete_soft_hold(hold):
    # soft delete a record in the hold table by setting its weight to -1 (see also method "valid" in the hold class)
    with Session(engine) as session:
        session.execute(update(Hold).where(Hold.id == hold.id).values(erfaring=-1, størrelse=hold.størrelse))
        session.commit()  # makes changes permanent in database
# endregion hold

# region bane
def update_bane(bane):
    # update a record in the bane table
    with Session(engine) as session:
        session.execute(update(Bane).where(Bane.id == bane.id).values(kapacitet=bane.kapacitet, sværhedsgrad=bane.sværhedsgrad))
        session.commit()  # makes changes permanent in database


def delete_hard_bane(bane):
    # delete a record in the bane table
    with Session(engine) as session:
        session.execute(delete(Bane).where(Bane.id == bane.id))
        session.commit()  # makes changes permanent in database


def delete_soft_bane(bane):
    # soft delete a record in the bane table by setting its weight to -1 (see also method "valid" in the hold class)
    with Session(engine) as session:
        session.execute(update(Bane).where(Bane.id == bane.id).values(kapacitet=-1, sværhedsgrad=bane.sværhedsgrad))
        session.commit()  # makes changes permanent in database
# endregion bane

# region booking
def update_booking(booking):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # update a record in the booking table
    with Session(engine) as session:
        session.execute(update(Booking).where(Booking.id == booking.id).values(date=booking.date, hold_id=booking.hold_id, bane_id=booking.bane_id))
        session.commit()  # makes changes permanent in database


def delete_hard_booking(booking):
    # delete a record in the booking table
    with Session(engine) as session:
        session.execute(delete(Booking).where(Booking.id == booking.id))
        session.commit()  # makes changes permanent in database
# endregion booking

if __name__ == "__main__":  # Executed when invoked directly
    # The next 2 lines are needed _after_ data classes / sql tables were defined
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
    # create_test_data()
    print(select_all(Hold))
    print(get_record(Hold, 2))
else:  # Executed when imported
    engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
    Base.metadata.create_all(engine)

# create_test_data()
