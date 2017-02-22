# This workflow converts the encoded proximity data to human readable format
import MQTT
import cloud_driver_ams

proximity = cloud_driver_ams.decode_ams_proximity(IONode.get_input('in1')['event_data']['value'])

# generate output event
IONode.set_output('out1', {'proximity': proximity})

# print to display
MQTT.publish_event_to_client('s3a7', 'D{};{}'.format(9, "Proximity: "+str(proximity)), 'latin1')