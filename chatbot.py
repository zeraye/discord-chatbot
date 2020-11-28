import discord
import Levenshtein
import json
import random
import asyncio
import difflib

def read_token():
	# you have to create file token.txt and write there your bot's token
	with open('token.txt', 'r') as file:
		lines = file.readlines()
		return lines[0].strip()

def similarity(word1, word2):
    return difflib.SequenceMatcher(None,word1,word2).ratio()

def read():
	with open("database.json", "r") as file:
		new_data = json.load(file)
		return new_data

def write(data, new_data):
	with open("database.json", "r+") as file:
		data.update(new_data)
		json.dump(data, file, indent=4)

def find_answer(word):
	data = read()
	best_accuracy = 0
	best_message = ""
	for message in data:
		if similarity(message, word) > best_accuracy:
			best_accuracy = similarity(message, word)
			best_message = message
		elif (similarity(message, word) == best_accuracy and
				random.randint(1,2) % 2 == 0):
			best_message = message
	return random.choice(data[best_message])

def add_answer(message, answer):
	data = read()
	new_data = data
	# adding answer to existing query
	try:
		new_data[message] += [answer]
	# adding new query and answer
	except KeyError:
		new_data.update({message: [answer]})
	finally:
		write(data, new_data)

token = read_token()

client = discord.Client()

@client.event
async def on_message(message):
	# you server goes here
	server_id = 123456780534543543
	
	id = client.get_guild(server_id)
	# type channel name where bot will be working
	channels = ["general"]

	if str(message.channel) in channels:
		if message.author.bot:
			return

		if message.content.startswith('.correct'):
			async for message_in_history in message.channel.history(
					limit=20, oldest_first=False):
				if (message.author == message_in_history.author and not
						message_in_history.content.startswith('.correct')):
					add_answer(message_in_history.content, message.content[9:])
					await message.channel.send(
						f"{message.author.mention} answer added")
					return

		else:
			answer = find_answer(message.content)
			await message.channel.send(f"{message.author.mention} {answer}")
			await message.channel.send(f"{message.author.mention} to correct"\
				" query type .correct <expected answer>")

client.run(token)