from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Date
from dateutil import parser
from tkinter import messagebox

Base = declarative_base()  # creating the registry and declarative base classes - combined into one step. Base will serve as the base class for the ORM mapped classes we declare.


class Hold(Base):
    __tablename__ = "hold"
    id = Column(Integer, primary_key=True)
    erfaring = Column(Integer)
    størrelse = Column(Integer)

    def __repr__(self):  # Only for test purposes.
        return f"Hold({self.id=:4}    {self.erfaring=:2}    {self.størrelse=:4})"

    def convert_to_tuple(self):  # Convert to tuple
        return self.id, self.erfaring, self.størrelse

    def valid(self):
        try:
            value = int(self.størrelse)
            value2 = int(self.erfaring)
        except ValueError:
            return False
        return value >= 0 and 0 <= value2 <= 2

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Hold
        hold = Hold(id=tuple_[0], erfaring=tuple_[1], størrelse=tuple_[2])
        return hold


class Bane(Base):
    __tablename__ = "bane"
    id = Column(Integer, primary_key=True)
    kapacitet = Column(Integer)
    sværhedsgrad = Column(Integer)

    def __repr__(self):  # Only for test purposes.
        return f"Bane({self.id=:2}    {self.kapacitet=:12}    {self.sværhedsgrad=:1})"

    def convert_to_tuple(self):  # Convert to tuple
        return self.id, self.kapacitet, self.sværhedsgrad

    def valid(self):
        try:
            value = int(self.kapacitet)
            value2 = int(self.sværhedsgrad)
        except ValueError:
            return False
        return value >= 0 and 0 <= value2 <= 2

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Bane
        bane = Bane(id=tuple_[0], kapacitet=tuple_[1], sværhedsgrad=tuple_[2])
        return bane


class Booking(Base):
    __tablename__ = "booking"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    hold_id = Column(Integer, ForeignKey("hold.id"), nullable=False)
    bane_id = Column(Integer, ForeignKey("bane.id"), nullable=False)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Booking({self.id=:3}    {self.date=}    {self.hold_id=:5}    {self.bane_id=:8})"

    def convert_to_tuple(self):  # Convert Container to tuple
        return self.id, self.date, self.hold_id, self.bane_id

    def valid(self):
        try:
            value = int(self.hold_id)
            value2 = int(self.bane_id)
        except ValueError:
            return False
        return value >= 0 and value2 >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to booking
        try:
            if tuple_[0] != '':
                id_ = int(tuple_[0])
            else:
                id_ = 0
            date = parser.parse(tuple_[1])
            hold_id = int(tuple_[2])
            bane_id = int(tuple_[3])
            booking = Booking(id=id_, date=date, hold_id=hold_id, bane_id=bane_id)
            return booking
        except:
            messagebox.showwarning("", "Entries could not be converted to booking!")
