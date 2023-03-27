from typing import List
from sqlalchemy.orm import Session
from exceptions import CustomerInfoInfoAlreadyExistError, CustomerInfoNotFoundError
from models import CustomerInfo
from schemas import CreateAndUpdateCustomer


# Function to get list of Customer info
def get_all_Customers(session: Session, limit: int, offset: int) -> List[CustomerInfo]:
    return session.query(CustomerInfo).offset(offset).limit(limit).all()


# Function to  get info of a particular Customer
def get_Customer_info_by_id(session: Session, _id: int) -> CustomerInfo:
    Customer_info = session.query(CustomerInfo).get(_id)

    if Customer_info is None:
        raise CustomerInfoNotFoundError

    return Customer_info


# Function to add a new Customer info to the database
def create_Customer(session: Session, Customer_info: CreateAndUpdateCustomer) -> CustomerInfo:
    Customer_details = session.query(CustomerInfo).filter(CustomerInfo.manufacturer == Customer_info.manufacturer, CustomerInfo.modelName == Customer_info.modelName).first()
    if Customer_details is not None:
        raise CustomerInfoInfoAlreadyExistError

    new_Customer_info = CustomerInfo(**Customer_info.dict())
    session.add(new_Customer_info)
    session.commit()
    session.refresh(new_Customer_info)
    return new_Customer_info


# Function to update details of the Customer
def update_Customer_info(session: Session, _id: int, info_update: CreateAndUpdateCustomer) -> CustomerInfo:
    Customer_info = get_Customer_info_by_id(session, _id)

    if Customer_info is None:
        raise CustomerInfoNotFoundError

    Customer_info.manufacturer = info_update.manufacturer
    Customer_info.modelName = info_update.modelName
    Customer_info.fuelType = info_update.fuelType
    Customer_info.cc = info_update.cc
    Customer_info.gearBox = info_update.gearBox
    Customer_info.onRoadPrice = info_update.onRoadPrice
    Customer_info.seatingCapacity = info_update.seatingCapacity

    session.commit()
    session.refresh(Customer_info)

    return Customer_info


# Function to delete a Customer info from the db
def delete_Customer_info(session: Session, _id: int):
    Customer_info = get_Customer_info_by_id(session, _id)

    if Customer_info is None:
        raise CustomerInfoNotFoundError

    session.delete(Customer_info)
    session.commit()

    return
