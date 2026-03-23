import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("AI Beauty Passport System")
st.write("Upload a face image for AI skin & hair analysis")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

# -----------------------------
# AI ANALYSIS FUNCTIONS
# -----------------------------

def detect_acne(image):

    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    acne_pixels = np.sum(mask>0)

    if acne_pixels < 5000:
        return "Low Acne"
    elif acne_pixels < 15000:
        return "Moderate Acne"
    elif acne_pixels < 20000:
        return "Severe Acne"
    else:
        return "High Acne"


def detect_wrinkles(face):

    gray = cv2.cvtColor(face, cv2.COLOR_RGB2GRAY)

    edges = cv2.Canny(gray,100,200)

    wrinkle_score = np.sum(edges)

   if wrinkle_score < 10000:
        result = "Low Wrinkles"
    elif wrinkle_score < 50000:
        result = "Moderate Wrinkles"
    elif wrinkle_score < 100000:
        result = "High Wrinkles"
    else:
        result = "Severe Wrinkles"
        

def detect_dark_circles(face):

    h, w, _ = face.shape

    eye_region = face[int(h*0.45):int(h*0.65), int(w*0.2):int(w*0.8)]

    gray = cv2.cvtColor(eye_region, cv2.COLOR_RGB2GRAY)

    brightness = np.mean(gray)

    if brightness < 200:
        return "Severe Dark Circles"
    elif brightness < 150:
        return "Moderate Dark Circles"
    elif brightness <75:
        return "Low Dark Circles"
    else:
        return "Healthy Under-Eye"


def analyze_skin_brightness(face):

    gray = cv2.cvtColor(face, cv2.COLOR_RGB2GRAY)

    brightness = np.mean(gray)

    if brightness < 80:
        return "Dry Skin"
    elif brightness < 150:
        return "Normal Skin"
    else:
        return "Oily Skin"


def detect_hair_loss(img):

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    edges = cv2.Canny(gray,50,150)

    density = np.sum(edges)/(edges.shape[0]*edges.shape[1])

    if density < 15:
        return "High Hair Loss"
    elif density < 50:
        return "Moderate Hair Loss"
    else:
        return "Healthy Hair"


# -----------------------------
# RECOMMENDATION
# -----------------------------

def beauty_recommendation(acne, wrinkle, dark_circle, hair, skin_type):

    rec = []

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

    return rec


# -----------------------------
# PREDICTIVE HOME CARE PLAN
# -----------------------------

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


# -----------------------------
# PROCESS IMAGE
# -----------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    img = np.array(image)

    st.image(img, caption="Uploaded Image")

    acne = detect_acne(img)
    wrinkle = detect_wrinkles(img)
    dark_circle = detect_dark_circles(img)
    skin = analyze_skin_brightness(img)
    hair = detect_hair_loss(img)

    st.subheader("AI Beauty Analysis")

    st.write("Acne:", acne)
    st.write("Wrinkles:", wrinkle)
    st.write("Dark Circles:", dark_circle)
    st.write("Skin Type:", skin)
    st.write("Hair Condition:", hair)

    rec = beauty_recommendation(acne, wrinkle, dark_circle, hair, skin)

    st.subheader("Personalized Beauty Recommendation")

    for r in rec:
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



   

   
   


  
 

    
 
