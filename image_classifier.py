from ultralytics import YOLO
from PIL import Image
import numpy as np
import torch

def load_yolov8_model():
    
    model = YOLO('yolov8l.pt')  
    return model

def classify_blocks(blocks, model, conf_threshold=0.1):
    
    classifications = {}

    for block_name, block in blocks.items():
        block_image = Image.fromarray(block)
        
        block_image = block_image.resize((640, 640))

        results = model(block_image)

        print(f"Raw predictions for {block_name}:")
        print(results)

        predictions = []

        if hasattr(results, 'boxes') and len(results.boxes) > 0:
            for result in results.boxes:
                confidence = result[4]  
                if confidence >= conf_threshold:
                    class_id = int(result[5]) 
                    predictions.append({
                        'class': model.names[class_id],  
                        'confidence': confidence,
                        'bbox': result[:4]  
                    })

        if predictions:
            best_prediction = max(predictions, key=lambda x: x['confidence'])
            classifications[block_name] = best_prediction
            print(f"{block_name}: {best_prediction['class']} with confidence {best_prediction['confidence']:.2f}")
        else:
            classifications[block_name] = {"class": "No object detected", "confidence": 0.0}
            print(f"{block_name}: No object detected")
    
    return classifications