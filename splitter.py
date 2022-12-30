from pathlib import Path
from moviepy.editor import VideoFileClip
import subprocess
from termcolor import colored
import os


def final_scenes_splitter(mkvmerge_path, videos_path, ending_cut_time):
  videos = Path(videos_path)
  for i, video_path in enumerate(videos.iterdir()):
    print(colored(video_path, "green"))
    video = VideoFileClip(str(video_path))
    video_duration = video.duration
    mkvmerge_list = [
      mkvmerge_path, # Software
      f"--split", # Split option
      str(video_duration - ending_cut_time) + "s", # Split timestamp in seconds
      video_path, # Video to split
      "-o", # Output option
      os.path.join(videos, "%02d.mkv" % (i+1)) # Output path
    ]
    subprocess.run(mkvmerge_list)


mkvmerge_path = "C:/Program Files/MKVToolNix/mkvmerge.exe"
videos_path = "E:/Grabaciones/Soulcalibur VI/Peleas/SSLL 1 PS4"
ending_cut_time = 21 # Seconds

final_scenes_splitter(mkvmerge_path, videos_path, ending_cut_time)