# coding: utf-8

from tapioca import (TapiocaAdapter, generate_wrapper_from_adapter,
                     JSONAdapterMixin)

from .resource_mapping import TELEGRAM_BOT_RESOURCE_MAPPING


class TelegramBotClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    resource_mapping = TELEGRAM_BOT_RESOURCE_MAPPING

    def get_api_root(self, api_params):
        if hasattr(self, 'api_root'):
            return self.api_root

        token = api_params.get('token')
        if not token:
            raise AttributeError('missing token')

        # API url format: https://api.telegram.org/bot<token>/<methods>
        api_root = 'https://api.telegram.org/'
        self.api_root = '{}bot{}'.format(api_root, token)
        return self.api_root


TelegramBot = generate_wrapper_from_adapter(TelegramBotClientAdapter)
