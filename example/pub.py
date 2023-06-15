# Import the PGQ class from the pgqmini module
from pgqmini import PGQ

# Create an instance of the PGQ class
# qname: the name of the queue
# dbname: the name of the database
# host: the host address of the PostgreSQL server
# user: the username to connect to the PostgreSQL server
# password: the password to connect to the PostgreSQL server
# port: the port number of the PostgreSQL server
pgq = PGQ(
    qname="message_queue",
    dbname="pgq",
    host="127.0.0.1",
    user="username",
    password="password",
    port=5432,
)

# Establish the connection to the PostgreSQL server
pgq.connect()

# Publish a message to the queue
# The message is a JSON string
pgq.pub_message('{"key1": "value1", "key2": "value2"}')

# Disconnect from the PostgreSQL server
pgq.disconnect()
