#!/usr/bin/env python3
from datetime import datetime
from dev_aberto import hello
import gettext
from babel.dates import format_date


if __name__ == '__main__':
    gettext.install('cli', localedir='locale')
    date, name = hello()
    date = datetime(int(date[:4]),int(date[5:7]),int(date[8:10]), int(date[11:13]), int(date[14:16]), int(date[17:19]))
    date = format_date(date)
    print(_('Último commit feito em:'), _(date), _(' por'), name)
