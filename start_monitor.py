from celerymonitor.service import MonitorService
import logging

logger = logging.getLogger()
m = MonitorService(logger)
m.start()
