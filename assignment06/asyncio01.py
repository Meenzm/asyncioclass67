import asyncio

class AsyncDatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
    
    async def __aenter__(self):
        print(f'Connection to the database {self.db_name}...')
        await asyncio.sleep(1) # simulate asyn connectio setup
        print(f'Connected to the database {self.db_name}')
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        print(f'Closing the database connection to {self.db_name}...')
        await asyncio.sleep(1) # simulate asyn connectio teardown
        print(f'Closed the database connection to {self.db_name}.')
        if exc:
            print(f'An exception occurred: {exc}')
    
    async def fetch_data(self):
        await asyncio.sleep(1) # simulate an async data fetch
        return {"data" : "sample data"}
    
async def main():
    async with AsyncDatabaseConnection('my_db') as db:
        data = await db.fetch_data()
        print(f"Fetched data: {data}")
        
# Running the asyn main function
asyncio.run(main())