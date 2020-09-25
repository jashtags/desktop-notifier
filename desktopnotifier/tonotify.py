import time
import notify2
from desktopnotifier import shouldimportthis

path="Users⁩/jashwanth⁩/⁨Desktop⁩"
newsitems=shouldimportthis()
notify2.init("notifier online")
nobj=notify2.Notification(None,icon=path)
nobj.set_urgency(notify2.URGENCY_NORMAL)
n.set_timeout(50000)
for news in newsitems:
    n.update(newsitems['title'],newsitems['description'])
    n.show()
    time.sleep(15)
