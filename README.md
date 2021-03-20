# Description 
A Flask Web API that simulates the behavior of an audio file server. 


# Installation 
1. ``` git clone https://github.com/atoyegbe/filed_python_test.git ``` and change directory into the cloned folder.

2. Create and activate a virtual environment for the project.

3. Run ```pip install -r requirements.txt ```

4. set your environment variable :
    - `export FLASK_APP="run.py"`
    - `export SECRET="your-secret-key"`
    - `export DATABASE_URL="your-app-database-url"` for the main database.
    - `export DATABASE_TEST_URL="your-test-databse-url"` for the test database.

5. Run `flask run` to start the project.

> `python test_api.py` to run the test file.

# Audio File Types
- song
- podcast 
- audiobook


# Endpoints
| Methods | Url | Description |
| --- | --- | --- |
| GET | `/<AudioFileType>/<AudioFileID>` | Get a specific audio file. |
| GET | `/<AudioFileType>` | Get a list of all audio files. |
| POST | `/<AudioFileType>` | Create a new audio file. |
| PUT | `/<AudioFileType>/<AudioFileID>` | Update an exisiting audio file. |
| DELTE | `/<AudioFileType>/<AudioFileID>` | Delete an existing audio file. |

