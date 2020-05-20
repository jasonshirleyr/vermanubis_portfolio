from django.db import models

# Music will be used to store all information regarding the "Music" section of Vermanubis portfolio.
class About(models.Model):
    about = models.CharField(max_length=10000)
    last_updated = models.DateTimeField(auto_now_add=True)
    
    def get_about(self):
        return self.about

# Music will hold songs
# music_player_url is the url to the bandcamp player
# bandcamp_url is the direct link to the bandcamp page the song resides
# song_title is the title of the song
# last_updated is when the song was last inserted/updated
class Music(models.Model):
    music_player_url = models.URLField(max_length=200, unique=True)
    bandcamp_url = models.URLField(max_length=200, unique=True)
    song_title = models.CharField(max_length=100, blank = True)
    last_update = models.DateTimeField(auto_now_add=True)

    def get_music_player_url(self):
        return self.music_player_url
