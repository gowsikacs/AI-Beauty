import streamlit as st
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

def detect_skin_type(image):
    gray = cv2.cvtColor(face, cv2.COLOR_RGB2GRAY)

    brightness = np.mean(gray)

    if brightness < 80:
        result = "Dry / Dull Skin"
    elif brightness < 150:
        result = "Normal Skin"
    else:
        result = "Oily / Shiny Skin"

    return brightness, result
        
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




def beauty_recommendation(detect_acne, detect_wrinkles, detect_dark_circles, detect_hair_loss, detect_skin_type):

    recommendations = []

    if "Moderate" in acne or "Severe" in acne:
        recommendations.append("Use Salicylic Acid Cleanser")
        recommendations.append("Acne Treatment Facial")

    if "Moderate" in wrinkle or "High" in wrinkle:
        recommendations.append("Use Retinol Cream")
        recommendations.append("Anti-aging Facial")

    if "Dark" in dark_circle:
        recommendations.append("Vitamin C Eye Cream")
        recommendations.append("Improve Sleep Schedule")

    if "Hair Loss" in hair:
        recommendations.append("Use Biotin Shampoo")
        recommendations.append("Hair Growth Serum")
        recommendations.append("Scalp Therapy")

    if "Dry" in skin_type or "Dull" in skin_type:
        recommendations.append("Use gentle and thick moisturizers")
        recommendations.append("Use Hydrating Cleanser")
        recommendations.append("Avoid Hot Showers")

    if "Oily" in skin_type or "Shiny" in skin_type:
        recommendations.append("Use Matte-finish sunscreen")
        recommendations.append("Use Niacinamide Serum")
        recommendations.append("Using Gel-based cleanser contain Salicylic Acid")

    return recommendations


rec = beauty_recommendation(acne, wrinkle, dark_circle, hair,skin_type)

print("------ Personalized Beauty Plan ------")

for r in rec:
    print("-", r)
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

Skin Type: {skin_type}

personalized recommendation: {beauty_recommendations}
"""

    return result



import streamlit as st
from PIL import Image

# Title and description
st.title("AI Beauty Passport System")
st.write("Upload a face image for AI skin & hair analysis")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open image
    image = Image.open(uploaded_file)

    # Show image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Run your model function
    result = beauty_analysis(image)
    rec = beauty_recommendation(**result)

st.write("### Recommendations")
for r in rec:
    st.write("-", r)

    # Display output
    st.subheader("Analysis Result")
    st.write(result)
