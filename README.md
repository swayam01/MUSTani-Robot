# Humaniod_SpeechFramework build in python

dependencies required to install-
pip install SpeechRecognition
pip install py-audio 0.2.11
pip install pywapi --allow -external --allow -unverified
pip install wikipedia
pip install requests
pip intall beautifulsoup4

Key ingredient - From a high-level view, these are the three basic components that make up

main.py - This involves recording the user’s voice, capturing the
words from the recording (cancelling any noise and fixing distortion in the process), and
then using natural language processing (NLP) to convert the recording to a text string

brain.py - component that receives the text string from the STT
engine and handles the input by processing it and passing the output to the TTS enginebrain; 
it handles user queries via a series of if - then - else clauses in the Python programming language. 
It decides what the output should be in response to specific inputs.

tts.py - This component receives the output from Mlogic engine and converts the string to
speech to complete the interaction with the user

conversation.py - This involves building additional third-party modules to be implemented in logic engine
(ex- time module,weather module,news module,wikipedia module.etc )
