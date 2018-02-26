# -*- coding: utf-8 -*-
from reddit import ui
from click.exceptions import ClickException


class RedditException(ClickException):

    def __init__(self, message):
        BaseException.__init__(self, message)

    def show(self):
        name = self.__class__.__name__
        ui.echo(u'{}: {}'.format(name, self.message), fg='red')


class RedditApiError(RedditException):

    def __init__(self, message):
        RedditException.__init__(self, message)


class SubredditNotFound(RedditException):

    def __init__(self, message):
        RedditException.__init__(self, message)


class InvalidOption(RedditException):

    def __init__(self, message):
        RedditException.__init__(self, message)
