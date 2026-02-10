#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

