#!/usr/bin/env python
import datetime
import names
import socket

me = socket.getfqdn()


while True:
  now = datetime.datetime.now()
  curr_time = now.isoformat()
  name = names.get_full_name()
  print("[INFO]: Logging from " + me + " at " + curr_time + " for " + name)


