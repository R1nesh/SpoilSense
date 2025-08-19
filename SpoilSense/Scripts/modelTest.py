
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO
from tkinterdnd2 import TkinterDnD, DND_FILES
#Change the model path to an absolute locatl path if this doesnt work
MODEL_PATH = r'..\runs_mod1\detect\train\weights\best.pt'

def load_model(model_path):
    model = YOLO(model_path)
    return model

def process_image(image_path):
    image = Image.open(image_path)
    return image

def predict(model, image):
    results = model(image)
    return results

def display_results(results, canvas, label):
    result = results[0]
    print("Detection Results:")
    print(f"Detected Boxes: {result.boxes}")
    print(f"Detected Classes: {result.names}")
    print(f"Detection Probabilities: {result.probs}")
    print(f"Image Shape: {result.orig_shape}")
    print(f"Inference Speed: {result.speed}")
    img_with_boxes = result.plot()
    img_with_boxes = Image.fromarray(img_with_boxes)
    img_with_boxes = resize_image(img_with_boxes, 640, 400)
    img_with_boxes = ImageTk.PhotoImage(img_with_boxes)
    canvas.create_image(0, 0, anchor="nw", image=img_with_boxes)
    canvas.image = img_with_boxes
    label.config(text="Processing Complete! Upload Another Image.")

def upload_image_from_path(image_path, canvas, label):
    label.config(text="Processing Image... Please wait.")
    if image_path:
        model = load_model(MODEL_PATH)
        image = process_image(image_path)
        results = predict(model, image)
        display_results(results, canvas, label)

def on_drop(event, canvas, label):
    image_path = event.data
    upload_image_from_path(image_path, canvas, label)

def upload_image( canvas, label):
    label.config(text="Processing Image... Please wait.")
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.webp")])
    if image_path:
        model = load_model(MODEL_PATH)
        image = process_image(image_path)
        results = predict(model, image)
        display_results(results, canvas, label)

def resize_image(image, max_width, max_height):
    img_width, img_height = image.size
    aspect_ratio = img_width / img_height
    if img_width > max_width or img_height > max_height:
        if aspect_ratio > 1:
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
        else:
            new_height = max_height
            new_width = int(max_height * aspect_ratio)
        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return image

def create_gui():
    root = TkinterDnD.Tk()
    root.title("YOLO Image Inference")
    canvas = tk.Canvas(root, width=640, height=480)
    canvas.pack(pady=20)
    label = tk.Label(root, text="Upload Image", font=("Helvetica", 20))
    upload_button = tk.Button(root, text="Upload Image", command=lambda: upload_image(canvas, label))
    upload_button.pack(pady=20)
    label = tk.Label(root, text="Drag and Drop an Image Here", font=("Times New Roman", 25))
    label.pack(pady=10)
    root.drop_target_register(DND_FILES)
    root.mainloop()

if __name__ == "__main__":
    create_gui()