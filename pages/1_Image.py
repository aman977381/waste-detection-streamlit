import cv2
import math
import numpy as np
import streamlit as st
from PIL import Image
from ultralytics import YOLO

st.write("# Let's detect the Waste 🗑️")
st.write("Welcome to Garbage Detection WebApp! Try uploading an image to see our advanced algorithms in action. We'll analyze the waste and categorize it for you. Together, let's take a step towards a cleaner environment.")

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.unsplash.com/photo-1597655601841-214a4cfe8b2c?q=80&w=1889&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
    background-color: rgba(255, 255, 255, 0.1);
}
[data-testid=stSidebar] {
        background-color: #5888c6;
    }
</style>
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

def predict(img):
    model = YOLO(r"best.pt")
    results = model(img,stream=True)
    classNames = ['BIODEGRADABLE', 'CARDBOARD', 'GLASS', 'METAL', 'PAPER', 'PLASTIC']
    name = ""
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1),int(y1),int(x2),int(y2)
            w, h = x2-x1,y2-y1

            cv2.rectangle(img,(x1, y1), (x2, y2),color=(255,0,0), thickness=2)
            conf = math.ceil((box.conf[0]*100))/100
            cls = box.cls[0]
            print(conf)
            name = classNames[int(cls)]

            cv2.putText(img,f"{name} {conf}",(max(0,x1), max(35,y1)),cv2.FONT_HERSHEY_DUPLEX,0.5,(0,150,0),1)
    return img,name

def main_loop():
    
    image_file = st.sidebar.file_uploader("Upload Your Image Here", type=['jpg', 'png', 'jpeg'])

    if not image_file:
        image_file = r"test_img.jpg"
    
    uploaded_img = Image.open(image_file)
    uploaded_img = np.array(uploaded_img)
    img = uploaded_img.copy()
    #cv2.imshow("orig",original_img)
    predict_img, name = predict(img)


    col1.write("original 📷")
    col1.image(uploaded_img,width = 350)
    #st.sidebar.image(uploaded_img, width = 250)
    col2.write(f"👉{name} Predicted")
    col2.image(predict_img, width = 350)
    
    #st.sidebar.download_button("Download fixed image", "fixed.png", "image/png")

col1, col2 = st.columns(2)
if __name__ == '__main__':
    main_loop()