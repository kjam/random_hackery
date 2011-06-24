from celery.app import app_or_default
import cPickle
import logging

class EventMonitor(object):

    def __init__(self,app=None):
        self.app = app_or_default()
        self.conn = self.app.broker_connection()
        self.recv = self.app.events.Receiver(self.conn, handlers={"*": self.push_event})
        self.eventList = []
        self.taskEventList = []
        try:
            self.recv.capture()
        except:
            logging.info("Receiver closed...")


    def get_state(self):
        return self.app.events.State()
   

    def push_event(self, event):
        self.eventList.append(event)
        if 'task' in event['type']:
            self.taskEventList.append(event)
            f = open('data/event_queue','wb')
            cPickle.dump(self.taskEventList,f)
            f.close()

def start_monitoring():
    mon = EventMonitor()


if __name__=='__main__':
    mon = EventMonitor()

