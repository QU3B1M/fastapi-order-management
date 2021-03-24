from app.db.repositories.base import BaseRepository
from app.db.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate


class CustomerRepository(BaseRepository[Customer, CustomerCreate, CustomerUpdate]):
    """
    Class with methods to Create, Read, Update and Delete a Customer.
    """

    pass


customer = CustomerRepository(Customer)