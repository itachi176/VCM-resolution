import cv2 
import numpy as np

def YUV_read_frame(filename, size):
    height, width = size
    frame_len = width*height*3//2
    shape = (int(height*1.5), width)

    frames = []
    with open(filename, "rb") as file:
        while True:
            try:
                raw = file.read(frame_len)
                yuv = np.frombuffer(raw, dtype=np.uint8)
                yuv = yuv.reshape(shape)

                img = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420, 3)

                frames.append(img)
            except:
                break
    return frames 

def YUV_read_frame_gray(filename, size):
    height, width = size
    frame_len = width*height*3//2
    shape = (int(height*1.5), width)

    frames = []
    with open(filename, "rb") as file:
        while True:
            try:
                raw = file.read(frame_len)
                yuv = np.frombuffer(raw, dtype=np.uint8)
                yuv = yuv.reshape(shape)

                img = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420, 3)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                frames.append(img)
            except:
                break
    return frames 

def display_frame(frames):
    # for i, frame in enumerate(frames):
    #     feature = Image2HogFeature(frame)
    #     encoded = RLE_encoding(feature, bits=8)
    #     reconstruct = RLE_decode(encoded, feature.shape)
    #     # cv2.imwrite("./frame_feature/frame{}.png".format(i), reconstruct)
    #     show(reconstruct)
    #     # cv2.imshow("video", frame)
    #     print("feature extracted frame {}\n".format(i+1))
    #     if cv2.waitKey(40) & 0xFF == ord('q'):
    #         break
    for i, frame in enumerate(frames):
        cv2.imshow("video", frame)
        print(i)
        if cv2.waitKey(40) & 0xFF == ord('q'):
            break


