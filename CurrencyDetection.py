import os
import cv2
import numpy as np
import tensorflow as tf
import win32com.client as wincl
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder
from object_detection.utils import config_util
import time

from Detection import Detect
from imageCam import ImageCam


class CurrencyDetection:
    LABEL_MAP_NAME = 'label_map.pbtxt'
    CUSTOM_MODEL_NAME = 'my_ssd_mobnet'
    numckpt='ckpt-101'


    paths = {
        'ANNOTATION_PATH': os.path.join('Egyptian Currency/Tensorflow', 'workspace', 'annotations'),
        'IMAGE_PATH': os.path.join('Egyptian Currency/Tensorflow', 'workspace', 'images'),
        'CHECKPOINT_PATH': os.path.join('Egyptian Currency/Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME)
    }

    files = {
        'PIPELINE_CONFIG': os.path.join('Egyptian Currency/Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME, 'pipeline.config'),
        'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME)
    }
    imageCam= ImageCam()

    category_index = label_map_util.create_category_index_from_labelmap(files['LABELMAP'])

    configs = config_util.get_configs_from_pipeline_file(files['PIPELINE_CONFIG'])
    detection_model = model_builder.build(model_config=configs['model'], is_training=False)

    # Restore checkpoint
    ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
    ckpt.restore(os.path.join(paths['CHECKPOINT_PATH'], numckpt)).expect_partial()



    def detect_fn(self,image):
        image, shapes = self.detection_model.preprocess(image)
        prediction_dict = self.detection_model.predict(image, shapes)
        detections = self.detection_model.postprocess(prediction_dict, shapes)
        return detections

    def sum (sum , num) :
        return sum + num

    def currncydetection(self):
        IMAGE_PATH = self.imageCam.imagePath
        img = cv2.imread(IMAGE_PATH,cv2.IMREAD_UNCHANGED)
        image_np = np.array(img)

        input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
        # detections = self.detect.detect_fn(input_tensor, self.detection_model)
        detections = self.detect_fn(input_tensor)

        num_detections = int(detections.pop('num_detections'))
        detections = {key: value[0, :num_detections].numpy()
                      for key, value in detections.items()}

        detections['num_detections'] = num_detections
        # detection_classes should be ints.
        detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

        label_id_offset = 1
        image_np_with_detections = image_np.copy()
        viz_utils.visualize_boxes_and_labels_on_image_array(
            image_np_with_detections,
            detections['detection_boxes'],
            detections['detection_classes'] + label_id_offset,
            detections['detection_scores'],
            self.category_index,
            use_normalized_coordinates=True,
            max_boxes_to_draw=100,
            min_score_thresh=.7,
            agnostic_mode=False)

        speak = wincl.Dispatch("SAPI.SpVoice")
        j = 0
        s = 0
        count=0
        for i in detections['detection_scores']:
            if i >= 0.8:
                count+=1
                txt = str(self.category_index[detections['detection_classes'][j] + 1]['name'])[:-3]
                speak.Speak(txt + " bound")
                print(txt + " bound", "       ", detections['detection_scores'][j])
                s = sum(s, int(txt))
            else:
                break
            j += 1
        print(s)
        if count > 1:
            speak.Speak("the sum is "+ str(s) + " bound")
        cv2.imshow('Curruncy', cv2.resize(image_np_with_detections, (800, 600)))
        cv2.waitKey(10000)
        cv2.destroyAllWindows()
