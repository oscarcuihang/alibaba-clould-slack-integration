# -*- coding: utf-8 -*-
import logging
import requests
import json
import time

WEBHOOK = 'your slack webhook url here'
COLOR_RED = '#fd0000'
COLOR_GREEN = '#74DB12'

def handler(event, context):
  evt = json.loads(event)
  level = evt.get("level")
  color = COLOR_GREEN
  check_mark = ':heavy_check_mark:'
  face_emoji = ':information_source:'

  if (level == 'CRITICAL'):
    color = COLOR_RED
    face_emoji = ':skull_and_crossbones:'
    check_mark = ':x:'

  instance_name = evt.get("instanceName")
  name = evt.get("name")
  status = evt.get("status")

  content = evt.get("content")
  start_time = content.get("startTime")
  cause = content.get("cause")
  description = content.get("description")
  end_time = content.get("endTime")
  total_capacity = content.get("totalCapacity")
  expect_num = content.get("expectNum")

  ali_url = 'your ali cloud account url here'
  headers = {'Content-type': 'application/json'}

  payload = {
    "attachments": [
      {
        "text": 'Ali Alert',
        "color": color,

        "fields": [
          {
            "title": "Instance",
            "value": instance_name,
            "short": True
          },
          {
            "title": "Status",
            "value": check_mark + '  ' + status,
            "short": True
          },
          {
            "title": "Level",
            "value": face_emoji + '  ' + level,
            "short": True
          },
          {
            "title": "Alarm",
            "value": name,
            "short": True
          },
          {
            "title": "Total Capacity",
            "value": total_capacity,
            "short": True
          },
          {
            "title": "Expect Number",
            "value": expect_num,
            "short": True
          },
          {
            "title": "Description",
            "value": description,
            "short": False
          },
          {
            "title": "Cause",
            "value": cause,
            "short": False
          },
          {
            "title": "Started",
            "value": start_time,
            "short": True
          },
          {
            "title": "Ended",
            "value": end_time,
            "short": True
          }
        ],

        "footer": 'Ali Cloud',
        "footer_icon": 'your footer icon url here',
        "ts": int(time.time()),
        "actions": [
          {
            "text": "View in Ali Cloud",
            "type": "button",
            "url": ali_url
          }
        ]
      }
    ]
  }

  r = requests.post(WEBHOOK, headers=headers, data=json.dumps(payload))
  
  return 'ok'