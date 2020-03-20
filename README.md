# SupyPlugins

My collection of plugins for [Limnoria](https://github.com/ProgVal/Limnoria).

## WARNING: THIS BRANCH IS END OF LIFE

**As Python 2 is EOL and Limnoria has dropped support for it, this branch is end of life as of March 2020**. Please migrate your bot to Python 3 and use the *master* branch instead.

## Installation
The recommended way of fetching plugins in this repository is to clone the git repository:

* `$ git clone https://github.com/jlu5/SupyPlugins`

and add the folder to your bot's `config directories.plugins`.

## Support
If you have any questions, concerns, or feature requests, feel free to submit an issue. Pull requests are welcome and appreciated.

Or, you can find me on IRC at: `irc.overdrivenetworks.com #dev`

## License
Unless otherwise noted, all plugins are available under a 3 clause BSD license (inserted at the top of each file).

## List of plugins
Please note that this list may not always be up to date; your best bet is to actually browse the code for yourself! Any specific plugin dependencies should also be listed.

Most of these plugins also have their own READMEs in their folders; you can usually find a usage demonstration or further explanation of what they do.

##### CtcpNext
- Alternative to the official Ctcp plugin, with a database for configurable replies.

##### DDG
- Provides an interface to DuckDuckGo's web search.
   - **Requires:** [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)

##### LastFM
- LastFM plugin, forked from [krf/supybot-lastfm](https://github.com/krf/supybot-lastfm).

##### [Namegen](Namegen/README.md)
- A small random name generator.

##### [NoTrigger](NoTrigger/README.md)
- Anti-abuse script; prevents the bot from triggering other bots by modifying its output slightly. For more information, see [NoTrigger/README.md](NoTrigger/README.md).

##### [OperUp](OperUp/README.md)
- Allows Supybot to oper up on configured networks, automatically (on connect) and on demand.

##### PassGen
- Generates random passwords on the fly!

##### [PkgInfo](PkgInfo/README.md)
- Fetches package information from various Linux and BSD distros' software repositories.
   - **Requires:** [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)

##### QuakeNet
- Log in to Quakenet's Q Service via CHALLENGEAUTH. This plugin was written by request and not officially supported.

##### Restart
- **EXPERIMENTAL**: provides a command to restart Limnoria from IRC.

##### [RelayNext](RelayNext/README.md)
- Next generation relayer plugin, designed with two-way relays in mind.

##### SedRegex
- History replacer using sed-style expressions. Fork of [t3chguy's Replacer plugin](https://github.com/t3chguy/Limnoria-Plugins/tree/master/Replacer).

##### SupyMisc
- Some assorted commands that don't seem to fit anywhere else.

##### SysDNS
- An alternative to Supybot's built-in DNS function, using the `host` DNS lookup utility on the host machine.
    * **Requires:** `host` DNS lookup binary (as in `/usr/bin/host`)

##### Voteserv
- A plugin for storing and manipulating votes/polls.

##### [Weather](Weather/README.md)
- My fork of [reticulatingspline's Weather](https://github.com/reticulatingspline/Weather) plugin, with rewritten output handling, explicit location search, and many other tweaks.

##### Wikifetch
- Fork of [ProgVal's Wikipedia plugin](https://github.com/ProgVal/Supybot-plugins), with support for other wikis (via a `--site` option) and other improvements.
