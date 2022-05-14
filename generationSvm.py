import dlib

option = dlib.simple_object_detector_training_options()
option.add_left_right_image_flips = True
option.C = 5

dlib.train_simple_object_detector("files/buttonBackApp.xml", "files/butonBackApp.svm", option)

print('Finalizou a geração SVM')