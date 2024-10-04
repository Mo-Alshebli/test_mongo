from pymongo import MongoClient


class MongoDBManager:
    def __init__(self, uri, dbname):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]

    def create_collection_with_keys(self, collection_name, keys):
        collection = self.db[collection_name]
        # Create a dummy document with all the specified keys
        dummy_document = {key: "" for key in keys}
        result = collection.insert_one(dummy_document)
        print(f"Created collection '{collection_name}' with keys: {keys}")
        # Optionally remove the dummy document after creation
        collection.delete_one({"_id": result.inserted_id})


def main():
    # Connect to MongoDB and select the Alrazi_db database
    db_manager = MongoDBManager("mongodb://localhost:28017/", "QB_db")


    # JSON structure with collections and keys
    collections_info = {
        "collections": [
            {
                "name": "requests",
                "keys": [
                    "approved_by", "username", "file_name", "created_at", "doc_id",
                    "rejection_reason", "operation", "file_path", "status",
                    "completed_at", "text"
                ]
            },
            {
                "name": "Masseges",
                "keys": []
            },
            {
                "name": "api_keys",
                "keys": ["name", "key"]
            },
            {
                "name": "settings_company",
                "keys": ["prompt", "mongodb_url", "model_openai", "status", "myDatabase", "n_results"]
            },
            {
                "name": "MessageLogs",
                "keys": [
                    "history", "error_message", "client_ip", "timestamp", "name_platform",
                    "status", "datetime", "text", "response"
                ]
            },
            {
                "name": "users",
                "keys": ["username", "password", "status", "Permissions", "name", "user_type"]
            },
            {
                "name": "settings",
                "keys": [
                    "chroma_collection_name", "data_port", "mongodb_host",
                    "data_host", "default_openai_api_key"
                ]
            },
            {
                "name": "operations",
                "keys": [
                    "approved_by", "username", "file_name", "created_at", "doc_id",
                    "rejection_reason", "operation", "status", "completed_at", "text"
                ]
            }
        ]
    }

    # Create each collection with the specified keys
    for collection in collections_info["collections"]:
        db_manager.create_collection_with_keys(collection["name"], collection["keys"])


if __name__ == "__main__":
    main()
