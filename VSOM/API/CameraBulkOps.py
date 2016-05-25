#### CameraBulkOps.py will have methods for interacting with the /camerabulkops endpoint
import VSOM.client

def associate_cameras_to_device_template(token, device_references, template_reference):
  body = {
    "deviceRefs": device_references,
    "templateRef": template_reference
  }
  client = VSOM.client.new("/camerabulkops/associateCamerasToDeviceTemplate", body, token)
  return client.post_it()

def create_full_motion_windows(token, device_references):
  body = {
    "deviceRefs": device_references
  }
  client = VSOM.client.new("/camerabulkops/createFullMotionWindows", body, token)
  return client.post_it()