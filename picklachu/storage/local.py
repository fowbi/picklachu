from picklachu.storage.base import BaseStorage


class Local(BaseStorage):
    def __init__(self, directory: str):
        self.directory = directory

    def persist(self, path: str, data: bytes):
        """Persist data to local storage

        Args:
            path (str): filename
            data (bytes): data in bytes

        Returns:
            None
        """
        with open(self.directory + path, 'wb') as file:
            file.write(data)

    def retrieve(self, path: str) -> bytes:
        """Retrieve data from local storage

        Args:
            path (str): filename

        Returns:
            Retrieved data in bytes
        """
        with open(self.directory + path, 'rb') as file:
            data = file.read()
        return data
