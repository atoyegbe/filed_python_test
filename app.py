from flask import Flask, request, jsonify, abort 
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import os 



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


########################################
from models import Audiobook, Podcast, Song


class SongSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'duration')


class PodcastSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'duration', 'host', 'participants')



class AudibookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author' , 'narrator', 'duration')

song_schema = SongSchema()
songs_schema = SongSchema(many=True)

podcast_schema = PodcastSchema()
podcasts_schema = PodcastSchema(many=True)

audiobook_schema = AudibookSchema()
audiobooks_schema = AudibookSchema(many=True)


##################################################

@app.route('/<audioFileType>', methods= ['POST'])
def add_audio(audioFileType):
        title = request.json['title']
        duration = request.json['duration']

        if audioFileType == 'audiobook':
            author = request.json['author']
            narrator = request.json['narrator']
            new_audiobook = Audiobook(title, duration, author, narrator)
            new_audiobook.save()

            return audiobook_schema.jsonify(new_audiobook), 200
        elif audioFileType == 'podcast':
            host = request.json['host']
            participants = request.json['participants']

            new_podcast = Podcast(title, duration, host, participants)
            new_podcast.save()

            return podcast_schema.jsonify(new_podcast), 200
        elif audioFileType == 'song':
            new_song = Song(title, duration)
            new_song.save()

            return song_schema.jsonify(new_song), 200


@app.route('/<audioFileType>/<audioFileID>', methods=['GET'])
def get_audio(audioFileType, audioFileID):

    if audioFileType == 'song':
        get_song = Song.query.get(audioFileID)
        if not get_song:
            abort(404)
        result = song_schema.dumps(get_song)

        return jsonify(result)
    elif audioFileType == 'audiobook':
        get_audiobook = Audiobook.query.get(audioFileID)
        if not get_audiobook:
            abort(404)
        result = audiobook_schema.dumps(get_audiobook)

        return jsonify(result)
    elif audioFileType == 'podcast':
        get_podacst = Podcast.query.get(audioFileID)
        if not get_podacst:
            abort(404)
        result = podcast_schema.dumps(get_podacst)

        return jsonify(result)




@app.route('/<audioFileType>', methods=['GET'])
def get_all_audio(audioFileType):
    if audioFileType == 'song':
        all_songs = Song.query.all()
        result = songs_schema.dumps(all_songs)

        return jsonify(result), 200
    elif audioFileType == 'podcast':
        all_podcast = Podcast.query.all()
        result = podcasts_schema.dumps(all_podcast)

        return jsonify(result), 200
    elif audioFileType == 'audiobook':
        all_audiobook = Audiobook.query.all()
        result = audiobooks_schema.dumps(all_audiobook)

        return jsonify(result), 200



@app.route('/<audioFileType>/<audioFileID>', methods= ['PUT'])
def update_audio(audioFileType, audioFileID):
        title = request.json['title']
        duration = request.json['duration']
       
        if audioFileType == 'audiobook':
            author = request.json['author']
            narrator = request.json['narrator']

            audiobook = Audiobook.query.get(audioFileID)
            if not audiobook:
                abort(404)
            audiobook.title = title 
            audiobook.author = author
            audiobook.narrator = narrator
            audiobook.duration = duration 

            audiobook.save()

            return audiobook_schema.jsonify(audiobook), 200
        elif audioFileType == 'podcast':
            host = request.json['host']
            participants = request.json['participants']
            podcast = Podcast.query.get(audioFileID)

            if not podcast:
                abort(404)

            podcast.title = title 
            podcast.duration = duration 
            podcast.host = host 
            podcast.participants = participants

            podcast.save()

            return podcast_schema.jsonify(podcast), 200
        elif audioFileType == 'song':
            song = Song.query.get(audioFileID)
            if not song:
                abort(404)
            
            song.title = title 
            song.duration = duration
            song.save()

            return song_schema.jsonify(song), 200


@app.route('/<audioFileType>/<audioFileID>', methods= ['DELETE'])
def delete_audio(audioFileType, audioFileID):
    if audioFileType == 'song':
        song = Song.query.get(audioFileID)
        song.delete()
        return song_schema.jsonify(song), 200 

    elif audioFileType == 'podcast':
        podcast = Podcast.query.get(audioFileID)
        podcast.delete()

        return podcast_schema.jsonify(podcast), 200

    elif audioFileType == 'audiobook':
        audiobook = Audiobook.query.get(audioFileID)
        audiobook.delete()

        return audiobook_schema.jsonify(audiobook), 200 
    else:
        return {"message": f"{audioFileType} is not available." }
# Initailizing Schema 





# Run a server.

if __name__ == '__main__':
    app.run(debug=True)