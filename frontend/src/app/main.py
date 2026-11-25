import os
import sys
from pathlib import Path

# Add frontend/src to sys.path so 'app.settings' and 'app.urls' resolve
SRC_DIR = Path(__file__).resolve().parent.parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
print(f"Added {SRC_DIR} to sys.path")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
app = application