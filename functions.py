import os


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


if __name__ == "__main__":

    print(get_cred())
