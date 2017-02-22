# This workflow will calculate a total movement by adding up all the max values from x,y,z axis on the accelerometer
# An alert is generated when the total movement is above a threshold
# and has been seen for at least 2 consecutive periods

import FCM
import Store
import MQTT

# set movement threshold
movement_threshold = 1.5

# get movement cycle count from Store library
cycle_count = Store.get("cycle_count")

if cycle_count == None:
    cycle_count = 0
cycle_count = int(cycle_count)+1

# get FCM token for push notification
FCM_token = IONode.get_input('in4')['event_data']['value']

# get last Push Notification state
last_push = Store.get("garage_movement_last_push")

# Add all the max values to get total movement
total_movement=abs(IONode.get_input('in1')['event_data']['value'])
+abs(IONode.get_input('in2')['event_data']['value'])
+abs(IONode.get_input('in3')['event_data']['value'])

# Send total movement to device
MQTT.publish_event_to_client('s3a7', 'D{};{}'.format(13, "Total Movement: "+str(total_movement)), 'latin1')
if total_movement > movement_threshold:
    # print to screen
    MQTT.publish_event_to_client('s3a7', 'D{};{}'.format(14, "Movement DETECTED"), 'latin1')
    MQTT.publish_event_to_client('s3a7', 'D{};{}'.format(15, " Cycles: "+str(cycle_count)), 'latin1')

    # condition to send push
    if last_push != "true" and cycle_count > 1:
        FCM.send_fcm_notification_to_m1_application([FCM_token],"Movement Detected", sound="chime")

        # save to data store
        Store.set_data("garage_movement_last_push","true")
else:
    cycle_count = 0
    # save to data store

    Store.set_data("garage_movement_last_push","false")
    MQTT.publish_event_to_client('s3a7', 'D{};{}'.format(14, "Movement NOT DETECTED"), 'latin1')
    MQTT.publish_event_to_client('s3a7', 'D{};{}'.format(15, ""), 'latin1')

# save cycle count back to store
Store.set_data("cycle_count",str(cycle_count))