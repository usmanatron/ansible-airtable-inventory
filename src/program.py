from .services.AirtableService import AirtableService

service = AirtableService()
print(service.GetRecords())
