import argparse
from imutils.video import VideoStream
import cv2


# initialize video frame in main
def init_video():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video",
                    help="path to the (optional) video file")
    args = vars(ap.parse_args())

    if not args.get("video", False):
        vs = VideoStream(src=0).start()
    else:
        vs = cv2.VideoCapture(args["video"])

    return vs


def main():
    vs = init_video()

    while True:
        frame = vs.read()
        cv2.imshow("frame", frame)


if __name__ == "__main__":
    main()
