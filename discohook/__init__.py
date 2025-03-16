"""
Discohook
~~~~~~~~~~~~~~~~~~~

A basic Library to send Discord Webhook

:copyright: (c) 2022 JanakXD
:license: MIT, see LICENSE for more details.

"""

__title__ = 'Discohook'
__author__ = 'JanakXD'
__license__ = 'MIT'
__copyright__ = 'Copyright 2022 JanakXD'
__version__ = '1.0.0'

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

__all__ = ["Discohook", "DiscohookEmbed"]

from .client import Discohook, DiscohookEmbed
