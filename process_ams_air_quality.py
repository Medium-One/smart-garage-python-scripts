# This workflow converts the encoded air_quality data to human readable format
import MQTT
import cloud_driver_ams

# get input data from the connected trigger.  Note "in1"
buf = IONode.get_input('in1')['event_data']['value']

status = cloud_driver_ams.decode_ams_status(buf)
air_quality_value = cloud_driver_ams.decode_ams_air_quality(buf)
resistance = cloud_driver_ams.decode_ams_resistance(buf)

# generate output event
IONode.set_output('out1', {
        "air_quality": air_quality_value,
        "resistance": resistance,
        "status": status
    })

# print to display at row 5 & 6
MQTT.publish_event_to_client('s3a7', 'D{};{}'.format(5, "Air Quality: "+str(air_quality_value)+" ppm."), 'latin1')
MQTT.publish_event_to_client('s3a7', 'D{};{}'.format(6, " Status: "+str(status)), 'latin1')