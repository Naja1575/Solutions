from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract
import S2_data as S2d
import S2_sql as S2sql


def plads(bane, hold):
    # does the bane have capacity for the hold
    return bane.kapacitet >= hold.størrelse


def skill(bane, hold):
    # does the hold have erfaring for sværhedsgraden
    return bane.sværhedsgrad <= hold.erfaring


def max_one(bane, date_):
    # return the bane's destination at a certain date in the booking table
    with Session(S2sql.engine) as session:
        records = session.scalars(select(S2d.Booking).where(S2d.Booking.bane_id == bane.id).where(extract('day', S2d.Booking.date) == date_.day).where(extract('month', S2d.Booking.date) == date_.month).where(extract('year', S2d.Booking.date) == date_.year))
        counter = 0
        for rec in records:
            counter += 1
    return counter == 0