import json
import requests
import time
import VSOM.API.Authentication  as Authentication
import VSOM.API.Camera          as Camera
import VSOM.API.Location        as Location
import VSOM.API.CameraRecording as CameraRecording
import VSOM.API.CameraBulkOps   as CameraBulkOps
import VSOM.API.Job             as Job
import VSOM.API.DeviceTemplate  as DeviceTemplate

import Spark.API.Messages       as Messages
import Tropo.API.Session        as Session

import paho.mqtt.client

import Spark.client
import Tropo.client

def pretty_print(data):
  print (json.dumps(data, indent=4, separators=(',', ': ')))

def vsom_token():
  res = Authentication.login("admin", "Password1")
  return res["data"]["uid"]

def create_template(token):
  tree_root = Location.get_tree_root(token)
  vsom_uid  = tree_root["data"]["vsomUid"]
  name      = "Patrick's Template"
  desc      = "This is an example template"
  location  = {
    "refUid":         tree_root["data"]["childGroups"][0]["uid"],
    "refName":        tree_root["data"]["childGroups"][0]["name"],
    "refObjectType":  tree_root["data"]["childGroups"][0]["objectType"],
    "refVsomUid":     tree_root["data"]["childGroups"][0]["vsomUid"]
  }
  return DeviceTemplate.create_default_template(token, name, desc, vsom_uid, location)

def get_job(token, job_reference, timer):
  result = Job.get_status(token, job_reference)
  if result["status"]["errorType"] == "SUCCESS":
    if ( result["data"]["numberOfRunningSubJobs"] != 0 or
         result["data"]["numberOfPendingSubJobs"] != 0):
      print("still running...")
      pretty_print(result)
      time.sleep(timer)
      get_job(token, job_reference, timer*2)
  return result

def get_device_reference(device):
  device_reference = {
    "refUid":        device["data"]["items"][0]["alternateId"],
    "refName":       device["data"]["items"][0]["name"],
    "refObjectType": device["data"]["items"][0]["objectType"],
    "refVsomUid":    device["data"]["items"][0]["vsomUid"]
  }
  return device_reference

def apply_template(token):
  device             = Camera.get_by_name(token, "CIVS-IPC-2830-01")
  template           = DeviceTemplate.get_by_name(token, "Patrick's Template")
  device_reference   = get_device_reference(device)
  template_reference = {
    "refUid":        template["data"]["items"][0]["uid"],
    "refName":       template["data"]["items"][0]["name"],
    "refObjectType": template["data"]["items"][0]["objectType"],
    "refVsomUid":    template["data"]["items"][0]["vsomUid"]
  }
  res = CameraBulkOps.associate_cameras_to_device_template(token, [device_reference], template_reference)
  return get_job(token, res["data"], 5)

def configure_motion_window(token):
  device           = Camera.get_by_name(token, "CIVS-IPC-2830-01")
  device_reference = get_device_reference(device)
  res              = CameraBulkOps.create_full_motion_windows(token, [device_reference])
  return get_job(token, res["data"], 5)

def start_recording(token):
  device           = Camera.get_by_name(token, "CIVS-IPC-2830-01")
  device_reference = get_device_reference(device)
  res              = CameraRecording.start_on_demand(token, device_reference)
  return res

def get_snapshot(token):
  device           = Camera.get_by_name(token, "CIVS-IPC-6400E-01")
  device_reference = get_device_reference(device)
  filter = {
    "byCameraAlternateId": device["data"]["items"][0]["alternateId"] 
  }
  res = CameraRecording.get_camera_recording_catalog_entries(token, filter)
  id  = res["data"]["items"][0]["uid"]
  res = CameraRecording.get_first_last_recording_catalog_entry(token, device_reference, id)
  id  = res["data"]["uid"]
  current_time = int(time.time())
  last_frame   = res["data"]["lastFrame"]
  start_frame  = last_frame - 1000
  res          = CameraRecording.get_thumbnails(token, device_reference, id, start_frame, last_frame)
  return res

def stop_recording(token):
  device           = Camera.get_by_name(token, "CIVS-IPC-2830-01")
  device_reference = get_device_reference(device)
  res              = CameraRecording.stop_on_demand(token, device_reference)
  return res

def mqtt_client(host, port, keep_alive):
  client = paho.mqtt.client.Client()
  client.subscribe("devnet/2")
  client.on_message = on_message
  client.connect(host, port, keep_alive)
  return client

def on_message(client, userdata, message):
  if message.topic == "devnet/2":
    content = json.loads(json_string)
    if content["trig"] != "none":
      parse_content(content["trig"])

def parse_content(content):
  if   content == "dist-1":
    # ---> start recording
    # start_recording(vsom_token())
  elif content == "light":
    # ---> take snapshot
    # spark_token = "YWE5NTc0ZGItMjljMy00YWFmLThiY2YtNTE5ZjYxNDhmZmUwZGIwMzg3ZDctNDA3"
    # token = vsom_token()
    # res   = get_snapshot(token)
    # files = {'upload_file': res.content}
    # r     = requests.post("http://173.36.206.19/images/tmp", files=files)
    # json  = r.json()
    # url   = "http://173.36.206.19" + json["uri"]
    # res   = Messages.send(spark_token, "Testing", [url], None, None, "priel@cisco.com" )
    # pretty_print(res)
  elif content == "dist-2":
    # ---> stop recording
    # res   = stop_recording(vsom_token())
    # prett_print(res)
  else:
    return


def vsom_run():
 # spark_token = "YWE5NTc0ZGItMjljMy00YWFmLThiY2YtNTE5ZjYxNDhmZmUwZGIwMzg3ZDctNDA3"
 # token = vsom_token()
 # res   = get_snapshot(token)
 # files = {'upload_file': res.content}
 # r     = requests.post("http://173.36.206.19/images/tmp", files=files)
 # json  = r.json()
 # url   = "http://173.36.206.19" + json["uri"]
 # res = Messages.send(spark_token, "Testing", [url], None, None, "priel@cisco.com" )
 # pretty_print(res)

  client = mqtt_client('173.36.206.30', 7777, 10000)
  client.loop_forever()

vsom_run()