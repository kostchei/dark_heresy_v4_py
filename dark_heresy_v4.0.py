import random

# Frequency distribution for patrons
patron_distribution = {
    "Adeptus Administratum": range(1, 11),
    "Adeptus Astra Telepathica": range(11, 16),
    "Adeptus Mechanicus": range(16, 31),
    "Adeptus Ministorum": range(31, 40),
    "Astra Militarum": range(40, 55),
    "Imperial Fleet": range(55, 65),
    "Infractionists": range(65, 75),
    "The Inquisition": range(75, 95),
    "Rogue Trader Dynasty": range(95, 101)
}

# Function to choose a patron based on the frequency distribution
def choose_patron(distribution):
    random_number = random.randint(1, 100)
    for patron, freq_range in distribution.items():
        if random_number in freq_range:
            return patron
    return "Unknown"  # Fallback in case of an unexpected result

# Sample data for other categories
factions = ["Faction 1", "Faction 2", "Faction 3"]
origins = ["Origin 1", "Origin 2", "Origin 3"]
roles = ["Role 1", "Role 2", "Role 3"]
skills = ["Skill 1", "Skill 2", "Skill 3"]
talents = ["Talent 1", "Talent 2", "Talent 3"]
equipment = ["Equipment 1", "Equipment 2", "Equipment 3"]
names = ["Name 1", "Name 2", "Name 3"]

# Function to create a character
def create_character():
    character = {
        "Patron": choose_patron(patron_distribution),
        "Faction": random.choice(factions),
        "Origin": random.choice(origins),
        "Role": random.choice(roles),
        "Skill": random.choice(skills),
        "Talent": random.choice(talents),
        "Equipment": random.choice(equipment),
        "Name": random.choice(names)
    }
    return character

# Function to write the character to a file
def write_character_to_file(filename):
    character = create_character()
    with open(filename, 'w') as file:
        for key, value in character.items():
            file.write(f"{key}: {value}\n")

# Usage
write_character_to_file("dark_heresy_character.txt")

