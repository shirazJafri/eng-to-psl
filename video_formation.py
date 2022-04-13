from moviepy.editor import *
from word_mapping import bare_form
import os

path = '/home/shiraz/OneDrive/FYP/API/static'

def video_formation(sentences, paths):

    if paths:

        combined_sentence = ' '.join(sentences)

        combined_sentence = bare_form(combined_sentence)

        hashed_sentence = str(abs(hash(combined_sentence)))

        file_name = hashed_sentence + ".mp4"

        if file_name not in os.listdir(path):
            clips = [VideoFileClip(clips_path) for clips_path in paths]

            final_video = concatenate_videoclips(clips, method= "compose")

            print('Combined Sentence ', combined_sentence)

            final_video.write_videofile(os.path.join(path, file_name))

        return file_name

    return ""