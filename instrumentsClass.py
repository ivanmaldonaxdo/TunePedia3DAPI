class MusicalInstResp:
    def __init__(self, **kwargs):
        self.artist = kwargs.get('Artist')
        self.description = kwargs.get('Description')
        self.glbModel = kwargs.get('GlbModel')
        self.image = kwargs.get('Image')
        self.name = kwargs.get('Name')
        self.demo = kwargs.get('Demo')
        self.artist =  kwargs.get('ArtistList')

def addArtistList(instrument,db):
    artistasList = []
    artistas = db.execute("select * from v_artist_instruments WHERE instrumento = ? ",instrument["Name"])
    if len(artistas ) > 0:
        artistasList = list(map(lambda art: art["artista"], artistas))
    instrument['ArtistList'] = artistasList
    return MusicalInstResp(**instrument)