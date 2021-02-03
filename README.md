# Events App

This is an app where you can find, create or go to an even. There is a DB of guests & events, have fun!


## Technology Used

- Flask
- Jinja2
- HTML/CSS
- SQL
- dotenv


## Install/Setup

### Install
```
pip3 install -r requirements.txt
```

### Setup
Make an `.env` file & add:
```
SQLALCHEMY_DATABASE_URI=sqlite:///database.db
```

### Run:
```
python3 app.py
```

## Img

***Homepage***
<img alt="Screenshot of the homepage, it has blocks that hold different events." src="https://github.com/lwrgithub/events-app/blob/main/events_app/static/img/home-pg.png" />

***Event***
<img alt="Screenshot of event page where you can add guests it has a form to do this." src="https://github.com/lwrgithub/events-app/blob/main/events_app/static/img/event-page.png" />

***Guest***
<img alt="Guest page, here you can view info about a specific guest such as email and phone." src="https://github.com/lwrgithub/events-app/blob/main/events_app/static/img/view-guest-page.png" />