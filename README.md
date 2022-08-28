# Chat Data Frame
## About
Chat Data Frame is a simple python script which takes exported WhatsApps chat data
and generates a pandas data frame of this data.

The generated data frame has columns for: message date, message time, message sender and message
content.

## Obtain WhatsApp Data
[This guide](https://faq.whatsapp.com/196737011380816/?helpref=search&query=export%20chat%20history&search_session_id=13b2f689afbc8a73cac18906bb3169d1&sr=0) details how to download WhatsApp chat data.

## Missing Messages
Some messages may fail to be added to the data frame. This is usually due to the fact that the
message is not in a form the script expects or that the message contains charters that are
used by the script to split the message.

All messages that are not added to the data frame are added to the 'failed_messages.txt'. This
can be found in the same directory that the script was run from after the script finishes running.

Once the script has run it will indicate what percentage of the original data was added to the
data frame.

## Media in Messages
When exporting chat data, WhatsApp will offer to export with or without media files attached.
Chat Data Frame has only been tested on data without media files.

When exporting without media the message content in the data will indicate what type of media was
omitted.
