import re

def split_data(chat_log):
    """Split data string up into date, time, sender and message parts."""
    # Date the message was sent
    message_date = []
    # Time the message was sent
    message_time = []
    # Sender of the message
    message_sender = []
    # Message content
    message_content = []

    for message in chat_log:
        # Split the message into date/time, sender and content
        split_message = re.split(r'] |: ', message)
        
        # Check if the string has been split correctly (into 3 parts)
        if len(split_message) == 3:
            message_date.append(split_message[0])
            message_sender.append(split_message[1])
            message_content.append(split_message[2])
        # This block will trigger if message was not split correctly
        else:
            # Messages here will be left out of data. Need to fix
            pass

    for index, date in enumerate(message_date):
        date_time_split = date.split(', ')
        message_time.append(date_time_split.pop())
        # Trim the unneeded character ([) from the start of the date
        message_date[index] = date_time_split.pop()[-10:]

    return [message_date, message_time, message_sender, message_content]


if __name__ == '__main__':

    # Path to chat file downloaded from WhatsApp 
    chat_data = 'Chat_Data/BDBoys_Chat.txt'

    with open(chat_data) as f:
        chat_log = f.read().split('\n')
    
    split_data(chat_log)
