import cv2
from PIL import Image
from util import get_limits

YELLOW = [0, 255, 255]  # Yellow in BGR colorspace


def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_limit, upper_limit = get_limits(color=YELLOW)

        mask = cv2.inRange(hsv_image, lower_limit, upper_limit)

        bbox = Image.fromarray(mask).getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
