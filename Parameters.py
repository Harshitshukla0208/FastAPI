# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel

# Class which describes Bank Notes measurements
class Parameters(BaseModel):
    Accelerometer_1: float  # Accelerometer 1 (m/s^2)
    Temperature: float  # Temperature (Celsius)
    healthy: float  # Healthy status
