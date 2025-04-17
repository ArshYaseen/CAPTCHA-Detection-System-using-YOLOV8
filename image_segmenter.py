import numpy as np
from PIL import Image

def segment_image(image):
   
    img_array = np.array(image)
    
    height, width, _ = img_array.shape
    
    block_height = height // 3
    block_width = width // 3
    
    blocks = {}
    
    for i in range(3):
        for j in range(3):
            block = img_array[i*block_height:(i+1)*block_height, j*block_width:(j+1)*block_width]
            blocks[f"Block_{i+1}_{j+1}"] = block
            
            block_image = Image.fromarray(block)
            block_image.save(f"block_{i+1}_{j+1}.jpeg")
            
    return blocks
