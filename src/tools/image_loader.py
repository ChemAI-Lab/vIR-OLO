'''
Take a folder containing images of spectrograms and load them into the UI application

The script contains a maing object ImageManager(), which stores information on the current 
image loaded, the state of its annotations and the list of images in the folder.

Important utilities include the saving process to create annotations in YOLO format

The information on the folder and images is stored in a global dictionary, read from a 
json configuration file passed by the user — and created by the program — when a New 
project is created.
'''

import os
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import io # Convert PIL image to bytes
from os.path import join as jn 

class ImageManager():
    def __init__(self, images_path=None, annotations_path = None):
        self.current_image = None
        self.current_index = 0
        self.annotations = sorted([jn(annotations_path, f) for f in os.listdir(annotations_path) if f.lower().endswith(('.txt'))])
        self.image_list = sorted([jn(images_path, f) for f in os.listdir(images_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    def load_image(self):
        """
        Load the image at current_index and return a QPixmap ready for QLabel display.
        
        Returns:
            QPixmap or None: The loaded image as QPixmap, or None if loading fails
        """
            
        # Get the image path from the list using current_index
        image_path = self.image_list[self.current_index]
             
        # Load image using PIL
        pil_image = Image.open(image_path)
        
        # Convert PIL image to RGB if it's not already to allow it to handle different formats
        if pil_image.mode != 'RGB':
            pil_image = pil_image.convert('RGB')
        
        img_bytes = io.BytesIO()
        pil_image.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        # Create QPixmap from bytes
        pixmap = QPixmap()
        pixmap.loadFromData(img_bytes.getvalue())
        
        # Store reference to current image path
        self.current_image = image_path
        
        return pixmap

    def fit_to_window(self, width: int, height: int, pixmap: QPixmap, stretch: bool = True) -> QPixmap:
        """
        Scale the current image to fit within the specified window dimensions.
        
        Args:
            width (int): The width of the canvas/window
            height (int): The height of the canvas/window
            pixmap (QPixmap): The original QPixmap image to be scaled
            stretch (bool): If True, stretch image to fill window, ignoring aspect ratio
                
        Returns:
            QPixmap: The scaled image as a QPixmap object
        """
            
        # Get the image dimensions
        img_width = pixmap.width()
        img_height = pixmap.height()
        
        if stretch:
            # Simply use the target dimensions
            new_width = width
            new_height = height
            aspect_flag = Qt.IgnoreAspectRatio
        else:
            # Calculate scaling ratios
            width_ratio = width / img_width
            height_ratio = height / img_height
            
            # Use the smaller ratio to ensure the image fits in both dimensions
            scale_ratio = min(width_ratio, height_ratio)
            
            # Calculate new dimensions
            new_width = int(img_width * scale_ratio)
            new_height = int(img_height * scale_ratio)
            aspect_flag = Qt.KeepAspectRatio
        
        # Scale the pixmap
        scaled_pixmap = pixmap.scaled(new_width, new_height, 
                                    aspect_flag, 
                                    Qt.SmoothTransformation)
        
        return scaled_pixmap
    
    def render(self, QtLabel):
        """
        Render the current image onto a given QLabel.
        
        Args:
            QLabel: The QLabel widget where the image will be displayed.
        """
        
        width = QtLabel.width()
        height = QtLabel.height()
        
        # Load the original pixmap
        pixmap = self.load_image()
        # Scale it using fit_to_window
        scaled_pixmap = self.fit_to_window(width, height, pixmap)
        
        # Set the scaled pixmap to the label
        QtLabel.setPixmap(scaled_pixmap)
        
    def next_image(self):
        '''
        Update the index in the Image Manager
        '''
        if self.current_index < len(self.image_list) - 1:
            self.current_index += 1
    
    def previous_image(self):
        '''
        Update the index in the Image Manager
        '''
        if self.current_index > 0:
            self.current_index -= 1