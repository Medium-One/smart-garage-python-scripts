# This workflow sends a push notification when the air quality exceeds a threshold
import FCM
import Store
import MQTT

# set air quality alert threshold
threshold = 900

# get last push state from data store
last_push = Store.get("garage_air_quality_last_push")

# get air quality data from input
air_quality=IONode.get_input('in1')['event_data']['value']

# get FCM token for push notification from input
FCM_token = IONode.get_input('in2')['event_data']['value']

if air_quality > threshold:
    # print to screen
    MQTT.publish_event_to_client('s3a7', 'D{};{}'.format(7, "Exhaust DETECTED"), 'latin1')
    # send notification
    if last_push != "high":
        FCM.send_fcm_notification_to_m1_application([FCM_token],"Exhaust DETECTED", sound="chime")

        # save to data store
        Store.set_data("garage_air_quality_last_push","high")
else:
    # print to screen
    MQTT.publish_event_to_client('s3a7', 'D{};{}'.format(7, "Exhaust NOT DETECTED"), 'latin1')

    # send notification

    if last_push != "low":
        FCM.send_fcm_notification_to_m1_application([FCM_token],"Air Quality back to normal", sound="chime")
        Store.set_data("garage_air_quality_last_push","low")