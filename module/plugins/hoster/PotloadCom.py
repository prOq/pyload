# -*- coding: utf-8 -*-

from module.plugins.internal.DeadHoster import DeadHoster, create_getInfo


class PotloadCom(DeadHoster):
    __name__ = "PotloadCom"
    __type__ = "hoster"
    __version__ = "0.02"

    __pattern__ = r'http://(?:www\.)?potload\.com/\w{12}'

    __description__ = """Potload.com hoster plugin"""
    __license__ = "GPLv3"
    __authors__ = [("stickell", "l.stickell@yahoo.it")]


getInfo = create_getInfo(PotloadCom)
