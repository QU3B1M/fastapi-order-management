from api.repositories.base import BaseRepository
from api.models.customer import Customer
from api.schemas.customer import CustomerCreate, CustomerUpdate


class CustomerRepository(BaseRepository[Customer, CustomerCreate, CustomerUpdate]):
    """
    Class with methods to Create, Read, Update and Delete a Customer.
    """

    pass


customer = CustomerRepository(Customer)