import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import setup
spotifyObject = setup.run()
import methods
import pprint
#print("output:", methods.currentlyPlaying(spotifyObject))

#print("output:", methods.userInfo(spotifyObject))

#print("output:", methods.searchArtist(spotifyObject, "tuxx"))
a = methods.searchSong(spotifyObject, "post malone")
pprint.pprint(a, width=1)
