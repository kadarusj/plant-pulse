from google.appengine.ext import ndb

class Plant(ndb.Model):
  """Models an individual Plant entry with content and date."""
  pod_id = ndb.IntegerProperty()
  node_id = ndb.IntegerProperty()
  node_location = ndb.StringProperty()
  lux = ndb.IntegerProperty()
  broadband = ndb.IntegerProperty()
  infrared = ndb.IntegerProperty()
  air_temp = ndb.FloatProperty()
  humidity = ndb.FloatProperty()
  heat_index = ndb.FloatProperty()
  soil_temp = ndb.FloatProperty()
  soil_moist1 = ndb.IntegerProperty()
  soil_moist2 = ndb.IntegerProperty()
  plant_volt = ndb.FloatProperty()
  batt_volt = ndb.FloatProperty()
  timestamp = ndb.DateTimeProperty(auto_now_add=True)

  @classmethod
  def query_book(cls, ancestor_key):
    return cls.query(ancestor=ancestor_key).order(-cls.date)