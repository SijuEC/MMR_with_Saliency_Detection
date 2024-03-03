import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from torchvision.transforms.functional import to_pil_image
import math

def sal_check(batch):
    ### This function takes each batch and processes each image to find the salient regions inside
    ### the image, i.e. the region of the image where the blade probably resides.
    ### The input of the function is the batch from the dataloader.
    ### The function returns a list of the bounding box info
    ### Each element of the list has the information as follows:
    ### [x (The x coordinate of the top left corner), y (The y coordinate of the top left corner),
    ### w (The width of the bounding box), h (The height of the bounding box)]
    
    bounding_rects = []
    for img in batch['image']:
        img = to_pil_image(img)
        img = np.array(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        saliency = cv2.saliency.StaticSaliencyFineGrained_create()
        success, saliencyMap = saliency.computeSaliency(gray)
        saliencyMap = (saliencyMap * 255).astype("uint8")

        # Threshold the saliency map
        _, threshMap = cv2.threshold(saliencyMap, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Find contours
        contours, _ = cv2.findContours(threshMap, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:

            # Find the largest contour
            largest_contour = max(contours, key=cv2.contourArea)

            # Compute the bounding box
            x, y, w, h = cv2.boundingRect(largest_contour)
            
            bounding_rects.append([x, y, w, h])

            # # Draw the bounding box on the original image
            # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 10)

        # plt.figure(figsize=(5,1))
        # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # plt.axis('off')
        # plt.show()
        # plt.close()
    return bounding_rects



def find_sal_region(img):
    ### This function takes an image and finds the salient regions inside
    ### the image, i.e. the region of the image where the blade probably resides.
    ### The input of the function is an image.
    ### The function returns a list of the bounding box info
    ### Each element of the list has the information as follows:
    ### [x (The x coordinate of the top left corner), y (The y coordinate of the top left corner),
    ### w (The width of the bounding box), h (The height of the bounding box)]
    
    img = to_pil_image(img)
    img = np.array(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    saliency = cv2.saliency.StaticSaliencyFineGrained_create()
    success, saliencyMap = saliency.computeSaliency(gray)
    saliencyMap = (saliencyMap * 255).astype("uint8")

    # Threshold the saliency map
    _, threshMap = cv2.threshold(saliencyMap, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(threshMap, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:

        # Find the largest contour
        largest_contour = max(contours, key=cv2.contourArea)

        # Compute the bounding box
        x, y, w, h = cv2.boundingRect(largest_contour)

        bounding_rects = [x, y, w, h]

    return bounding_rects


def find_sal_patches(img):
    ### This function takes an image and finds the salient patches inside
    ### the image, i.e. the patches of the image where the blade probably resides.
    ### The input of the function is an image.
    ### The function returns a list indexes of the patches where the blade resides
    
    patch_size = 16
    
    img = to_pil_image(img)
    img = np.array(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    saliency = cv2.saliency.StaticSaliencyFineGrained_create()
    success, saliencyMap = saliency.computeSaliency(gray)
    saliencyMap = (saliencyMap * 255).astype("uint8")

    # Threshold the saliency map
    _, threshMap = cv2.threshold(saliencyMap, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(threshMap, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:

        # Find the largest contour
        largest_contour = max(contours, key=cv2.contourArea)

        # Compute the bounding box
        x, y, w, h = cv2.boundingRect(largest_contour)
        
    X = math.floor(x/patch_size)
    Y = math.floor(y/patch_size)
    W = math.ceil(w/patch_size)
    H = math.ceil(h/patch_size)
    
    num_horiz_patches = W-X
    num_rows = H-Y
    
    patches = []
    
    for row in range(Y, Y+H):
        for col in range(X, X+W):
            patch_num = (row * 14) + (col)
            patches.append(patch_num)   

    return patches