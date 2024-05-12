import cv2

# Load the image
image = cv2.imread('D:/SEPR/Spectrogram Images/train2000_images/0/bass_acoustic_000-060-100.png')

# Check the shape of the image
height, width, channels = image.shape

print("Number of channels:", channels)
print("Image size: ", height, "X", width)