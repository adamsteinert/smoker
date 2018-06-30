#!/usr/bin/python
import spidev
import max6675
from time import sleep
import RPi.GPIO as GPIO
import boto3
import time
from datetime import datetime, timedelta

clock_pin = 26
cs_pin = 19
data_pin = 13
units = "f"
currentValue=0.0

client = boto3.client('cloudwatch')

def sendMetrics(value):
    response = client.put_metric_data(
 	Namespace='smoker',
    	MetricData=[
            {
                'MetricName': 'tempf',
                #'Dimensions': [
                #    {
                #        'Name': 'tempf',
                #        'Value': str(value)
                #    },
                #],
                'Timestamp': datetime.utcnow(),
                'Value': float(value),
                'Unit': 'None',
                'StorageResolution': 1
            },
        ]
    ) 

while True:
    sensor_0_0 = max6675.MAX6675(cs_pin, clock_pin, data_pin, units)
    currentValue = sensor_0_0.get()
    print currentValue
    sendMetrics(currentValue)
    sleep(2)


