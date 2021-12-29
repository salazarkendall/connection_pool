import sys

from psycopg2 import pool

from logger_base import log


class Connection:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _MIN = 1
    _MAX = 5
    _pool = None

    # Why a connection pool?
    # It simplify connection reuse for performance purposes
    # Creates a pool connection with the database
    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN, cls._MAX, host=cls._HOST, user=cls._USERNAME,
                                                      password=cls._PASSWORD, port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.info('Successful pool connection')
                return cls._pool
            except Exception as e:
                log.error(f'Error: {e}')
                sys.exit()
        else:
            return cls._pool

    # Based on the pool, it creates a simple connection object that allow us to interact with the database
    @classmethod
    def get_conn(cls):
        connection = cls.get_pool().getconn()
        log.info(f'Successfully connected via pool: {connection}')
        return connection

    # Self explanatory, it releases the connection we specify if we are not going to used it any more
    @classmethod
    def release_conn(cls, connection):
        cls.get_pool().putconn(connection)
        log.debug(f'Connection released')

    # It closes all ongoing connections
    @classmethod
    def close_conn(cls):
        cls.get_pool().closeall()


if __name__ == '__main__':
    connection_test1 = Connection.get_conn()
    Connection.release_conn(connection_test1)
    connection_test2 = Connection.get_conn()
