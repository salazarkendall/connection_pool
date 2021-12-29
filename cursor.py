from connection import Connection
from logger_base import log


class PoolCursor:
    def __init__(self):
        self._connection = None
        self._cursor = None

    # Python executes this code when enter into 'PoolCursor' and when we use the 'with' code block
    def __enter__(self):
        log.debug('Initializing with connection')
        self._connection = Connection.get_conn()
        self._cursor = self._connection.cursor()
        return self._cursor

    # After a 'with' block, this code is executed
    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Executing exit method')
        if exc_val:
            self._connection.rollback()
            log.error(f'Executing rollback: {exc_type} {exc_tb} {exc_val}')
        else:
            self._connection.commit()
            log.debug('Transaction commit')
        Connection.release_conn(self._connection)


if __name__ == '__main__':
    with PoolCursor() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        data = cursor.fetchall()
        for persona in data:
            print(persona)
