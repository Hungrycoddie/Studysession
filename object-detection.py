from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )


    """_summary_
    Here's what the above code is doing:
1. We first import the ObjectDetection class from the ImageAI library.
2. We then create an instance of the ObjectDetection class and set the model type to RetinaNet.
3. We then set the model path to the path of the RetinaNet model file that we downloaded earlier.
4. We then load the model into the ObjectDetection class instance.
5. We then call the detectObjectsFromImage method, passing in the input image path and the output image path.
6. We then print the name of the object and the percentage probability that the object detected is the correct one.
    """
