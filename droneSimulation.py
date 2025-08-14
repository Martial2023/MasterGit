from pysimverse import Drone

drone = Drone()

drone.connect()
drone.take_off()
drone.move_forward(1000)

# Obtenir le flux vidéo
video_stream = drone.get_frame()
