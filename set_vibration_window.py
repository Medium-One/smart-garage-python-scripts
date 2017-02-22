# This workflow will send a message to the device to increase the vibration period to 10 seconds
import MQTT

# set to 10 seconds
aggregation_window = 10000
MQTT.publish_event_to_client('s3a7', 'Svibration_window{}'.format(aggregation_window), 'latin1')
MQTT.publish_event_to_client('s3a7', 'D{};{}'.format(12, "Vibration Freq: "+str(aggregation_window)+" ms"), 'latin1')