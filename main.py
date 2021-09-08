#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "5FCB30F6-EE46-44BE-94FB-4E67670E49A7",
  "name": "LoZ",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631059037625,
  "passages": [
	{
	  "name": "Hero's Forest",
	  "tags": "",
	  "id": "1",
	  "text": "This is your home. Where you've been raised and have never left. You are a young beast-person. The Great Grove has called on you to go on an adventure. An evil tyrant has captured the princess of your forest. Time to save her!\n\n(set: $Kingsword to false)\n(set: $key to false)\n\n* [[Exit the forest -> Phoenix Plains]]",
	  "links": [
		{
		  "linkText": "Phoenix Plains",
		  "passageName": "Phoenix Plains",
		  "original": "[[Exit the forest -> Phoenix Plains]]"
		}
	  ],
	  "hooks": [],
	  "cleanText": "This is your home. Where you've been raised and have never left. You are a young beast-person. The Great Grove has called on you to go on an adventure. An evil tyrant has captured the princess of your forest. Time to save her!"
	},
	{
	  "name": "Phoenix Plains",
	  "tags": "",
	  "id": "2",
	  "text": "A former lushious land now barren with ash and dead trees. It seems the tyrant has attacked the Kingdom that protects your forest. Will you go into town to investigate or go to the temple to explore?\n\n[[Kingdom City -> Kingdom City]] \n[[Temple -> Temple of Time]]\n(if: $map is true)[[Castle -> Phoenix King's Palace]]",
	  "links": [
		{
		  "linkText": "Kingdom City",
		  "passageName": "Kingdom City",
		  "original": "[[Kingdom City -> Kingdom City]]"
		},
		{
		  "linkText": "Temple",
		  "passageName": "Temple of Time",
		  "original": "[[Temple -> Temple of Time]]"
		},
		{
		  "linkText": "Castle",
		  "passageName": "Phoenix King's Palace",
		  "original": "[[Castle -> Phoenix King's Palace]]"
		}
	  ],
	  "hooks": [],
	  "cleanText": "A former lushious land now barren with ash and dead trees. It seems the tyrant has attacked the Kingdom that protects your forest. Will you go into town to investigate or go to the temple to explore?"
	},
	{
	  "name": "Kingdom City",
	  "tags": "",
	  "id": "3",
	  "text": "The city is filled with ghouls! You wonder what happened. Do you approach the ghouls or leave the city?\n\n[[Approach -> Kingdom City 2]]\n[[Leave -> Phoenix Plains]]",
	  "links": [
		{
		  "linkText": "Approach",
		  "passageName": "Kingdom City 2",
		  "original": "[[Approach -> Kingdom City 2]]"
		},
		{
		  "linkText": "Phoenix Plains",
		  "passageName": "Phoenix Plains",
		  "original": "[[Leave -> Phoenix Plains]]"
		}
	  ],
	  "hooks": [],
	  "cleanText": "The city is filled with ghouls! You wonder what happened. Do you approach the ghouls or leave the city?"
	},
	{
	  "name": "Temple of Time",
	  "tags": "",
	  "id": "4",
	  "text": "You enter the temple and see a sword in a stone. You pull it out and a blinding light shines.\n\n(set: $Kingsword to true)\n\n[[Leave -> Phoenix Plains]]",
	  "links": [
		{
		  "linkText": "Phoenix Plains",
		  "passageName": "Phoenix Plains",
		  "original": "[[Leave -> Phoenix Plains]]"
		}
	  ],
	  "hooks": [],
	  "cleanText": "You enter the temple and see a sword in a stone. You pull it out and a blinding light shines."
	},
	{
	  "name": "Kingdom City 2",
	  "tags": "",
	  "id": "5",
	  "text": "(if: $Kingsword is true)[(print: \"You killed the ghouls and obtained a map!\") (set: $map to true) [[Leave -> Phoenix Plains]]]\n\n(if: $Kingsword is false)[(print: \"You died! Restart the application to start over.\")]",
	  "links": [
		{
		  "linkText": "Phoenix Plains",
		  "passageName": "Phoenix Plains",
		  "original": "[[Leave -> Phoenix Plains]]"
		}
	  ],
	  "hooks": [
		{
		  "hookName": "Success",
		  "hookText": "You killed the ghouls and obtained a map!",
		  "original": "(if: $Kingsword is true)[(print: \"You killed the ghouls and obtained a map!\") (set: $map to true) [[Leave -> Phoenix Plains]]]\n\n(if: $Kingsword is false)[(print: \"You died! Restart the application to start over.\")]"
		},
		{
		  "hookName": "Fail",
		  "hookText": "You died! Type X to restart.",
		  "original": "(if: $Kingsword is true)[(print: \"You killed the ghouls and obtained a map!\") (set: $map to true) [[Leave -> Phoenix Plains]]]\n\n(if: $Kingsword is false)[(print: \"You died! Restart the application to start over.\")]"
		}
	  ],
	  "cleanText": ""
	},
	{
	  "name": "Phoenix King's Palace",
	  "tags": "",
	  "id": "6",
	  "text": "You enter an extravagant room with 3 doors! The door straight ahead is decorated with stone heads of some of your former villagers! The left door is slightly ajar, and the right door has a keyhole. Where will you go first?",
	  "links": [
		{
		  "linkText": "Straight",
		  "passageName": "Phoenix King's Throne Room",
		  "original": "[[Straight -> Phoenix King's Throne Room]]"
		},
		{
		  "linkText": "Left",
		  "passageName": "Key Room",
		  "original": "[[Left -> Key Room]]"
		},
		{
		  "linkText": "Right",
		  "passageName": "Armory",
		  "original": "[[[Right -> Armory]]]"
		}
	  ],
	  "hooks": [],
	  "cleanText": "You enter an extravagant room with 3 doors! The door straight ahead is decorated with stone heads of some of your former villagers! The left door is slightly ajar, and the right door has a keyhole. Where will you go first?"
	},
	{
	  "name": "Phoenix King's Throne Room",
	  "tags": "",
	  "id": "7",
	  "text": "You enter the Phoenix King's Throne Room. He appears to have been waiting for you.\n\n\"I will hang you on the door just like the ones before you!!!\"\n\n(if: $Kingsword is true and $shield is true)[[[Attack -> Phoenix King's Throne Room 2]]]",
	  "links": [
		{
		  "linkText": "Attack",
		  "passageName": "Phoenix King's Throne Room 2",
		  "original": "[[[Attack -> Phoenix King's Throne Room 2]]]"
		}
	  ],
	  "hooks": [],
	  "cleanText": "You enter the Phoenix King's Throne Room. He appears to have been waiting for you.\n\n\"I will hang you on the door just like the ones before you\""
	},
	{
	  "name": "Key Room",
	  "tags": "",
	  "id": "8",
	  "text": "You kill the minions in the room and they drop a key!\n\n(set: $key to true)\n\n[[Main Room -> Phoenix King's Palace]]",
	  "links": [
		{
		  "linkText": "Main Room",
		  "passageName": "Phoenix King's Palace",
		  "original": "[[Main Room -> Phoenix King's Palace]]"
		}
	  ],
	  "hooks": [],
	  "cleanText": "You kill the minions in the room and they drop a key!"
	},
	{
	  "name": "Armory",
	  "tags": "",
	  "id": "9",
	  "text": "You enter an armory! You found a steel shield! How useful!\n\n(set: $shield to true)\n\n[[Main Room -> Phoenix King's Palace]]",
	  "links": [
		{
		  "linkText": "Main Room",
		  "passageName": "Phoenix King's Palace",
		  "original": "[[Main Room -> Phoenix King's Palace]]"
		}
	  ],
	  "hooks": [],
	  "cleanText": "You enter an armory! You found a steel shield! How useful!"
	},
	{
	  "name": "Prison Room",
	  "tags": "",
	  "id": "10",
	  "text": "You have found the princess! You win! To play again, type X.",
	  "links": [],
	  "hooks": [],
	  "cleanText": "You have found the princess! You win! To play again, type X. To quit, type QUIT."
	},
	{
	  "name": "Phoenix King's Throne Room 2",
	  "tags": "",
	  "id": "11",
	  "text": "You have killed the Phoenix King! You look around and see a door creaked open. Is that where the princess is?\n\n[[Enter -> Prison Room]]",
	  "links": [
		{
		  "linkText": "Enter",
		  "passageName": "Prison Room",
		  "original": "[[Enter -> Prison Room]]"
		}
	  ],
	  "hooks": [
		  {
		  "hookName": "Win",
		  "hookText": "You dodge the first swipe from the King and swiftly swing your Kingsword! You decapitate the Phoenix King cleanly. You have killed the Phoenix King! You look around and see a door creaked open. Is that where the princess is?",
		  "original": "(if: $Kingsword is true and $shield is true)[[[Attack -> Phoenix King's Throne Room 2]]]"
		  },
		  {
		  "hookName": "Loss",
		  "hookText": "You have died! Type X to restart.",
		  "original": "(if: $Kingsword is true and $shield is false)(print: \"You Died\"))"
		  }
	  ],
	  "cleanText": ""
	}
  ]
}

# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, moves, kingsword, key, map, shield):
	if "name" in current_location and "cleanText" in current_location:
		name = current_location["name"]
		if name == "Kingdom City 2":
			name = "Kingdom City"
		if current_location["name"] == "Kingdom City 2":
			for hook in current_location["hooks"]:
					if kingsword and hook["hookName"] == "Success":
						name += "\n\n" + hook["hookText"]
						print("\n\nYou are at the " + name)
						print(current_location["cleanText"] + "\n")
						print("Moves: " + str(moves))
						print("Available Locations:")
						linkTexts = ""
						linkNameCheck = ""
						for links in current_location["links"]:
							linkNameCheck = links["linkText"]
							if linkNameCheck == "Castle":
								linkTexts += ""
							else:
								linkTexts += links["linkText"] + "\n"
						print(linkTexts)
					if not kingsword and hook["hookName"] == "Fail":
						name += "\n\n" + hook["hookText"]
						print("\n\nYou are at the " + name)
						print(current_location["cleanText"] + "\n")
						print("Moves: " + str(moves))

		if current_location["name"] == "Phoenix King's Throne Room 2":
			if name == "Phoenix King's Throne Room 2":
				name = "Phoenix King's Throne Room"
			for hook in current_location["hooks"]:
					if shield and hook["hookName"] == "Win":
						name += "\n\n" + hook["hookText"]
						print("\n\nYou are at the " + name)
						print(current_location["cleanText"] + "\n")
						print("Moves: " + str(moves))
						print("Available Locations:")
						linkTexts = ""
						linkNameCheck = ""
						for links in current_location["links"]:
							linkNameCheck = links["linkText"]
							if linkNameCheck == "Castle":
								linkTexts += ""
							else:
								linkTexts += links["linkText"] + "\n"
						print(linkTexts)
					if not shield and hook["hookName"] == "Loss":
						name += "\n\n" + hook["hookText"]
						print("\n\nYou are at the " + name)
						print(current_location["cleanText"] + "\n")
						print("Moves: " + str(moves))
		else:
			print("\n\nYou are at the " + name)
			print(current_location["cleanText"] + "\n")
			print("Moves: " + str(moves))
			print("Available Locations:")
			linkTexts = ""
			linkNameCheck = ""
			for links in current_location["links"]:
				linkNameCheck = links["linkText"]
				if ((linkNameCheck == "Castle" and not map) or (linkNameCheck == "Right" and not key)):
					linkTexts += ""
				else:
					linkTexts += links["linkText"] + "\n"
			print(linkTexts)


		# print("\n\nYou are at the " + name)
		# print(current_location["cleanText"] + "\n")
		# print("Moves: " + str(moves))
		# print("Available Locations:")
		# linkTexts = ""
		# linkNameCheck = ""
		# for links in current_location["links"]:
		# 	linkNameCheck = links["linkText"]
		# 	if linkNameCheck == "Castle":
		# 			linkTexts += ""
		# 	else:
		# 		linkTexts += links["linkText"] + "\n"
		# print(linkTexts)
	

def get_input():
	response = input("What do you want to do? ").strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again. \n\n")
	return location_label


# ----------------------------------------------------------------

location_label = "Hero's Forest"
current_location = {}
response = ""
moves = 0
kingsword = False
key = False
map = False
shield = False

while True:
	if response == "QUIT":
		break
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if current_location["name"] == "Temple of Time" and not kingsword:
		kingsword = True
	if  current_location["name"] == "Kingdom City 2" and kingsword:
		map = True
	if  current_location["name"] == "Key Room":
		key = True
	if  current_location["name"] == "Armory":
		shield = True
	render(current_location, moves, kingsword, key, map, shield)
	moves += 1
	response = get_input()
	if response == "X":
		location_label = "Hero's Forest"
		current_location = {}
		response = ""
		moves = 0
		kingsword = False
		key = False
		map = False
		shield = False


print("Thanks for playing!")