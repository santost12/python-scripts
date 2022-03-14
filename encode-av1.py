#!/usr/bin/python3

import os

# See: https://ffmpeg.org/trac/ffmpeg/wiki/CompilationGuide
ffmpegBinary = "\"/home/ffmpeg/bin/ffmpeg\""

# change these for your setup
inputPath = "/home/ffmpeg/videos/"
outputPath = "/home/ffmpeg/videos-output/"

cpuUsed = "4"
libaom_av1 = "yes"
copyAudio = "yes"
copySubtitles = "yes"
crf = "30"

# 10bit video
yuv420p10le = "yes"


if libaom_av1 == "yes" and copyAudio == "yes" and copySubtitles == "yes" and yuv420p10le == "yes":
	for file in os.listdir(inputPath):
		os.path.join(inputPath, file)
		finalInput = "\"" + inputPath + file + "\""
		finalOutput = "\"" + outputPath + file + "\""

		os.system(ffmpegBinary + " -i " + finalInput + " -cpu-used " + cpuUsed + " -c:v libaom-av1" + " -crf " + crf + " -pix_fmt yuv420p10le -b:v 0 -c:a copy -c:s copy " + finalOutput)
