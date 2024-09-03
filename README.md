# Intruder_extention
A script automating PortSwigger lab.

The name of the lab is **Broken brute-force protection, IP block**.

The lab can be found here: https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block

There are 2 scripts where one is simple and the other is more advanced introducing **asynchronous** requests. In the context of this specific lab it doesn't make that much of a differnce because of the small amount of passwords to try.

## Usage
`extention.py <url>`\
`improved_version.py <url>`
### Example
`improved_version.py https://0a7700bb03a4730a8255d486008d0086.web-security-academy.net/login`
Notice the **/login** at the end.

> [!important]
> Make sure you have the necessary libraries installed, they are pretty common. If you don't have them just `pip install <name_of_library>`.

>[!Tip]
> Make sure you understand the core concepts before you use automated scripts, it's the most important part!
