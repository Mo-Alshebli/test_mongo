from pymongo import MongoClient
from pymongo.errors import OperationFailure


class MongoDBManager:
    def __init__(self, uri, dbname):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]
        # self.client.drop_database(dbname)

    def list_collections(self):
        return self.db.list_collection_names()

    def create_collection(self, collection_name):
        if collection_name not in self.db.list_collection_names():
            self.db.create_collection(collection_name)
            print(f"Created new collection: {collection_name}")
        else:
            print(f"Collection '{collection_name}' already exists.")
        return self.db[collection_name]

    def get_collection(self, collection_name):

        return self.db[collection_name]

    def delete_all_documents(self, collection_name):
        collection = self.get_collection(collection_name)
        result = collection.delete_many({})
        print(f"All documents deleted from {collection_name}: {result.deleted_count}")

    def insert_document(self, collection_name, document):
        collection = self.get_collection(collection_name)
        result = collection.insert_one(document)
        print(f"One document inserted in {collection_name}: {result.inserted_id}")

    def add_field_to_collection(self, collection_name, field_name, field_value):
        collection = self.get_collection(collection_name)
        query = {field_name: {"$exists": False}}  # Find documents where the field doesn't exist
        update = {"$set": {field_name: field_value}}  # Set the new field with the specified value
        result = collection.update_many(query, update)
        print(f"Updated documents in {collection_name}: {result.modified_count}")

    def read_documents(self, collection_name, query={}):
        collection = self.get_collection(collection_name)
        documents = collection.find(query)
        return list(documents)  # Convert cursor to list

    def update_documents(self, collection_name, query, new_values):
        collection = self.get_collection(collection_name)
        result = collection.update_many(query, {'$set': new_values})
        print(f"Documents updated in {collection_name}: {result.modified_count}")

    def delete_documents(self, collection_name, query):
        collection = self.get_collection(collection_name)
        result = collection.delete_many(query)
        print(f"Documents deleted from {collection_name}: {result.deleted_count}")



def main():

    db_manager = MongoDBManager("mongodb://:28017/", "Alrazi_db")



    # List all collections

    # List all collections
    print("Available collections:")
    collections = db_manager.list_collections()
    print(collections)


    # # # Create a collection
    # collection_name = 'settings_QasmiBank'
    # db_manager.create_collection(collection_name)
    # #
    # mongodb_url = doc.get("mongodb_url")
    # myDatabase = doc.get("myDatabase")
    # prompt = doc.get("prompt")
    # n_results = doc.get("n_results")
    # model_openai = doc.get("model_openai")
    # status = doc.get("status")
    # # # Inserting a document
    # document =  {"mongodb_url": "mongodb://admin:nous_admin@195.26.253.58:27017/","myDatabase": "myDatabase","prompt": "Enter your prompt here","n_results": 2,"model_openai": "gpt-3.5-turbo","status": "true"}
    # db_manager.insert_document("settings_QasmiBank", document)
    # db_manager.insert_document("requests", {'text': ''})
    # db_manager.add_field_to_collection("requests", "text", "")
    # Reading documents
    # print("Reading documents:")

    # "أنت روبوت دردشة خاص ببنك القاسمي في اليمن. مهمتك هي الإجابة على استفسارات العملاء بخصوص البنك بشكل مفصل ودقيق.      الدقة والموثوقية: يجب عليك عدم تقديم معلومات خاطئة أو مفترضة تحت أي ظرف. في حال عدم توفر معلومات إضافية موثوقة (None)، يجب أن تقدم إجابة توضح عدم توفر المعلومات الكافية للرد الدقيق. أخبر العملاء بأنه لا تتوفر معلومات كافية لتقديم إجابة محددة وأنصحهم بالتحقق من مصادر أخرى أو الاستفسار من الجهات المعنية داخل البنك.      التحقق من الدقة: يجب عليك التأكد من صحة الأسماء والمناصب بناءً على المعلومات المؤكدة فقط. لا تقم بتقديم أي تفاصيل مرتبطة بأشخاص أو مناصب إلا إذا كانت مدعومة بمعلومات موثوقة ومؤكدة.      التركيز على الاستفسار: يجب أن تركز في الإجابة على حدود السؤال المقدم فقط، دون التوسع في تفاصيل خارج نطاق السؤال المحدد.      التفاعل الودي: عند الإجابة، يجب أن تدعم ردودك بالإيموجي المناسب لجعل التفاعل أكثر ودية.      الاتساق والمساعدة في صياغة الاستفسارات: يجب أن تساعد العملاء في صياغة استفساراتهم بشكل أكثر دقة . تأكد من الاتساق في الردود بالرجوع إلى الأسئلة السابقة المطروحة.
    # Updating document{'_id': ObjectId('66d4a1b1a2673e485bdf24af'), 'chroma_collection_name': 'alrazi', 'data_host': 'host.docker.internal:9890', 'data_port': 8000, 'db_name': 'Alrazi_db', 'default_openai_api_key': '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', 'mongodb_host': 'host.docker.internal:27017/'}
    # db_manager.update_documents("settings", {'db_name': 'Alrazi_db'}, {'data_host': 'localhost:9890','mongodb_host': 'localhost:27017/'})
    # db_manager.delete_documents("users", {'username': '',})
    # db_manager.delete_documents("requests", {'text': '',})
    # db_manager.delete_all_documents("operations")

    for i in collections:
        print(f"//////////{i}//////////")
        documents = db_manager.read_documents(i)
        for doc in documents:
            print(doc)
        print("////////////////////")
    # Deleting document


if __name__ =="__main__":
    main()


# {'_id': ObjectId('66b6b898b98f243445f33fc6'), 'operation': 'train', 'file_path': 'uploads/5ccd15ca-9cf8-4025-8a47-63bde7d91846_Q_A.txt', 'file_name': 'uploads//5ccd15ca-9cf8-4025-8a47-63bde7d91846_Q_A.txt', 'username': 'mo', 'status': 'approved', 'created_at': datetime.datetime(2024, 8, 10, 3, 47, 20, 499000), 'rejection_reason': '', 'approved_by': 'mo', 'completed_at': datetime.datetime(2024, 8, 10, 3, 47, 54, 218000)}
# {'_id': ObjectId('66d239e2a38150a5d0168041'), 'operation': 'train', 'file_path': 'uploads\\mo_2024-08-31 00-30-10', 'file_name': 'uploads//mo_2024-08-31 00-30-10', 'username': 'mo', 'status': 'approved', 'created_at': datetime.datetime(2024, 8, 31, 0, 30, 10, 321000), 'rejection_reason': '', 'approved_by': 'mo', 'completed_at': datetime.datetime(2024, 8, 31, 0, 30, 15, 480000)}

# {'_id': ObjectId('66b6b8a1b98f243445f33fcb'), 'operation': 'update', 'text': 'fgdf', 'username': 'mo', 'file_path': '', 'file_name': '', 'status': 'approved', 'created_at': datetime.datetime(2024, 8, 10, 3, 47, 29, 381000), 'rejection_reason': '', 'approved_by': 'mo', 'completed_at': datetime.datetime(2024, 8, 10, 3, 49, 34, 872000)}

# {'_id