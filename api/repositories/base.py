from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from api.db.base_class import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """Class with default Repository metods."""

    def __init__(self, model: Type[ModelType]):
        """
        Object with default methods to Create, Read, Update, Delete (Repository).

        Parameters
        ----------
            model: SQLAlchemy model class
            schema: Pydantic model (schema) class
        """
        self.model = model

    async def get(self, db: Session, id: int) -> Optional[ModelType]:
        """
        Default method to Read a object from the DataBase by ID.

        Parameters
        ----------
            db: SQLAlchemy Session object.
            id: int.

        Return
        ------
            SQLAlchemy model Object.
        """
        return db.query(self.model).filter(self.model.id == id).first()

    async def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        """
        Default method to Read multiple objects from the DataBase.

        Parameters
        ----------
            db: SQLAlchemy Session object.
            skip: int = 0.
            limit: int = 100.

        Return
        ------
            List of SQLAlchemy model Objects.
        """
        return db.query(self.model).offset(skip).limit(limit).all()

    async def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        """
        Default method to Create an Object in the DataBase.

        Parameters
        ----------
            db: SQLAlchemy Session object.
            obj_in: Pydantic model (schema) Object.

        Return
        ------
            SQLAlchemy model Object.
        """
        obj_in_data = jsonable_encoder(obj_in)
        print(obj_in_data, flush=True)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    async def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        """
        Default method to Update an Object from the DataBase.

        Parameters
        ----------
            db: SQLAlchemy Session object.
            db_obj: SQLAlchemy model Object
            obj_in: Pydantic model (schema) Object.

        Return
        ------
            SQLAlchemy model Object.
        """
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    async def remove(self, db: Session, *, id: int) -> ModelType:
        """
        Default method to Delete an Object from the DataBase.

        Parameters
        ----------
            db: SQLAlchemy Session object.
            id: int

        Return
        ------
            SQLAlchemy model Object.
        """
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
