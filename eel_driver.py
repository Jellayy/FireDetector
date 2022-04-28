import eel
import vision


@eel.expose
def detect_fire():
    vision.monitor_feed()


eel.init('ui', allowed_extensions=['.js', '.html'])
eel.start('main.html', size=(300, 300))
