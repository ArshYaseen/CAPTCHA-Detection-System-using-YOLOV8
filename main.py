from input_handler import load_and_enhance_image
from image_segmenter import segment_image
from image_classifier import load_yolov8_model, classify_blocks
from object_identifier import identify_object

def main(image_path, target_object):
    enhanced_image = load_and_enhance_image(image_path)
    
    segmented_blocks = segment_image(enhanced_image)
    
    model = load_yolov8_model()
    
    classifications = classify_blocks(segmented_blocks, model)
    
    identify_object(classifications, target_object)

if __name__ == "__main__":
    image_path = 'images/3.jpg'  
    target_object = 'bicycle'  
    main(image_path, target_object)
