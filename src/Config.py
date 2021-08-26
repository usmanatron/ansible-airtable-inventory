from dotenv import load_dotenv
import os

load_dotenv()

class Config:
   
  api_key = os.environ.get('AAI_AIRTABLE_APIKEY')
  base = os.environ.get('AAI_AIRTABLE_BASEID')
  table = os.environ.get('AAI_AIRTABLE_TABLEID')
  view = os.environ.get('AAI_AIRTABLE_VIEWNAME')
