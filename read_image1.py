import cv2

img = cv2.imread("C:/Users/SESA457837/Downloads/PRO-c116-Teacher-Reference-Code-main/PRO-c116-Teacher-Reference-Code-main/butterfly.jpg")

cv2.imshow("Display Image", img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale

cv2.imshow("Grayscale", gray_img)

cv2.waitKey(0) & 0xFF == ord('q')  # Wait for a keyboard input 'q' and if it is pressed then break the loop

# Close all windows
cv2.destroyAllWindows()