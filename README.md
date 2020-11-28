# Discord Chatbot
Discord Chatbot which is easy to use for everyone. 

## Description
Chatbot get a query and search for the most similar in database, then write answer.

## Installation
chatbot.py
```
@client.event
async def on_message(message):
	# you server goes here
	server_id = 123456780534543543
	
	id = client.get_guild(server_id)
	# type channel name where bot will be working
	channels = ["general"]
```
Customize id of your server and channels where bot will be working.

Run script and everything is done!

## Requirements
Python 3.6+ is required.

## Usage
Adding new queries to the database manually:
database.json
```
{
    "query1": [
        "answer1",
        "answer2",
        "answer3"
    ],
    "query2": [
        "answer4",
        "answer5",
        "answer6"
    ],
}
```
Adding new queries to the database through Discord:
Ask a question, if answer isn't as you expected type: .correct expected_answer.

## Author
The author of this project is Jakub Rudnik.