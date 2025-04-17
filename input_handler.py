from PIL import Image, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt

def load_and_enhance_image(image_path):
    
    image = Image.open(image_path)
    
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(2.0)  
    
    image = image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    
    plt.imshow(image)
    plt.axis('off')  
    plt.show()
    
    return image
