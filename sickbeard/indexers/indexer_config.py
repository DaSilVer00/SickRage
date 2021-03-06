# coding=utf-8

from tvdb_api.tvdb_api import Tvdb
from sickbeard import helpers

initConfig = {
    'valid_languages': [
        "da", "fi", "nl", "de", "it", "es", "fr", "pl", "hu", "el", "tr",
        "ru", "he", "ja", "pt", "zh", "cs", "sl", "hr", "ko", "en", "sv", "no"
    ],
    'langabbv_to_id': {
        'el': 20, 'en': 7, 'zh': 27,
        'it': 15, 'cs': 28, 'es': 16, 'ru': 22, 'nl': 13, 'pt': 26, 'no': 9,
        'tr': 21, 'pl': 18, 'fr': 17, 'hr': 31, 'de': 14, 'da': 10, 'fi': 11,
        'hu': 19, 'ja': 25, 'he': 24, 'ko': 32, 'sv': 8, 'sl': 30
    }
}

INDEXER_TVDB = 1
INDEXER_TVRAGE = 2  # Must keep

indexerConfig = {
    INDEXER_TVDB: {
        'id': INDEXER_TVDB,
        'name': 'theTVDB',
        'module': Tvdb,
        'api_params': {
            'apikey': '9DAF49C96CBF8DAC',
            'language': 'de',
            'useZip': True,
        },
        'session': helpers.make_session(),
        'trakt_id': 'tvdb_id',
        'xem_origin': 'tvdb',
        'icon': 'thetvdb16.png',
        'scene_loc': 'https://raw.githubusercontent.com/cytec/sickrage.github.io/master/scene_exceptions/scene_exceptions.json',
        'show_url': 'http://thetvdb.com/?tab=series&id=',
        'base_url': 'https://www.glotz.info/api/%(apikey)s/series/'
    }
}

indexerConfig[INDEXER_TVDB]['base_url'] %= indexerConfig[INDEXER_TVDB]['api_params']  # insert API key into base url
