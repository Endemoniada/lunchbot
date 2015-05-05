#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib
import muncher

from twisted.words.protocols import irc
from twisted.internet import protocol, reactor


class LunchBot(irc.IRCClient):
    """ LunchBot body """

    def __init__(self):
        self.nickname = factory.nickname
        self.realname = factory.realname

    def connectionMade(self):
        """ Called when a connection is made to the server """
        # TODO: Add logging functionality.
        irc.IRCClient.connectionMade(self)

    def connectionLost(self, reason):
        """ Called when a connection is lost from the server """
        # TODO: Add logging functionality.
        irc.IRCClient.connectionLost(self, reason)

    def signedOn(self):
        """ Called when the bot is actually signed on to server """
        # TODO: Add logging functionality.
        self.join(self.factory.channel)

    def joined(self, channel):
        """ Called when the bot joins a channel """
        # TODO: Add logging functionality.
        pass

    def privmsg(self, user, channel, message):
        """ Called when LunchBot receives a message """
        user = user.split('!', 1)[0]
        # TODO: Add logging functionality.

        # Check if LunchBot gets a private message
        if channel == self.nickname:
            msg_slap = 'Don\'t you dare message me again!'
            self.msg(user, msg_slap)

        # Check if message is directed to LunchBot
        if message.startswith('!lunch'):
            self.msg(channel, muncher.get_lunch())

    def alterCollidedNick(self, nickname):
        """ If our name is taken; alter the name """
        return '{0}_'.format(nickname)

    def action(self, user, channel, data):
        """ Called if LunchBot see someone trigger an action like /me"""
        pass


class LunchBotFactory(protocol.ClientFactory):
    """ Factory to bake our LunchBot! """

    protocol = LunchBot

    def __init__(self, nickname, realname, channel):
        self.nickname = nickname
        self.realname = realname
        self.channel = channel

    def clientConnectionLost(self, connector, reason):
        """ If we get disconnected, reconnect again """
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        """ If connection fails, shutdown the baking factory """
        reactor.stop()


if __name__ == '__main__':
    # Create factory and bring bot to life!
    factory = LunchBotFactory('LunchBot', 'LunchBot', 'lunchbot-dev')
    reactor.connectTCP('irc.freenode.org', 6667, factory)

    # Start LunchBot
    reactor.run()