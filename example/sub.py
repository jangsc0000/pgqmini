from pgqmini import PGQ
import time

# Create an instance of the PGQ class with the provided parameters
pgq = PGQ(
    qname="message_queue",
    dbname="pgq",
    host="127.0.0.1",
    user="username",
    password="password",
    port=5432,
)

# Connect to the PostgreSQL server and create the queue if it doesn't exist
pgq.connect()


# Define a function to process the messages.
# In this case, it simply prints the message and waits for 5 seconds.
def process_message(msg):
    print(msg)
    time.sleep(5)


# Run an infinite loop to continuously process the messages from the queue
while True:
    try:
        # Check for any messages that have been in 'PROCESSING' state
        # for more than 10 seconds and revert them back to 'PENDING'
        pgq.rollback_timeout_messages(timeout=10)

        # Fetch a 'PENDING' message from the queue for processing
        msg = pgq.sub_message()

        # Process the fetched message
        process_message(msg)

        # Mark the message as 'COMPLETED' after successful processing
        pgq.complete_message(msg)
    except KeyboardInterrupt as e:
        # In case of an interruption, the status of the message is reverted back to 'PENDING'
        # and the connection to the PostgreSQL server is closed
        pgq.rollback_message(msg)
        pgq.disconnect()
        exit()
    except Exception as e:
        # If any other exception occurs during processing,
        # the status of the message is reverted back to 'PENDING'
        pgq.rollback_message(msg)
