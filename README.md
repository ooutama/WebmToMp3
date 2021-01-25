# WebmToMp3

Convert all the webm file of a directory to mp3 using python and FFMPEG

## Note
To use this script, you should install **FFMPEG** in your system.
For Windows users, you need to download & add **FFMPEG** to the PATH (Windows Environment Variables).

## Usage
```bash
WebmToMp3.py --webm_path "/home/music/webm_files" --mp3_path "/home/music/mp3_files"
```

```bash
WebmToMp3.py --webm_path "/home/music/webm_files"
# It will put the generated mp3 files in the same folder of webm files
```

```bash
WebmToMp3.py --webm_path "/home/music/webm_files" --mp3_path "/home/music/non_existent_folder"
# It will create the non-existent path automatically
```