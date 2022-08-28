"""
A simple script to create a Pandas Data Frame from WhatsApp chat data.
"""
import re

import pandas as pd


def make_data_frame(data_file):
    """Create a data frame from WhatsApp chat data."""

    with open(data_file) as f:
        chat_log = f.read().split('\n')
    
    # Prepare the date for placing into data frame
    prepared_data = _split_data(chat_log)

    data_dictionary = {
            'date': prepared_data[0], # message_date
            'time': prepared_data[1], # message_time
            'sender': prepared_data[2], # message_sender
            'content': prepared_data[3], # message_content
            }

    chat_data = pd.DataFrame(data_dictionary)

    # Percentage of messages in the data successfully add to the data frame 
    percentage = (len(prepared_data[0]) / len(chat_log)) * 100
    print(f"\n{round(percentage, 2)} % of chat data added to data frame.")
    print("Missing message have been written to the file 'failed_messages.txt'.")

    return chat_data


def _split_data(chat_log):
    """Split data string up into date, time, sender and message parts."""
    # Date the message was sent
    message_date = []
    # Time the message was sent
    message_time = []
    # Sender of the message
    message_sender = []
    # Message content
    message_content = []
    # To hold messages which do not split correctly
    failed_messages = []

    for message in chat_log:
        # Split the message into date/time, sender and content
        split_message = re.split(r'] |: ', message)
        
        # Check if the string has been split correctly (into 3 parts)
        if len(split_message) == 3:
            message_date.append(split_message[0])
            message_sender.append(split_message[1])
            message_content.append(split_message[2])
        else:
            # Any messages not split correctly, to be written to a separate file
            failed_messages.append("".join(message))

    for index, date in enumerate(message_date):
        date_time_split = date.split(', ')
        message_time.append(date_time_split.pop())
        # Trim the unneeded character ([) from the start of the date
        message_date[index] = date_time_split.pop()[-10:]

    if len(failed_messages) > 0:
        _write_failed_data(failed_messages)

    return [message_date, message_time, message_sender, message_content]


def _write_failed_data(failed_messages):
    """Write messages which split incorrectly to a text file."""
    with open('failed_messages.txt', 'w') as f:
        for message in failed_messages:
            f.write(f"{message}\n")


if __name__ == '__main__':

    # Path to chat file downloaded from WhatsApp, update as needed 
    data_file = '_chat.txt'

    chat_data = make_data_frame(data_file)
