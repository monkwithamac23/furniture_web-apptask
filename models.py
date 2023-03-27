from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum
from database import Base
import enum


class FuelType(str, enum.Enum):
    Petrol = "Petrol"
    Diesel = "Diesel"


class CustomerInfo(Base):
    __tablename__ = "Customer"

    id = Column(Integer, primary_key=True, index=True)
    manufacturer = Column(String)
    modelName = Column(String)
    cc = Column(Integer)
    onRoadPrice = Column(Integer)
    seatingCapacity = Column(Integer)
    gearBox = Column(Integer)
    fuelType = Column(Enum(FuelType))
