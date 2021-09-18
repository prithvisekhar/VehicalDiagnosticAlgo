import cv2


def get_frames(video):
    def getFrame(x):
        video.set(cv2.CAP_PROP_POS_MSEC, x * 1000)
        hasFrames, image = video.read()
        if hasFrames:
            cv2.imwrite(str(count) + ".jpg", image)
        return hasFrames

    sec = 0
    frameRate = 1  # //it will capture image in each 0.5 second
    count = 1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)


# video = cv2.VideoCapture('Pothole_trial_18_6_0.mp4')
# Videofile = cv2.VideoCapture('D://G Drive backup//LTTS Internship//Data-OBD//Swift//MarL1_Out.mp4')
# get_frames(Videofile)
