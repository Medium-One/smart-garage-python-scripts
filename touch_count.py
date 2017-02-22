import MQTT
import Store
# get last sample count from data store
sample_count = Store.get("sample_count")

# initialize to 0 if this is the first time
if sample_count == None:
    sample_count = 0

# save increment back to data store
sample_count = int(sample_count)+1
Store.set_data("sample_count",str(sample_count))

# print the count to screen at row 3
MQTT.publish_event_to_client('s3a7','D{};{}'.format(3, "Touch Count: "+str(sample_count)),'latin1')