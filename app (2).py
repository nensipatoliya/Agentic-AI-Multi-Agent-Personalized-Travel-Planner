#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
from main_agent import travel_master_agent

st.title("🌍 Agentic AI Travel Planner")

query = st.text_input("Enter Travel Request")

if st.button("Plan Trip"):

    result = travel_master_agent(query)

    st.write(result)

