# Deploying to Python Anywhere

1. Create an account at [Python Amywhere](https://www.pythonanywhere.com/)
1. [Create SSH key](https://help.pythonanywhere.com/pages/ExternalVCS/)
1. Install public SSH key on GitHub
1. Clone your repo
1. [Create a virtual environment](https://help.pythonanywhere.com/pages/Virtualenvs/)
1. Create a Web app using the Web dashboard (choose 'Manual Configuration')
1. Set virtual env in Web dashboard
1. Install packages in your virtual env using `pip`
1. Set up WSGI file: add your MongoDB password and set CLOUD_MONGO=1 (Sample WSGI below!)
1. Try your server
1. Read the error log file if it doesn’t work
1. Fix problems
1. Try your server


## Sample WSGI file:

```
# +++++++++++ FLASK +++++++++++
import sys
import os

# YOUR_PASSWORD_VARIABLE will be something like `MONGO_PASSWORD`!
os.environ['YOUR_PASSWORD_VARIABLE'] = 'your-password'
os.environ['CLOUD_MONGO'] = '1'

path = '/home/YOUR_PA_ACCOUNT_NAME/YOUR_REPO_NAME'
if path not in sys.path:
    sys.path.append(path)

from server.endpoints import app as application  # noqa
```


