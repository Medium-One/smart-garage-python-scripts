# This workflow sense registers commands to the board to request sensor data.  The exact register values
# are based on the sensor data sheet

import cloud_driver_ams

cloud_driver_ams.request_ams_proximity(3, 'proximity', 's3a7')
cloud_driver_ams.request_ams_air_quality(3, 'air_quality', 's3a7')