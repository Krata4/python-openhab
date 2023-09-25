#!/usr/bin/env python3

"""Tries to connect to OpenHAB and fetch items. Loop until successful."""

import json
import time

import httpx

base_url = 'http://localhost:8080/rest'

while True:
  try:
    req = httpx.get(base_url + '/items')
    items = req.json()
  except (httpx.RequestError, json.JSONDecodeError) as exc:
    print(str(exc))
  else:
    if req.status_code == 200:
      break

  time.sleep(0.5)
