"""
predict.py - Model Inference Utilities for spectrAI

This module provides helper functions to load a YOLO model (Ultralytics) from a .pt file and run object detection predictions on images.

Key Features:
- Loads YOLO models from specified weight files (.pt)
- Runs inference on a given image path
- Returns the prediction results for further processing (e.g., extracting bounding boxes)

Notes:
- This module does not import or use OpenCV (cv2) directly, as the Ultralytics YOLO API handles image loading and processing internally.
- If you need to save or manipulate result images (e.g., using results[0].plot()), you may need to import cv2 in your own script.

Example usage:
	from predict import run_yolo_prediction
	result = run_yolo_prediction('path/to/model.pt', 'path/to/image.png')
	boxes = result.boxes
"""
import os
from ultralytics import YOLO


def reformat_results(result):
	"""
	Converts a YOLO Results object into a list of dictionaries with pixel coordinates and class index.
	Each dictionary has keys: 'x', 'y', 'w', 'h', 'idx'.
	All values are in pixels, not normalized.
	"""
	boxes = []
	if hasattr(result, 'boxes') and result.boxes is not None:
		# result.boxes.xywh is (N, 4) tensor: x_center, y_center, width, height (pixels)
		# result.boxes.cls is (N,) tensor: class indices
		xywh = result.boxes.xywh.cpu().numpy()
		cls = result.boxes.cls.cpu().numpy().astype(int)
		for i in range(xywh.shape[0]):
			x_c, y_c, w, h = xywh[i]
			idx = int(cls[i])
			box = {"x": float(x_c), "y": float(y_c), "w": float(w), "h": float(h), "idx": idx}
			boxes.append(box)
	return boxes

def run_yolo_prediction(model_path: str, image_path: str):
    """
	Loads a YOLO model from model_path, runs prediction on image_path, and returns results[0].
	"""
    model = YOLO(model_path)
    results = model(image_path)
    formatted_results = reformat_results(results[0])
    return formatted_results

if __name__ == "__main__":
    # Example usage
    model_path = "C:\\Users\\Uriel\\Desktop\\spectrAI\\images\\models\\spectrai-IR-YOLO\\spectrai_ultralytics_ir.pt"
    image_path = "C:\\Users\\Uriel\\Desktop\\spectrAI\\images\\images\\train\\image_000000.png"
    result = run_yolo_prediction(model_path, image_path)
    
    # example output
    # [{'x': 285.2972717285156, 'y': 48.377777099609375, 'w': 15.4547119140625, 'h': 46.86598205566406, 'idx': 11}]