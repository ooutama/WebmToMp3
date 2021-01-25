# Convert webm files to mp3 using FFMPEG
# To use this script you need to install FFMPEG in your system
# For windows users, you need to download & add FFMPEG to the PATH (Windows Environment Variables)

import os
import re
import subprocess
import argparse
import sys

# The parser
parser = argparse.ArgumentParser(description='Convert webm files of a specific directory to mp3 using ffmpeg.')

# The arguments
parser.add_argument('--webm_path',
                    #    metavar='webm_path',
                    action='store',
                       type=str,
                       required=True,
                       help='The path of webm files')

parser.add_argument('--mp3_path',
                    #    metavar='mp3_path',
                        action='store',
                       type=str,
                       required=False,
                       help='The path of mp3 files',
                    #    default=None,
                    )

args = parser.parse_args()
# input_path = args.Path

if not os.path.isdir(args.webm_path):
    print(f'The webm path "{args.webm_path}" does not exist.')
    sys.exit()

if args.mp3_path == None:
    args.mp3_path = args.webm_path

elif not os.path.isdir(args.mp3_path):
    os.makedirs(args.mp3_path)


for file in os.listdir(args.webm_path):
    webmFile = os.path.join(args.webm_path, file)
    mp3File = os.path.join(args.mp3_path, file).replace(
        "webm", "mp3")

    command = f"ffmpeg -i \"{webmFile}\" -vn -ab 128k -ar 44100 -y \"{mp3File}\""
    subprocess.call(command, shell=True)
