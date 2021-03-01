from api.crud.base import CRUDBase
from api.models.customer import Customer
from api.schemas.customer import CustomerCreate, CustomerUpdate


class CRUDCustomer(CRUDBase[Customer, CustomerCreate, CustomerUpdate]):
    pass


customer = CRUDCustomer(Customer)