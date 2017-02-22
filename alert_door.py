# This workflow will monitor proximity to determine if the garage is open or closed and sends a push notification
import FCM
import Store
import MQTT

# set proximity threshold
threshold = 1000

# get last state from store
last_push = Store.get("garage_open_last_push")

# get proximity data
proximity=IONode.get_input('in1')['event_data']['value']

# get FCM token for push notification
FCM_token = IONode.get_input('in2')['event_data']['value']

if proximity > threshold:
    #print to display
    MQTT.publish_event_to_client('s3a7', 'D{};{}'.format(10, "Garage Door: CLOSED"), 'latin1')

    # send notification
    if last_push != "open":
        FCM.send_fcm_notification_to_m1_application([FCM_token],"Garage Door Closed", sound="chime")
        Store.set_data("garage_open_last_push","open")
else:
    MQTT.publish_event_to_client('s3a7', 'D{};{}'.format(10, "Garage Door: OPEN"), 'latin1')
    if last_push != "closed":
        FCM.send_fcm_notification_to_m1_application([FCM_token],"Garage Door Open", sound="chime")
        Store.set_data("garage_open_last_push","closed")