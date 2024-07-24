import aiofiles
import asyncio
import json

pokemonapi_directory = 'assignment07\pokemon\pokemonapi'
pokemonmove_directort = 'assignment07\pokemon\pokemonmove'

async def main():
    # Read the contents of the json file.
    async with aiofiles.open(f'{pokemonapi_directory}/articuno.json', mode='r') as f: contents = await f.read()
    print(contents)
    
    # Load it into a dictionary and create a list of name.
    pokemon = json.loads(contents)
    print(pokemon['name'])
    
asyncio.run(main())
    
