from backend.dao.base_dao import BaseDao
from backend.models.base_model import BaseModel


class BaseController:
    def __init__(self, dao: BaseDao) -> None:
        self.__dao = dao

    def create(self, model: BaseModel) -> BaseModel:
        return self.__dao.save(model)

    def read_all(self) -> list:
        return self.__dao.read_all()

    def read_by_id(self, id_: int) -> BaseModel:
        return self.__dao.read_by_id(id_)

    def delete(self, model: BaseModel) -> None:
        self.__dao.delete(model)

    def update(self, model: BaseModel) -> BaseModel:
        return self.__dao.save(model)
