import dlib

option = dlib.simple_object_detector_training_options()
option.add_left_right_image_flips = True
option.C = 5

dlib.train_simple_object_detector("files/closeButtons.xml", "files/closeButtons.svm", option)

print('Finalizou a geração SVM')