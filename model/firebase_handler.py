import firebase_admin
from firebase_admin import credentials, storage, db
from uuid import uuid4
import os

class FirebaseHandler:
    storageBucket = 'fota-28ca6.appspot.com'
    databaseURL = 'https://fota-28ca6-default-rtdb.firebaseio.com/'
    def __init__(self) -> None:
        cred = credentials.Certificate("../firebase/resources/fota-28ca6-firebase-adminsdk-bg7vk-cfec2bcaec.json")
        firebase_admin.initialize_app(cred, {'storageBucket': self.storageBucket, 'databaseURL':self.databaseURL})
    
    def file_to_firebase(self, file_path, node_id):
        bucket = storage.bucket()
        blob = bucket.blob(os.path.basename(file_path))

        self.file_path = file_path
        self.node_id = node_id
        self.file_name = os.path.basename(self.file_path)
        
        # Create a token from UUID
        token = uuid4()
        metadata = {"firebaseStorageDownloadTokens": token}

        # Assign the token as metadata
        blob.metadata = metadata

        # Upload file to storage
        blob.upload_from_filename(filename=file_path)

        # Make the file public
        blob.make_public()

        #gcs_storageURL = blob.public_url

        #Generates a URL with Access Token from Firebase.
        self.firebase_storageURL = 'https://firebasestorage.googleapis.com/v0/b/{}/o/{}?alt=media&token={}'.format(self.storageBucket, self.file_name, token)

        # print({
        #     "gcs_storageURL": gcs_storageURL,
        #     "firebase_storageURL": self.firebase_storageURL
        # })

        self.update_db()
        pass

    def update_db(self):
        file_stats = os.stat(self.file_path)
        
        ref = db.reference("/")
        ref.set({"File_name": self.file_name,
                 "File_size": file_stats.st_size,
                 "NewUpdate": 0,
                 "Node_ID": self.node_id,
                 "url": self.firebase_storageURL
                 }) 
