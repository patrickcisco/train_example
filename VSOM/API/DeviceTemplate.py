#### DeviceTemplate.py will have methods for interacting with the /devicetemplate endpoint

import VSOM.client

def get_by_name(token, name):
  body = {
    "filter": {
      "byExactName": name
    }
  }
  client = VSOM.client.new("/devicetemplate/getDeviceTemplates", body, token)
  return client.post_it()
  

def create_default_template(token, name, description, vsom_uid, location_ref):
  body = {
    "template":{
      "systemDefined": False,
      "shared": True,
      "generic": True,
      "numAssocDevices": 0,  
      "ownerLocationRef": location_ref,
      "videoStreams": [{
        "streamNum": 1,
        "viewable": True,
        "motion_configured": True,
        "recordable": True,
        "videoStreamProfile": {
          "videoQuality": "medium",
          "format": "NTSC",
          "ltsRetentionDays": 0,
          "suspendableProxy": False
        }
      }],
      "recordings": [{
        "recordingType": "LOOP",
        "streamNum": 1,
        "duration": 86400,
        "expireTime": 1,
        "eventExpireTime": 30,
        "storageEstimation": True,
        "startImmediate": True,
        "recordIframe": False,
        "archiveToLTS": False,
        "ltsRetentionTime": 0,
        "zeroVideoLossEnabled": False
      }],
      "participateInFailover": False,
      "preBuffer": 0,
      "postBuffer": 0,
      "lastModified": 0,
      "enableRecordNow": True,
      "mergeRecordings": False,
      "name": name,
      "tags": "tags",
      "description": description,
      "vsomUid": vsom_uid,
      "objectType": "vs_deviceTemplate"
    }
  }
  client = VSOM.client.new("/devicetemplate/createDeviceTemplate", body, token)
  return client.post_it()