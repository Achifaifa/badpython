import math
import os
import random
import sys
from pyaudio import PyAudio

freqPower = 1.059463094 # twelfth root of 2
bpm = 138 # quarter notes per minute
quarterLength = 60.0 / bpm
RATE = 11050
songRaw = ''
song = {}

def buildSongData(instrument, patternData, noteData, durationData, lengthData):
	global song
	song[instrument] = [patternData, noteData, durationData, lengthData]

### BASS DRUM ###
bdNotes = [
	[-18, -18, -18, -18, -18, -18, -18], # 0
	[-18, -18, -18, -18, -18], # 1
	[-18, -18, -18, -18], # 2
	[-18, -18, -18, -18], # 3
	[-18, -18, -18, -18, -18, -18, -18, -18], # 4
	[-18, -18, -18, -18, -18], # 5
]
bdDurations = [
	[1, 1, 1, 0.25, 0.25, 0.25, 0.25], # 0
	[1, 1, 1, 0.5, 0.5], # 1
	[1, 1, 1, 0.25], # 2
	[1, 1, 1, 1], #3
	[1, 1, 1.0/3, 1.0/3, 1.0/3, 1.0/3, 1.0/3, 1.0/3], #4
	[1, 1, 0.5, 0.5, 1], # 5
]
bdLengths = [
	bdDurations[0],
	bdDurations[1],
	[1, 1, 1, 1],
	[1, 1, 1, 1],
	bdDurations[4],
	bdDurations[5],
]
bd = [0, 1, 0, 1, 0, 1, 0, 2, 3, 1, 3, 1, 3, 1, 3, 4, 3, 1, 3, 5, 3, 1, 3, 4]
buildSongData("bd", bd, bdNotes, bdDurations, bdLengths)

### MAIN VOICE ###
mainNotes = [
	[-6, -4, -3, -1, 1, 6, 4, 1, -6, 1, -1, -3, -4], # 0
	[-99], # 1
	[-6, -4, -3, -1, 1, -1, -3], # 2
	[-4, -6, -4, -3, -4, -6, -7, -4], # 3
	[-4, -3, -1, 1], #4
]
mainDurations = [
	[0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 1, 1, 0.5, 0.5, 0.5, 0.5], # 0
	[64], # 1
	[0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5], # 2
	[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], # 3
	[0.5, 0.5, 1, 0.5], #4
]
mainLengths = [
	mainDurations[0], # 0
	[64], # 1
	mainDurations[2], # 2
	mainDurations[3], # 3
	[1, 1, 1, 1], # 4
]
main = [1,
		0, 2, 3, 0, 2, 4,
		0, 2, 3, 0, 2, 4,]
buildSongData("main", main, mainNotes, mainDurations, mainLengths)

### CRASH CYMBAL ###
crashNotes = [
	[0, -99], # 0
	[0, -99, 0, 0, 0, 0, 0, 0], # 1
	[0, 0, 0, 0, 0, 0], # 2
]
crashDurations = [
	[3, 28], # 0
	[3, 26, 1.0/3, 1.0/3, 1.0/3, 1.0/3, 1.0/3, 1.0/3], # 1
	[1.0/3, 1.0/3, 1.0/3, 1.0/3, 1.0/3, 1.0/3], # 2
]
crashLengths = [
	[4, 28], # 0
	[4, 26, 1.0/3, 1.0/3, 1.0/3, 1.0/3, 1.0/3, 1.0/3], # 1
	crashDurations[2], # 2
]
crash = [0, 1, 1]
buildSongData("crash", crash, crashNotes, crashDurations, crashLengths)

### REVERSE CRASH CYMBAL ###
revCrashNotes = [
	[-99], # 0
	[0], # 1
	[-99, 0, -99], # 2
]
revCrashDurations = [
	[24], # 0
	[7], # 1
	[26, 4, 2], # 2
]
revCrashLengths = [
	[24], # 0
	[8], # 1,
	[26, 4, 2], # 2
]
revCrash = [0, 1, 2]
buildSongData("revCrash", revCrash, revCrashNotes, revCrashDurations, revCrashLengths)

### BASS ###
bassNotes = [
	[-99], # 0
	[-30, -20, -18, -18, -20, -18], # 1
	[-30, -18, -15, -27, -15, -13], # 2
	[-25, -15, -13, -27, -18, -15], # 3
	[-34, -23, -22, -22, -23, -22], # 4
	[-32, -22, -20, -20, -22, -20], # 5
	[-31, -21, -19, -19, -21, -19], # 6
]
bassDurations = [
	[32], # 0
	[0.5, 0.25, 0.375, 0.25, 0.25, 0.25], # 1
	[0.5, 0.25, 0.25, 0.5, 0.25, 0.25], # 2
	[0.5, 0.25, 0.25, 0.5, 0.25, 0.25], # 3
	[0.5, 0.25, 0.375, 0.25, 0.25, 0.25], # 4
	[0.5, 0.25, 0.375, 0.25, 0.25, 0.25], # 5
	[0.5, 0.25, 0.25, 0.25, 0.25, 0.25], # 6
]
bassLengths = [
	[32], # 0
	[0.5, 0.25, 0.5, 0.25, 0.25, 0.25], # 1
	bassDurations[2],
	bassDurations[3],
	[0.5, 0.25, 0.5, 0.25, 0.25, 0.25], # 4
	[0.5, 0.25, 0.5, 0.25, 0.25, 0.25], # 5
	[0.5, 0.25, 0.5, 0.25, 0.25, 0.25], # 6
]
bass = [0, 1, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1, 2, 1, 1, 1, 3,
		1, 1, 1, 2, 4, 4, 5, 6,
		1, 1, 1, 2, 4, 4, 5, 6,
		1, 1, 1, 2, 4, 4, 5, 6,
		1, 1, 1, 2, 4, 4, 5, 6,]
buildSongData("bass", bass, bassNotes, bassDurations, bassLengths)

### SYNTH ###
synthNotes = [
	[-99], # 0
	[6, 16, 18, 18, 16, 18], # 1
	[6, 18, 21, 9, 21, 23], # 2
	[11, 21, 23, 9, 18, 21], # 3
]
synthDurations = [
	[64], # 0
	[0.5, 0.25, 0.375, 0.25, 0.25, 0.25], # 1
	[0.5, 0.25, 0.25, 0.5, 0.25, 0.25], # 2
	[0.5, 0.25, 0.25, 0.5, 0.25, 0.25], # 3
]
synthLengths = [
	[64], # 0
	[0.5, 0.25, 0.5, 0.25, 0.25, 0.25], # 1
	synthDurations[2],
	synthDurations[3],
]
synth = [0,
		1, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1, 2, 1, 1, 1, 3,
		1, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1, 2, 1, 1, 1, 3,]
buildSongData("synth", synth, synthNotes, synthDurations, synthLengths)

### SECONDARY VOICE ###
secNotes = [
	[-11, -8, -6, -4, -3, 1, -1, -3, -11, -3, -4, -6, -8], # 0
	[-99], # 1
	[-10, -8, -6, -4, -3, -4, -6], # 2
	[-8, -10, -8, -6, -8, -10, -11, -8], # 3
	[-8, -6, -4, -1], # 4
]
secDurations = [
	[0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 1, 1, 0.5, 0.5, 0.5, 0.5], # 0
	[96], # 1
	[0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5], # 2
	[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], # 3
	[1, 1, 1, 1], #4
]
secLengths = [
	mainDurations[0], # 0
	[96], # 1
	mainDurations[2], # 2
	mainDurations[3], # 3
	[1, 1, 1, 1], # 4
]
sec = [1,
		0, 2, 3, 0, 2, 4,]
buildSongData("sec", sec, secNotes, secDurations, secLengths)

### GUITAR ###
guitarNotes = [
	[-99], # 0
	[-18, -22, -20, -19], # 1
]
guitarDurations = [
	[96], # 0
	[8, 4, 2, 2], # 1
]
guitarLengths = [
	[96], # 0
	[8, 4, 2, 2], # 1
]
guitar = [0,
			1, 1]
buildSongData("guitar", guitar, guitarNotes, guitarDurations, guitarLengths)

data = [[] for i in range(8)]

p = PyAudio()

stream = p.open(format =
				p.get_format_from_width(1),
				channels = 1,
				rate = RATE,
				output = True)
os.system("clear")

def getNoteFreq(diff):
	freq = 440 * pow(freqPower, diff)
	return freq

print "Rendering music..."
trackPos = 0
for track in song:
	for pattern in song[track][0]:
		patternPos = 0
		notePos = 0
		for note in song[track][1][pattern]:
			samples = int(quarterLength * song[track][3][pattern][notePos] * RATE);
			duration = int(quarterLength * song[track][2][pattern][notePos] * RATE);
			if note != -99:
				freq = getNoteFreq(note)
				period = RATE / freq
				periodBoundary = period
				positiveSamplesPerPeriod = period / 2
				positiveSamplesBoundary = 0
			t = 0
			for x in xrange(int(duration)):
				if note == -99:
					data[trackPos].append(0.0)
				else:
					if track == "crash":
						data[trackPos].append(random.uniform(0, 0.8) * ((duration - float(x)) / duration))
					elif track == "revCrash":
						data[trackPos].append(random.uniform(0, 0.8) * (float(x) / duration))
					else:
						if x < periodBoundary - 1:
							if (positiveSamplesBoundary < positiveSamplesPerPeriod):
								if track == "synth":
									data[trackPos].append(0.2)
									positiveSamplesBoundary+=0.25
								elif track == "guitar":
									data[trackPos].append(0.5)
									positiveSamplesBoundary+=0.85
								elif track == "bass":
									data[trackPos].append(0.8)
									positiveSamplesBoundary+=0.75
								else:
									data[trackPos].append(0.8)
									positiveSamplesBoundary+=1
							else:
								if track == "synth":
									data[trackPos].append(-0.2)
								elif track == "guitar":
									data[trackPos].append(-0.5)
								else:
									data[trackPos].append(-0.8)
							if track == "bd":
								t += (RATE / 20.0) / RATE
						else:
							if track == "synth":
								data[trackPos].append(-0.2)
							elif track == "guitar":
								data[trackPos].append(-0.5)
							else:
								data[trackPos].append(-0.8)
							periodBoundary+=(period+t)
							positiveSamplesBoundary = 0
			if samples > duration:
				for x in xrange(int(duration), int(samples)):
					data[trackPos].append(0.0)
			notePos+= 1
			patternPos+=1 1
	trackPos+=1

lenData = 0
for x in data:
  lenData = len(x) if len(x) > lenData else lenData

with open('testmusica2.wav', 'w') as f:
  for x in xrange(lenData):
	  sum = 0.0
	  for y in xrange(len(data)):
		  try:
			  sum += data[y][x]
		  except IndexError:
			  pass
	  sample = min(int(((max(min(sum/len(data), 1.0), -1.0)) + 1.0) * 128.0), 255)
	  songRaw += chr(sample)
	  f.write(chr(sample))

print "Music OK"
for DISCARD in xrange(1):
	stream.write(songRaw)
		
stream.stop_stream()
stream.close()
p.terminate()
