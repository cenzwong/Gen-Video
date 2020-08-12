ffmpeg -i input.mp3 -i input.mp4 -c:v copy output.mp4 -y

call activate ProgramTrade_Playground
python ./upload_video.py
call conda deactivate
echo "Done"

pause