import os 
import unittest 
import json
# from unittest import result

from core import app
from models import db  

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DATABASE_URL'] = os.getenv('DATABASE_TEST_URL')
        self.app = app.test_client()
        db.create_all()

    def test_add_song(self):
        """ Test API can add a new song  """
        song_payload = {
            "title": "Hold on",
            "duration": 240
        }
        res = self.app.post('/song', headers={"Content-Type": "application/json"}, data=json.dumps(song_payload))
        self.assertEqual(res.status_code, 200)

    
    def test_get_song(self):
        """ Test API to retrieve a song """
        song_payload = {
            "title": "Hold on",
            "duration": 240
        }
        
        self.app.post('/song', headers={"Content-Type": "application/json"}, data=json.dumps(song_payload))

        response = self.app.get('/song/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hold on", str(response.data))

    def test_update_song(self):
        """ Test API to update a song """
        song_post_payload = {
            "title": "Hold on",
            "duration": 240
        }
        
        song__update_payload = {
            "title": "God's plan",
            "duration": 344
        }
        
        rev = self.app.post('/song', headers={"Content-Type": "application/json"}, data=json.dumps(song_post_payload))
        self.assertEqual(rev.status_code, 200)

        response= self.app.put('/song/1', headers={"Content-Type": "application/json"}, data=json.dumps(song__update_payload))
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("God", str(response.data))


    def test_delete_Song(self):
        """ Test API can delete an existing song """
        song_payload = {
            "title": "Love me",
            "duration": 330
        }

        res_post = self.app.post('/song', headers={"Content-Type": "application/json"}, data=json.dumps(song_payload))
        self.assertEqual(res_post.status_code, 200)
        
        response = self.app.delete('/song/1')
        self.assertEqual(response.status_code, 200)

        """ Check if the song deleted still exist"""
        result = self.app.get('/song/1')
        self.assertEqual(result.status_code, 404)
        

    def test_add_podcast(self):
        """ Test API to add a new podcast """
        podcast_payload = {
            "title": "TDD in Python",
            "duration": 333,
            "host": "Adeyemi",
            "participants": ["adeyemi", "john", "david", "kash", "mary", "Kate", "sam", "Ugo", "Oj", "grace", "extra"]
        }

        res = self.app.post('/podcast', headers={"Content-Type": "application/json"}, data=json.dumps(podcast_payload))
        self.assertEqual(res.status_code, 200)
        self.assertIn("TDD", str(res.data))
    
    def test_get_podcast(self):
        """Test API to retrieve a podcast"""
        podcast_payload = {
            "title": "TDD in Python",
            "duration": 333,
            "host": "Adeyemi",
            "participants": ["adeyemi", "john", "david", "kash", "mary", "Kate", "sam", "Ugo", "Oj", "grace"]
        }

        self.app.post('/podcast', headers={"Content-Type": "application/json"}, data=json.dumps(podcast_payload))

        res = self.app.get('/podcast/1')
        self.assertEqual(res.status_code, 200)
        self.assertIn("TDD", str(res.data))

    def test_get_all_podcast(self):
        """ Test API to add a new podcast """
        podcast_one_payload = {
            "title":"TDD in Python",
            "duration": 333,
            "host": "Adeyemi",
            "participants": ["adeyemi", "john", "david", "kash", "mary", "Kate", "sam", "Ugo", "Oj", "grace"]
        }

        podcast_two_payload = {
            "title":"Testing Your Python Applications",
            "duration": 3333,
            "host": "Joy",
            "participants": ["adeyemi", "mary", "Kate", "sam", "Ugo", "Oj", "grace"]
        }

        self.app.post('/podcast', headers={"Content-Type": "application/json"}, data=json.dumps(podcast_one_payload))
        self.app.post('/podcast', headers={"Content-Type": "application/json"}, data=json.dumps(podcast_two_payload))

        res = self.app.get('/podcast')
        self.assertEqual(res.status_code, 200)
        self.assertIn("david", str(res.data))
        self.assertIn("Joy", str(res.data))



    
    def test_update_podcast(self):
        podcast_post_payload = {
            "title": "TDD in Python",
            "duration": 333,
            "host": "Adeyemi",
            "participants": ["adeyemi", "john", "david", "kash", "mary", "Kate", "sam", "Ugo", "Oj", "grace"]
        }

        podcast_update_payload = {
            "title": "Testing Your Python Applications",
            "duration": 3333,
            "host": "Joy",
            "participants": ["adeyemi", "mary", "Kate", "sam", "Ugo", "Oj", "grace"]
        }

        rev = self.app.post('/podcast', headers={"Content-Type": "application/json"}, data=json.dumps(podcast_post_payload))
        self.assertEqual(rev.status_code, 200)

        res = self.app.put('/podcast/1', headers={"Content-Type": "application/json"}, data=json.dumps(podcast_update_payload))
        self.assertEqual(res.status_code, 200)
        self.assertIn("Joy", str(res.data))

    def test_delete_podcast(self):
        podcast_payload = {
            "title": "Testing Your Python Applications",
            "duration": 3333,
            "host": "Joy",
            "participants": ["adeyemi", "mary", "Kate", "sam", "Ugo", "Oj", "grace"]
        }

        rev = self.app.post('/podcast', headers={"Content-Type": "application/json"}, data=json.dumps(podcast_payload))
        self.assertEqual(rev.status_code, 200)

        res = self.app.delete('/podcast/1')
        self.assertEqual(res.status_code, 200)

        result = self.app.get('/podcast/1')
        self.assertEqual(result.status_code, 404)


    def test_add_audiobook(self):
        audiobook_payload = {
            "title": "The One Thing",
            "duration": 2333,
            "author": "Raymond Rolland",
            "narrator": "James Kent",
        }

        res = self.app.post('/audiobook', headers={"Content-Type": "application/json"}, data=json.dumps(audiobook_payload))
        self.assertEqual(res.status_code, 200)

    def test_get_audiobook(self):
        audiobook_payload = {
            "title": "The One Thing",
            "duration": 2333,
            "author": "Raymond Rolland",
            "narrator": "James Kent",
        }

        self.app.post('/audiobook', headers={"Content-Type": "application/json"}, data=json.dumps(audiobook_payload))

        res = self.app.get('/audiobook/1')
        self.assertEqual(res.status_code, 200)
        self.assertIn('James ', str(res.data))

    def test_get_all_audiobook(self):
        audiobook_one_payload = {
            "title": "The One Thing",
            "duration": 2333,
            "author": "Raymond Rolland",
            "narrator": "James Kent",
        }

        audiobook_two_payload = {
            "title": "Actions",
            "duration": 3333,
            "author": "John Taylor",
            "narrator": "Adeyemi Atoyegbe",
        }

        self.app.post('/audiobook', headers={"Content-Type": "application/json"}, data=json.dumps(audiobook_one_payload))
        self.app.post('/audiobook', headers={"Content-Type": "application/json"}, data=json.dumps(audiobook_two_payload))

        res = self.app.get('/audiobook')
        self.assertEqual(res.status_code, 200)
        self.assertIn("Adeyemi Atoyegbe", str(res.data))
        self.assertIn('Raymond Rolland', str(res.data))


    def test_update_audiobook(self):
        audiobook_payload = {
            "title": "The One Thing",
            "duration": 2333,
            "author": "Raymond Rolland",
            "narrator": "James Kent",
        }

        audiobook_update_payload = {
            "title": "Atomic Habit",
            "duration": 2333,
            "author": "James Clear",
            "narrator": "Kent james",
        }

        self.app.post('/audiobook', headers={"Content-Type": "application/json"}, data=json.dumps(audiobook_payload))

        res = self.app.put('/audiobook/1', headers={"Content-Type": "application/json"}, data=json.dumps(audiobook_update_payload))
        self.assertEqual(res.status_code, 200)
        self.assertIn('James Clear', str(res.data))

    def test_delete_audibook(self):
        audiobook_payload = {
            "title": "The One Thing",
            "duration": 2333,
            "author": "Raymond Rolland",
            "narrator": "James Kent",
        }

        self.app.post('/audiobook', headers={"Content-Type": "application/json"}, data=json.dumps(audiobook_payload))
        
        res = self.app.delete('/audiobook/1')
        self.assertEqual(res.status_code, 200)
        
        rev = self.app.get('/audiobook/1')
        self.assertEqual(rev.status_code, 404)
        
        
        

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    ###### Testing GET Method #########

    # def test_get_song(self):

   

    



if __name__ == "__main__":
    unittest.main()

