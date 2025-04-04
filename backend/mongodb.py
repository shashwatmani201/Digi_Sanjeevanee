from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB Connection URI (Use your actual credentials)
MONGO_URI = "mongodb+srv://Utkarsh1234:Jaihind123456@fastapilearn.j7yqi.mongodb.net/?retryWrites=true&w=majority&appName=Fastapilearn&tls=true&tlsAllowInvalidCertificates=true"

# Database Name
DB_NAME = "DigiSanjeevani"

class Database:
    def __init__(self):
        self.client = None
        self.db = None
        self.users_collection = None
        self.appointments_collection = None
        self.medical_records_collection = None
        self.medicine_recommendations_collection = None
        self.medical_reports_collection = None  # ✅ Add this

    async def connect(self):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.db = self.client[DB_NAME]

        self.users_collection = self.db["users"]
        self.appointments_collection = self.db["appointments"]
        self.medical_records_collection = self.db["medical_records"]
        self.medicine_recommendations_collection = self.db["medicine_recommendations"]
        self.medical_reports_collection = self.db["medical_reports"]  # ✅ Add this too

        await self.users_collection.create_index("email", unique=True)

    async def close(self):
        self.client.close()

# Create a singleton database instance
database = Database()

users_collection = database.users_collection
appointments_collection = database.appointments_collection
medical_records_collection = database.medical_records_collection
medicine_recommendations_collection = database.medicine_recommendations_collection
medical_reports_collection = database.medical_reports_collection  # ✅ Use this