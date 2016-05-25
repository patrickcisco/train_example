#### CameraRecording.py will have methods for interacting with the /cameracamerarecording endpoint
import VSOM.client

def start_on_demand(token, device_reference):
  body = {
    "cameraRef": device_reference
  }
  client = VSOM.client.new("/camerarecording/startOnDemandRecording", body, token)
  return client.post_it()

def get_camera_recording_catalog_entries(token, filter):
  body = {
    "filter": filter
  }
  client = VSOM.client.new("/camerarecording/getRecordingCatalogEntries", body, token)
  return client.post_it()

def get_first_last_recording_catalog_entry(token, device_reference, id):
  body = {
    "cameraRef": device_reference,
    "recordingCatalogEntryId": id
  }
  client = VSOM.client.new("/camerarecording/getFirstLastForRecordingCatalogEntry", body, token)
  return client.post_it()

def get_thumbnails(token, camera_reference, id, start_time, end_time):
  body = {
    "request": {
      "cameraRef": camera_reference,
      "recordingCatalogEntryUid": id,
      "numThumbnails": 1,
      "startTimeInMSec": start_time,
      "endTimeInMSec": end_time,
      "forRecordings": False,
      "encoding": "JPG",
      "thumbnailResolution": "full",
      "thumbnailQuality": "high",
      "tokenExpiryInSecs": 300
    }
  }
  client = VSOM.client.new("/camerarecording/getThumbnails", body, token)
  return client.post()

def stop_on_demand(token, device_reference):
  body = {
    "cameraRef": device_reference
  }
  client = VSOM.client.new("/camerarecording/stopOnDemandRecording", body, token)
  return client.post_it()