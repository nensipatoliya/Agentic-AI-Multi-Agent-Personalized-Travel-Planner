#!/usr/bin/env python
# coding: utf-8

# In[3]:


import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv("Dot.env")
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def planner_agent(query):

    prompt = f"""
    Create day wise travel itinerary based on:

    {query}

    Include places, time schedule and activities.
    """

    response = model.generate_content(prompt)

    return response.text

