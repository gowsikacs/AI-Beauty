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

    if brightness < 2000:
        return "Severe Dark Circles"
    elif brightness < 150:
        return "High Dark Circles"
    elif brightness < 100:
        return "Moderate Dark Circles"
    elif brightness < 50:
        return "Low Dark Circles"
    else:
        return "Healthy Under-Eye"

def detect_skin_type(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

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


def beauty_analysis(image):

    img = np.array(image)

    acne = detect_acne(img)
    wrinkle = detect_wrinkles(img)
    dark = detect_dark_circles(img)
    hair = detect_hair_loss(img)
    skin_type = detect_skin_type(img)

    result = f"""  
   
 AI BEAUTY PASSPORT REPORT

Acne Level: {acne}

Wrinkle Level: {wrinkle}

Dark Circles: {dark}

Hair Condition: {hair}

Skin Type: {skin_type}


"""

    return result

def beauty_recommendation(acne, wrinkle, dark_circle, hair, skin_type):
       recommendation = []
      if "Moderate" in acne or "Severe" in acne:
        rec.append("Use Salicylic Acid Cleanser")
        rec.append("Anti-acne facial treatment")

     if "Moderate" in wrinkle or "High" in wrinkle:
        rec.append("Use Retinol Anti-aging Cream")

     if "Dark" in dark_circle:
        rec.append("Vitamin C Eye Cream")

     if "Hair Loss" in hair:
        rec.append("Use Biotin Shampoo")
        rec.append("Hair Growth Serum")

    if skin_type == "Dry Skin":
        rec.append("Use Hyaluronic Moisturizer")

         return recommendation

def predictive_homecare(acne, wrinkle, dark_circle, hair):

    morning = []
    night = []
    haircare = []

    if "Acne" in acne:
        morning.append("Salicylic Acid Face Wash")
        night.append("Acne Spot Treatment")

    if "Wrinkles" in wrinkle:
        night.append("Retinol Cream")

    if "Dark" in dark_circle:
        morning.append("Vitamin C Eye Cream")

    if "Hair Loss" in hair:
        haircare.append("Biotin Shampoo (3x/week)")
        haircare.append("Scalp Massage")

    return morning, night, haircare



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
     rec = beauty_recommendation(acne, wrinkle, dark_circle, hair, skin)

    st.subheader("Personalized Beauty Recommendation") 

   st.write("### Recommendations")
    for r in recommendation:
     st.write("-", r)

 morning, night, haircare = predictive_homecare(acne, wrinkle, dark_circle, hair)

    st.subheader("Predictive Home Care Plan")

    st.write("Morning Routine")
    for m in morning:
        st.write("-", m)

    st.write("Night Routine")
    for n in night:
        st.write("-", n)

    st.write("Hair Care")
    for h in haircare:
        st.write("-", h)

    # Display output
    st.subheader("Analysis Result")
    st.write(result)
