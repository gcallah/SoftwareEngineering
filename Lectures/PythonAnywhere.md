# Deploying to Python Anywhere

1. Create an account at [Python Anywhere](https://www.pythonanywhere.com/)
1. Clone your repo
1. [Create a virtual environment](https://help.pythonanywhere.com/pages/VirtualEnvForWebsites)
1. Install packages in your virtual env using `pip` and `requirements.txt`
1. Create a Web app using the Web dashboard (choose 'Manual Configuration')
1. Set virtual env in Web dashboard
1. Set up WSGI file: add your MongoDB password and set CLOUD_MONGO=1 (Sample WSGI below!)
1. Try your server
1. Read the error log file if it doesn’t work
1. Fix problems
1. Try your server

Not necessary? 1. [Create SSH key](https://help.pythonanywhere.com/pages/ExternalVCS/)

Not necessary? 1. Install public SSH key on GitHub Not necessary?

# Autodeploy through GitHub Actions
1. Make sure your "Deploy to PythonAnywhere" code in `.github/workflows/main.yml` is **not** commented out!
1. Install the PythonAnywhere (PA) helper scripts from your PA console: `pip3.10 install --user pythonanywhere`
1. From the `Account` tab create a API Key. Copy it!
1. Enter the key in your `.bashrc` in a PythonAnywhere console. (`export API_TOKEN=<YOUR_KEY>`)
1. Setup ssh access to your PythonAnywhere account; instructions here: https://help.pythonanywhere.com/pages/SSHAccess
1. From now on when you push to GitHub, **if** your tests pass, your server should update automatically.

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


