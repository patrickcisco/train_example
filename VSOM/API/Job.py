#### Job.py will have methods for interacting with the /job endpoint
import VSOM.client

def get_status(token, job_reference):
  body   = { "jobRef": job_reference }
  client = VSOM.client.new("/job/getJobStatus", body, token)
  return client.post_it()