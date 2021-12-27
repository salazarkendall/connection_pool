from connection import Connection
from logger_base import log


class PoolCursor:
    def __init__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        log.debug('Initializing with connection')
        self._connection = Connection.get_conn()
        self._cursor = self._connection.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Executing exit method')
        if exc_val:
            self._connection.rollback()
            log.error(f'Executing rollback: {exc_type} {exc_tb} {exc_val}')
        else:
            self._connection.commit()
            log.debug('Transaction commit')
        Connection.release_conn(self._connection)
