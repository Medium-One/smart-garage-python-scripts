import MQTT
# print message to screen using MQTT
MQTT.publish_event_to_client('s3a7', 'D{};{}'.format(1, "SMART GARAGE MONITORING"), 'latin1')