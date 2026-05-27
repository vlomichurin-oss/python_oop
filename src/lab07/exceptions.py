class PlayerNotFoundError(Exception):
    pass


class DuplicatePlayerError(Exception):
    pass


class InvalidPlayerDataError(Exception):
    pass


class EmptyCollectionError(Exception):
    pass


class StorageError(Exception):
    pass