# Tapioca Telegram Bot API

## Installation
```
pip install tapioca-telegram-bot-api
```

## Documentation
``` python
from tapioca_telegram_bot_api import TelegramBotApi


api = TelegramBotApi(token=<token>)

api.get_me().get()
# <TapiocaClient object
# {   'ok': True,
#     'result': {   'first_name': 'tapiocabot',
#                   'id': 789123,
#                   'username': 'tapiocabot'}}>

api.send_message().post(data={'chat_id': '123456',
                              'text': 'Hello, World'})
# {   'ok': True,
#     'result': {   'chat': { 'first_name': 'Marco',
#                             'id': 123456,
#                             'last_name': 'Rougeth',
# ...

```

> We support GET and POST HTTP methods.
_https://core.telegram.org/bots/api#making-requests_

You can use `.get(params={})` or `.post(data={})` with all api methods.

No more documentation needed.

- Learn how Tapioca works [here](http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html)
- Explore this package using iPython
- Have fun!
