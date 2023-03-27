from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from crud import get_all_Customers, create_Customer, get_Customer_info_by_id, update_Customer_info, delete_Customer_info
from database import get_db
from exceptions import CustomerInfoException
from schemas import Customer, CreateAndUpdateCustomer, PaginatedCustomerInfo

router = APIRouter()


# Example of Class based view
@cbv(router)
class Customers:
    session: Session = Depends(get_db)

    # API to get the list of Customer info
    @router.get("/Customers", response_model=PaginatedCustomerInfo)
    def list_Customers(self, limit: int = 10, offset: int = 0):

        Customers_list = get_all_Customers(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": Customers_list}

        return response

    # API endpoint to add a Customer info to the database
    @router.post("/Customers")
    def add_Customer(self, Customer_info: CreateAndUpdateCustomer):

        try:
            Customer_info = create_Customer(self.session, Customer_info)
            return Customer_info
        except CustomerInfoException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular Customer
@router.get("/Customers/{Customer_id}", response_model=Customer)
def get_Customer_info(Customer_id: int, session: Session = Depends(get_db)):

    try:
        Customer_info = get_Customer_info_by_id(session, Customer_id)
        return Customer_info
    except CustomerInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to update a existing Customer info
@router.put("/Customers/{Customer_id}", response_model=Customer)
def update_Customer(Customer_id: int, new_info: CreateAndUpdateCustomer, session: Session = Depends(get_db)):

    try:
        Customer_info = update_Customer_info(session, Customer_id, new_info)
        return Customer_info
    except CustomerInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a Customer info from the data base
@router.delete("/Customers/{Customer_id}")
def delete_Customer(Customer_id: int, session: Session = Depends(get_db)):

    try:
        return delete_Customer_info(session, Customer_id)
    except CustomerInfoException as cie:
        raise HTTPException(**cie.__dict__)