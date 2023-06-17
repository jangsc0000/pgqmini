# Import the PGQ class from the pgqmini module
from pgqmini import PGQ

# Create an instance of the PGQ class
pgq = PGQ(
    # qname: the name of the queue
    qname="message_queue",
    # dbname: the name of the database
    dbname="pgq",
    # host: the host address of the PostgreSQL server
    host="127.0.0.1",
    # user: the username to connect to the PostgreSQL server
    user="username",
    # password: the password to connect to the PostgreSQL server
    password="password",
    # port: the port number of the PostgreSQL server
    port=5432,
)

# Establish the connection to the PostgreSQL server
pgq.connect()

# Publish a message to the queue
# The message is a JSON string
pgq.pub('{"key1": "value1", "key2": "value2"}')

# Disconnect from the PostgreSQL server
pgq.disconnect()
