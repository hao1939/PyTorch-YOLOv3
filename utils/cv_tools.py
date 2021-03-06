import cv2


def stamp_text(image, box, text=None, color=(255, 255, 255)):
    ''' box = ((x1, y1), (x2, y2)), text align to the left-top corner. '''
    thickness = 2
    cv2.rectangle(image, box[0], box[1], color, thickness)

    if text is None:
        return

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    margin = 2

    text_size, baseline = cv2.getTextSize(text, font, font_scale, thickness)

    textbox_width = text_size[0] + margin
    textbox_height = text_size[1] + baseline + margin
    textbox = ((box[0][0], box[0][1]), (box[0][0] + textbox_width, box[0][1] + textbox_height))
    cv2.rectangle(image, textbox[0], textbox[1], color, cv2.FILLED)

    text_color = (255, 255, 255)
    text_x, text_y = textbox[0][0], textbox[1][1] - baseline
    cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, thickness)


def create_vedio_capture(input):
    ''' input: video file path. Return (cap, (fps, width, height)). '''
    cap = cv2.VideoCapture('../quebec_city_street_view.mp4')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return cap, (fps, width, height)


def create_video_writer(fps, width, height, output="output/output.mp4"):
    ''' "output" should end with extension ".mp4". '''
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    width = int(width)
    height = int(height)
    print("Write video to {0}, fps: {1}, resolution: {2}*{3}.".format(output, fps, width, height))
    return cv2.VideoWriter(output, fourcc, fps, (width, height))
