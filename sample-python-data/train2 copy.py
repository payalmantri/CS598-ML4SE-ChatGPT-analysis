import cv2

def show_prediction_labels_on_image(img_path, predictions):
    """
    Shows the face recognition results visually.

    :param img_path: path to image to be recognized
    :param predictions: results of the predict function
    :return:
    """
    img = cv2.imread(img_path)

    for name, (top, right, bottom, left) in predictions:
        # Draw a box around the face using OpenCV
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

        # Convert name to string if it's not already
        if not isinstance(name, str):
            name = str(name)

        # Draw a label with a name below the face
        label_size, _ = cv2.getTextSize(name, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        cv2.rectangle(img, (left, bottom - label_size[1] - 10), (right, bottom), (0, 0, 255), cv2.FILLED)
        cv2.putText(img, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Face Recognition Result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
