import motor.motor_asyncio
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb://facturas_user:isis2503@10.128.0.83:27017?retryWrites=true&w=majority"
)
db = client.get_database("facturas_db")
places_collection = db.get_collection("facturas")

async def set_places_db():
    # Creates a unique index on the code field
    await places_collection.create_index("code", unique=True)

# Represents an ObjectId field in the database.
PyObjectId = Annotated[str, BeforeValidator(str)]
