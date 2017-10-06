# Humaniod_SpeechFramework build in python

# Abstract:

MUSTani detects words/patterns based on learned results <br />
MUSTani must be trained to get results <br />
MUSTani works offline <br />
MUSTani recognizes words/patterns in real time and requires a multi core processor architecture <br />
MUSTani is highly configurable for quick and dirty results as well as for more precise recognition <br />
MUSTani was tested and developed with Python 2.7 on a Raspberry Pi 2 <br />
MUSTani comes with a very simple plugin interface for further processing <br />

# dependencies required to install- <br />
pip install SpeechRecognition <br />
pip install py-audio 0.2.11 <br />
pip install pywapi --allow -external --allow -unverified <br />
pip install wikipedia <br />
pip install requests <br />
pip intall beautifulsoup4 <br />
pip install numpy <br />
pip install matplotlib <br />
pip install scipy <br />


# Key ingredient - From a high-level view

main.py - This involves recording the user’s voice, capturing the
words from the recording (cancelling any noise and fixing distortion in the process), and
then using natural language processing (NLP) to convert the recording to a text string

brain.py - component that receives the text string from the STT
engine and handles the input by processing it and passing the output to the TTS enginebrain; 
it handles user queries via a series of if - then - else clauses in the Python programming language. 
It decides what the output should be in response to specific inputs.

mustani.py - Motion Control based on trained aatribute

tts.py - This component receives the output from Mlogic engine and converts the string to
speech to complete the interaction with the user

conversation.py - This involves building additional third-party modules to be implemented in logic engine
(ex- time module,weather module,news module,wikipedia module.etc )
