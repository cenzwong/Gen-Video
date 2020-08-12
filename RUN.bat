CALL download_MP3.bat
cd Python_audio_v2
CALL combine_audio.bat
cd ..
cd Python_video_v2
pause
CALL combine_video.bat
cd ..
cd Video_combine
CALL convert_and_upload.bat
pause