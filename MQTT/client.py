import paho.mqtt.client

def new(host, port, keep_alive):
  client = paho.mqtt.client()
  client.subscribe("devnet/2")
  client.connect(host, port, keep_alive)
  client.on_message = on_message

def on_message(client, userdata, message):
  if message.topic == "devnet/2":
    content = json.loads(json_string)
    if content["trig"] != "none":
      __parse_content["trig"]

def __parse_content(content):
  if   content == "dist-1":
  elif content == "dist-2":
  elif content == "light":
  else:
   return

          content = JSON.parse(message)
          #puts JSON.pretty_generate(content)
          #if content["trig"] = "dist-2"
          if content["trig"] != "none"
            case content["trig"]
              when trig1.name
                #puts trig1.name
              #  trig1.execute
              when trig2.name
              #  puts trig2.name
             #   trig2.execute
              when trig3.name
                #puts trig3.name
                trig3.execute
                sleep(44)
               # trig1.execute
                #sleep(10)
                #trig2.execute
               # sleep(225)
              #  trig3.execute
                #trig3.execute
            end
          end


    #print("Received message '" + str(message.payload) + "' on topic '"
    #    + message.topic + "' with QoS " + str(message.qos))

mqttc.on_message = on_message

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Connect
mqttc.connect("localhost", 1883,60)


# Continue the network loop
mqttc.loop_forever()