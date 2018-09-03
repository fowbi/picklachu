import abc


class BaseStorage:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def persist(self, path: str, data: bytes):
        raise NotImplementedError

    """Persist data to storage"""

    @abc.abstractmethod
    def retrieve(self, path: str):
        raise NotImplementedError

    """Retrieve data from storage"""
