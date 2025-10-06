from VISHALMUSIC.core.bot import JARVIS
from VISHALMUSIC.core.dir import dirr
from VISHALMUSIC.core.git import git
from VISHALMUSIC.core.userbot import Userbot
from VISHALMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = JARVIS()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
