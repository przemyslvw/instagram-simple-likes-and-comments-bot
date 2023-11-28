# instagram-simple-likes-and-comments-bot
instagram simple likes and comments bot  

EN info: The bot is a loop, it adds posts it encounters on its way to the list (buffor.json), and adds those it comments and likes to the archive.
Does not visit the same posts again (from archive.json).

PL info: Bot jest pętlą, dodaje posty które spotyka na drodze do listy (buffor.json), te które już skomentuje i polajkuje dodaje do archiwum.
Nie wchodzi ponownie na te same posty (z archiwum.json).

## Selenium and Python  

without HTTP error 429 Instagram

add to projest accounts.json
[{"username": "your.username", "password": "your.password"}]

commands:
pip install -r requirements.txt
python run.py