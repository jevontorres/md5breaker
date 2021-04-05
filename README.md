# MD5 Breaker (The "Lazy" Way)

IPS is a Python script that can "break" passwords hashed with the MD5 Algorithm. Created in a brainstorming attempt for ITP125 Final Project. This script reads through a file of hashes, and "translates" each one, relying on [another site](https://md5.gromweb.com/) to reverse the hash. I intend on replacing the web-scraping aspect with the same MD5 algorithm, or calling some function that can do the algorithm for me and then compare the result to a hashes.txt.

(Cheating) because the assignement seems to require actual work (rubric talks about reporting how long each password took and this would _theoretically_ just give a constant number based off internet connection) and not just scraping the result of a different unhasher. More of a thought experiment for myself and an attempt to bend the rules.

## Installation & Setup

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install MechanicalSoup.

```bash
pip install MechanicalSoup
```
Create a hashes.txt of MD5 hashes, which can be created [here](http://www.md5hasher.net/).
## Usage

```bash
python3 IPS.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. I don't exactly know how GitHub works so this seems standard.

## License
[MIT](https://choosealicense.com/licenses/mit/)
