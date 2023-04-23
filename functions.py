import os
import glob
import time


def get_cred():
    cred_dic = {}
    for key in os.environ:
        if key == "PASSWORD_WEBCAM_APP":
            cred_dic["PASSWORD_WEBCAM_APP"] = os.environ["PASSWORD_WEBCAM_APP"]
        elif key == "SENDER_WEBCAM_APP":
            cred_dic["SENDER_WEBCAM_APP"] = os.environ["SENDER_WEBCAM_APP"]
        elif key == "RECEIVER_WEBCAM_APP":
            cred_dic["RECEIVER_WEBCAM_APP"] = os.environ["RECEIVER_WEBCAM_APP"]
    return cred_dic


def get_all_images():
    all_images = glob.glob("images/*.png")
    img_dict = {}
    for image in all_images:
        key = image.replace("images", '').replace('.png', '').replace('\\', '')
        img_dict[key] = image
    return img_dict


def clean_folder():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)


if __name__ == "__main__":

    # print(get_cred())
    print(type(get_all_images()))
