import re

from celery import Celery

from conf import HOST, PORT

BROKER_URL = 'mongodb://%s:%s/jobs' % (HOST, PORT)

celery = Celery('POC_TASKS', broker=BROKER_URL)
celery.config_from_object('conf')


@celery.task
def chef_task(phrase):
    """convert HTML to Swedish Chef-speak
    Cribbed from Mark Pilgrim's "Dive Into Python" - http://www.diveintopython.net/html_processing/index.html -
    code at http://www.siafoo.net/snippet/133
   which was based on the classic chef.x, copyright (c) 1992, 1993 John Hagerman
   """

    subs = ((r'a([nu])', r'u\1'),
            (r'A([nu])', r'U\1'),
            (r'a\B', r'e'),
            (r'A\B', r'E'),
            (r'en\b', r'ee'),
            (r'\Bew', r'oo'),
            (r'\Be\b', r'e-a'),
            (r'\be', r'i'),
            (r'\bE', r'I'),
            (r'\Bf', r'ff'),
            (r'\Bir', r'ur'),
            (r'(\w*?)i(\w*?)$', r'\1ee\2'),
            (r'\bow', r'oo'),
            (r'\bo', r'oo'),
            (r'\bO', r'Oo'),
            (r'the', r'zee'),
            (r'The', r'Zee'),
            (r'th\b', r't'),
            (r'\Btion', r'shun'),
            (r'\Bu', r'oo'),
            (r'\BU', r'Oo'),
            (r'v', r'f'),
            (r'V', r'F'),
            (r'w', r'w'),
            (r'W', r'W'),
            (r'([a-z])[.]', r'\1.  Bork Bork Bork!'))

    for fromPattern, toPattern in subs:
        phrase = re.sub(fromPattern, toPattern, phrase)
    return phrase
