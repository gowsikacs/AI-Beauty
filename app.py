import gradio as gr
import cv2
import numpy as np
from PIL import Image


def detect_acne(image):

    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    acne_pixels = np.sum(mask>0)

    if acne_pixels < 1000:
        return " Very Low Acne"
    elif acne_pixels < 5000:
        return "Low Acne"
    elif acne_pixels < 15000:
        return "Moderate Acne"
    elif acne_pixels < 20000:
        return "High Acne"
    else:
        return "Severe Acne"


def detect_wrinkles(image):

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    edges = cv2.Canny(gray,100,200)

    wrinkle_score = np.sum(edges)

    if wrinkle_score < 100000:
        return "Low Wrinkles"
    elif wrinkle_score < 500000:
        return "Moderate Wrinkles"
    elif wrinkle_score < 1000000:
        return "High wrinkles"
    else:
        return "No Wrinkles"


def detect_dark_circles(image):

    h, w, _ = image.shape

    eye_region = image[int(h*0.45):int(h*0.65), int(w*0.2):int(w*0.8)]

    gray = cv2.cvtColor(eye_region, cv2.COLOR_RGB2GRAY)

    brightness = np.mean(gray)

    if brightness < 150:
        return "Severe Dark Circles"
    elif brightness < 50:
        return "Moderate Dark Circles"
    else:
        return "Healthy Under-Eye"


def detect_hair_loss(image):

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    edges = cv2.Canny(gray,50,150)

    density = np.sum(edges)/(edges.shape[0]*edges.shape[1])

    if density < 5:
        return "High Hair Loss"
    elif density < 15:
        return "Moderate Hair Loss"
    else:
        return "Healthy Hair"


def beauty_analysis(image):

    img = np.array(image)

    acne = detect_acne(img)
    wrinkle = detect_wrinkles(img)
    dark = detect_dark_circles(img)
    hair = detect_hair_loss(img)

    result = f"""
AI BEAUTY PASSPORT REPORT

Acne Level: {acne}

Wrinkle Level: {wrinkle}

Dark Circles: {dark}

Hair Condition: {hair}
"""

    return result


interface = gr.Interface(
    fn=beauty_analysis,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="AI Beauty Passport System",
    description="Upload a face image for AI skin & hair analysis"
)

interface.launch()
    
       
   
