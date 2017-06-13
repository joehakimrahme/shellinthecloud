import os

from blogstrap import create_app

BASE = os.path.dirname(os.path.abspath(__file__))
config = lambda x: os.path.join(BASE, x)

application = create_app(config('blogstrap.conf'))

if __name__ == '__main__':
    application.run()
