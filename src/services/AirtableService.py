import requests

from ..Config import Config


class AirtableService:

  def __init__(self):
    self.config = Config()
    pass

  def GetRecords(self):
    url = "https://api.airtable.com/v0/{0}/{1}?view={2}".format(
      Config.base,
      Config.table,
      Config.view
    )

    response = requests.get(
      url,
      headers={'Authorization': "Bearer {0}".format(self.config.api_key)}
    )

    if (response.status_code != 200):
      raise Exception
    return response.json()


