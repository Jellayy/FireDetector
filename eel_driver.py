import eel
import vision


@eel.expose
def detect_fire():
    main.code()


eel.init('.', allowed_extensions=['.js', '.html'])
eel.start('main.html', size=(300, 300))
