# import os
# import win32com.client as wincl
# import cv2
# import numpy as np
# import tensorflow as tf
# from object_detection.utils import label_map_util
# from object_detection.utils import visualization_utils as viz_utils
# from object_detection.builders import model_builder
# from object_detection.utils import config_util
#
# LABEL_MAP_NAME = 'label_map.pbtxt'
# CUSTOM_MODEL_NAME = 'my_ssd_mobnet'
# numckpt = 'ckpt-51'
#
# paths = {
#     'ANNOTATION_PATH': os.path.join('ObjectDetection/Tensorflow', 'workspace', 'annotations'),
#     'IMAGE_PATH': os.path.join('ObjectDetection/Tensorflow', 'workspace', 'images'),
#     'CHECKPOINT_PATH': os.path.join('ObjectDetection/Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME),
# }
#
# files = {
#     'PIPELINE_CONFIG': os.path.join('ObjectDetection/Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'pipeline.config'),
#     'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME)
# }
#
# category_index = label_map_util.create_category_index_from_labelmap(files['LABELMAP'])
#
# configs = config_util.get_configs_from_pipeline_file(files['PIPELINE_CONFIG'])
# detection_model = model_builder.build(model_config=configs['model'], is_training=False)
#
# # Restore checkpoint
# ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
# ckpt.restore(os.path.join(paths['CHECKPOINT_PATH'], numckpt)).expect_partial()
#
#
# @tf.function
# def detect_fn(image):
#     image, shapes = detection_model.preprocess(image)
#     prediction_dict = detection_model.predict(image, shapes)
#     detections = detection_model.postprocess(prediction_dict, shapes)
#     return detections
#
#
# def objectDetection(stop):
#     cap = cv2.VideoCapture(0)
#     speak = wincl.Dispatch("SAPI.SpVoice")
#     words = ""
#     print("in")
#     list = []
#     while True:
#         if stop:
#             ret, frame = cap.read()
#             image_np = np.array(frame)
#             listt = []
#             listt = list
#             list = []
#             input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
#             detections = detect_fn(input_tensor)
#             num_detections = int(detections.pop('num_detections'))
#             detections = {key: value[0, :num_detections].numpy()
#                           for key, value in detections.items()}
#             detections['num_detections'] = num_detections
#
#             # detection_classes should be ints.
#             detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
#
#             label_id_offset = 1
#             image_np_with_detections = image_np.copy()
#
#             viz_utils.visualize_boxes_and_labels_on_image_array(
#                 image_np_with_detections,
#                 detections['detection_boxes'],
#                 detections['detection_classes'] + label_id_offset,
#                 detections['detection_scores'],
#                 category_index,
#                 use_normalized_coordinates=True,
#                 max_boxes_to_draw=100,
#                 min_score_thresh=.5,
#                 agnostic_mode=False)
#             j = 0
#             if detections['detection_scores'][0] >= .5:
#                 list.insert(len(list), category_index[detections['detection_classes'][0] + 1]['name'])
#             print("Start")
#             list.sort()
#             listt.sort()
#             if listt != list:
#                 print(list)
#                 print("---------")
#                 speak.Speak(list)
#             cv2.imshow('object detection', cv2.resize(image_np_with_detections, (800, 600)))
#             cv2.waitKey(125)
#         else:
#             # ret, frame = cap.read()
#
#             # Display the clicked frame for 2
#             # sec.You can increase time in
#             # waitKey also
#             # cv2.imshow('a', frame)
#
#             # time for which image displayed
#             # cap.release()
#             cv2.destroyAllWindows()
#             break
#
# # objectDetection(stop=True)
#
