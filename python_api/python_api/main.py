#how to connect to an API using Python
import requests

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url) #give me this information at this url
    print(response) #prints 200, the response was okay
    
    if response.status_code == 200:
        pokeymon_data = response.json() #key value pairs
        return pokeymon_data
    else:
        print(f"Failed to retrieve data {response.status_code}.")
    
pokemon_name = "greninja"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}") #pokemon
    print(f"ID: {pokemon_info["id"]}") #658 pokemon in the franchise
    print(f"Height: {pokemon_info["height"]}") #height
    print(f"Weight: {pokemon_info["weight"]}") #weight
    