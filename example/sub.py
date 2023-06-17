from pgqmini import PGQ
import time
import threading

# Create an instance of the PGQ class with the provided parameters
pgq = PGQ(
    # The name of the queue
    qname="message_queue",
    # The name of the database
    dbname="pgq",
    # The hostname of the PostgreSQL server
    host="127.0.0.1",
    # The username for the PostgreSQL server
    user="username",
    # The password for the PostgreSQL server
    password="password",
    # The port on which the PostgreSQL server is listening
    port=5432,
)

# Connect to the PostgreSQL server and create the queue if it doesn't exist
pgq.connect()


# Define a function to periodically rollback messages that have timed out
def start_rollback_timeout_messages(pgq: PGQ, timeout, period):
    while True:
        # Rollback any messages that have timed out
        pgq.rollback_timeout_messages(timeout=10)
        # Pause for the timeout duration before running again
        time.sleep(20)


# Start the rollback_timeout_messages method in another thread
rollback_thread = threading.Thread(
    target=start_rollback_timeout_messages, args=(pgq, 10)
)
rollback_thread.start()


# Define a function to process the messages.
# In this case, it simply prints the message and waits for 5 seconds.
def process_message(payload: str):
    # Print the payload of the message
    print(payload)
    # Wait for 5 seconds to simulate processing time
    time.sleep(5)


# Run an infinite loop to continuously process the messages from the queue
while True:
    # Process messages from the queue
    pgq.sub(process_message)
