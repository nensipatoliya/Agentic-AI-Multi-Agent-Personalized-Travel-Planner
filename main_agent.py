#!/usr/bin/env python
# coding: utf-8

# In[7]:


import google.generativeai as genai
import os
from dotenv import load_dotenv

from agents.planner_agent import planner_agent
from agents.booking_agent import booking_agent
from agents.weather_agent import weather_agent

load_dotenv("Dot.env")
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def travel_master_agent(user_query):

    plan = planner_agent(user_query)

    booking = booking_agent(plan)

    weather = weather_agent(plan)

    final_prompt = f"""
    Combine travel plan, booking info and weather forecast.

    PLAN:
    {plan}

    BOOKING:
    {booking}

    WEATHER:
    {weather}
    """

    response = model.generate_content(final_prompt)

    return response.text

