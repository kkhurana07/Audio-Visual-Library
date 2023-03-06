# Helper functions for Blackfoot project
# CMPT 120 
# Nov. 12, 2020
import functions
import wave
from replit import audio

def concat(infiles,outfile):
  """
  Input: 
  - infiles: a list containing the filenames of .wav files to concatenate,
    e.g. ["hello.wav","there.wav"]
  - outfile: name of the file to write the concatenated .wav file to,
    e.g. "hellothere.wav"
  Output: None
  """
  data= []
  for infile in infiles:
      w = wave.open(infile, 'rb')
      data.append( [w.getparams(), w.readframes(w.getnframes())] )
      w.close()    
  output = wave.open(outfile, 'wb')
  output.setparams(data[0][0])
  for i in range(len(data)):
      output.writeframes(data[i][1])
  output.close()


#defining concatenate function, which will help in speech synthesis
def concatenate():
  file = open("translation (2).csv")
  synthesis_dict = {}
  
  for line in file:
    (key,value) = line.strip().split(",")

    synthesis_dict[str(key)]= value
 
  #print(synthesis_dict)
  for i in range(3):
    print("Which phrase do you wanna form ?(Enter the three English words) \n")
    concatlist = []
    for i in range(3):
      Words = input().replace(" ","").lower()
      for word in Words:
        newword = "sounds/" + Words + ".wav"
      concatlist.append(newword)
    
    concat(concatlist,"synthesis.wav")
    audio.play_file("synthesis.wav") 
  
  functions.move() 

    

    




    




  





