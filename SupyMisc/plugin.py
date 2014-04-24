###
# Copyright (c) 2014, James Lu (GLolol)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.world as world
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('SupyMisc')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x

class SupyMisc(callbacks.Plugin):
    """Add the help for "@plugin help SupyMisc" here
    This should describe *how* to use this plugin."""
    threaded = True

    ### Some semi-useful utilities
    def words(self, irc, msg, args, text):
        """<text>
        Returns the amount of words in <text> (separated by spaces). """
        irc.reply(len(text.split()))
    words = wrap(words, ['text'])
    
    def repeat(self, irc, msg, args, num, text):
        """<num> <text>
        Returns <text> repeated <num> times. <num> must be a positive integer. 
        To keep leading and trailing spaces, it is recommended to quote the <text>
        argument " like this ". """
        max = self.registryValue("repeat.max")
        if num <= max:
            irc.reply(text * num)
        else:
            irc.error("The <num> value given is too large. Current "
                "maximum: {}".format(max), Raise=True)
    repeat = wrap(repeat, ['positiveInt', 'text'])
    
    ### Generic informational commands (ident fetcher, channel counter, etc.)
    def netcount(self, irc, msg, args):
        """takes no arguments.
        Counts the amount of networks the bot is on. """
        irc.reply(len(world.ircs))
    netcount = wrap(netcount)
    
    def supyplugins(self, irc, msg, args):
        """takes no arguments.
        Returns a URL for the source of this plugin. """
        irc.reply("SupyPlugins source is available at: https://github.com/GLolol/SupyPlugins")
    supyplugins = wrap(supyplugins)

    def chancount(self, irc, msg, args):
        """takes no arguments.
        Counts the amount of channels the bot is on. """
        irc.reply(len(irc.state.channels.keys()))
    chancount = wrap(chancount)

    def getchan(self, irc, msg, args):
        """takes no arguments.
        Returns the name of the current channel. """
        channel = msg.args[0]
        if ircutils.isChannel(channel):
             irc.reply(channel)
        else:
             irc.reply(None)
    getchan = wrap(getchan)
        
    def me(self, irc, msg, args):
        """takes no arguments.
        Returns the nick of the person who called the command.
        """
        irc.reply(msg.nick)
    me = wrap(me)

    def botnick(self, irc, msg, args):
        """takes no arguments.
        Returns the nick of the bot.
        """
        irc.reply(irc.nick)
    botnick = wrap(botnick)

    def getident(self, irc, msg, args, nick):
        """[<nick>]
        Returns the ident of <nick>. If <nick> is not given, returns the host
        of the person who called the command.
        """
        if not nick:
            nick = msg.nick
        irc.reply(ircutils.userFromHostmask(irc.state.nickToHostmask(nick)))
    getident = wrap(getident, [(additional('nick'))])

    def gethost(self, irc, msg, args, nick):
        """[<nick>]
        Returns the host of <nick>. If <nick> is not given, return the host
        of the person who called the command.
        """
        if not nick:
            nick = msg.nick
        irc.reply(ircutils.hostFromHostmask(irc.state.nickToHostmask(nick)))
    gethost = wrap(gethost, [(additional('nick'))])
    
    ### Access to python built-in functions
    def int2bin(self, irc, msg, args, num):
        """<int>
        Returns the binary representation of <int>.
        """
        out = bin(int(num))
        irc.reply(out)
    int2bin = wrap(int2bin, ['int'])
    
    def int2hex(self, irc, msg, args, num):
        """<int>
        Returns the hexadecimal representation of <int>.
        """
        out = hex(int(num))
        irc.reply(out)
    int2hex = wrap(int2hex, ['int'])
    
    def bin2int(self, irc, msg, args, num):
        """<binary>
        Returns the decimal representation of <binary>.
        """
        try:
            irc.reply(int(num, base=2))
        except ValueError:
            irc.error("Invalid input: {}.".format(num))
    bin2int = wrap(bin2int, ['somethingWithoutSpaces'])
    
    def hex2int(self, irc, msg, args, num):
        """<hex>
        Returns the decimal representation of <hex>.
        """
        try:
            irc.reply(int(num, base=16))
        except ValueError:
            irc.error("Invalid input: {}.".format(num))
    hex2int = wrap(hex2int, ['somethingWithoutSpaces'])

Class = SupyMisc

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
