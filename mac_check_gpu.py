import tensorflow as tf
devices = tf.config.list_physical_devices()
print("\n Devices: ", devices)

gpus = tf.config.list_physical_devices('GPU')
if gpus:
    detail = tf.config.experimental.get_device_details(gpus[0])
    print("GPU details:", detail)
"""
 Devices:  [PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU'),
   PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
   GPU details: {'device_name': 'METAL'}
"""