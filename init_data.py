from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from bson import ObjectId


class MongoDBManager:
    def __init__(self, uri, dbname):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]

    def insert_document(self, collection_name, document):
        collection = self.db[collection_name]
        result = collection.insert_one(document)
        print(f"Document inserted in '{collection_name}' with _id: {result.inserted_id}")


def main():
    # Connect to MongoDB and select the Alrazi_db database
    db_manager = MongoDBManager("mongodb://localhost:28017/", "QB_db")


    # Document for the settings_QasmiBank collection
    # document_settings_qasmibank = {
    #     'mongodb_url': 'mongodb://admin:nous_admin@195.26.253.58:27017/',
    #     'myDatabase': 'Alrazi_db',
    #     'prompt': "",
    #     'n_results': 2,
    #     'model_openai': 'gpt-3.5-turbo',
    #     'status': 'true'
    # }
    #
    # # Document for the settings collection
    # document_settings = {
    #     'default_openai_api_key': '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',
    #     'data_host': '',
    #     'data_port': 8000,
    #     'chroma_collection_name': 'alrazi',
    #     'mongodb_host': ''
    # }

    # Hash the password using werkzeug's generate_password_hash
    hashed_password = generate_password_hash("om")

    # Document for the users collection
    document_user = {
        "username": "om",
        "password": hashed_password,
        "status": 1,
        "Permissions": [
                    "Manage Documents",
                    "Train",
            "Settings",
                    "Delete Collection",
                    "Manage API Keys",
                    "Requests",
                    "Operation History",
                    "Message Report",
            "User Manager",
                    "Admin",
                    "My Requests Progress",
                ],
        "name": "Admin User",
        "user_type": "Admin"
    }
    key_api={
        "name": "om",
        "key": "001jhlk1jkjasdh1234h1kjhljhlk41hkj234hl1j"
    }

    # Insert the documents into the respective collections
    # db_manager.insert_document("settings_company", document_settings_qasmibank)
    # db_manager.insert_document("settings", document_settings)
    db_manager.insert_document("users", document_user)
    db_manager.insert_document("api_keys", key_api)


if __name__ == "__main__":
    main()
