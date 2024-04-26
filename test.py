import ffmpeg
import math
import numpy as np
def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        try:
            num, denom = frac_str.split('/')
        except ValueError:
            return None
        try:
            leading, num = num.split(' ')
        except ValueError:
            return float(num) / float(denom)
        if float(leading) < 0:
            sign_mult = -1
        else:
            sign_mult = 1
        return float(leading) + sign_mult * (float(num) / float(denom))

video_path = "./examples/charades.mp4"
probe = ffmpeg.probe("./examples/charades.mp4")
video_stream = next((stream for stream in probe['streams']
                        if stream['codec_type'] == 'video'), None)
width = int(video_stream['width'])
height = int(video_stream['height'])
fps = math.floor(convert_to_float(video_stream['avg_frame_rate']))
try:
    frames_length = int(video_stream['nb_frames'])
    duration = float(video_stream['duration'])
except Exception:
    frames_length, duration = -1, -1
info = {"duration": duration, "frames_length": frames_length,
        "fps": fps, "height": height, "width": width}

print(info)

cmd = ffmpeg.input(video_path).filter('fps', fps=fps).filter('scale', width, height)
    # .filter('scale', self.size, self.size)

out, err = cmd.output('pipe:', format='rawvideo', pix_fmt='rgb24').run(capture_stdout=True, capture_stderr=True)
# print(err)
# print(out)
video = np.frombuffer(out, np.uint8).reshape(
    [-1, height, width, 3])