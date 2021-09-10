"""
Created on 23/03/2021
author: https://github.com/caresppen
"""

import sys
import os
import fnmatch

if sys.platform == 'linux':
    cmd_ffmpeg = 'ffmpeg'
else:
    # Need to install FFMPEG tool: https://www.ffmpeg.org/
    cmd_ffmpeg = r'C:\ffmpeg\bin\ffmpeg.exe'

codec_video = '-c:v h264'
crf = '-crf 23' # Constant Rate Factor (crf): where 0 is lossless, 23 is default, and 51 is worst possible. A lower value is a higher quality
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 128k'
debug = '-ss 00:00:00 -to 00:00:10' # To determine the time frame to be downloaded

# Declare full origin & output path folder
origin = r'~\origin_videoconv'
output = r'~\output_videoconv'

for root, folders, files in os.walk(origin):
    for file in files:
        if not fnmatch.fnmatch(file, '*mp4'):
            continue
        
        path_to_file = os.path.join(root, file)
        file_name, file_extension = os.path.splitext(file)
        
        file_output = f'{output}/o-{file_name}{file_extension}'
        
        cmd = f'{cmd_ffmpeg} -i "{path_to_file}" {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} "{file_output}"'
        
        os.system(cmd)