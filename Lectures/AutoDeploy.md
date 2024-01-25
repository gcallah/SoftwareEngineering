# Auto-Deploy to PythonAnywhere

1. Get `deploy.sh` and `rebuild.sh` into your repo from `demo-repo4`.
1. Pull these files to your PA account: `cd <YOUR_REPO_DIR>; git pull origin master`
1. Get PA utils from https://github.com/pythonanywhere/helper_scripts: `pip3.10 install --user pythonanywhere`
1. Get API token from PA Account tab.
1. If you'd like, test `rebuild.sh` separately on PA. (You have to set VENV, PA_DOMAIN, and PA_USER!)
1. Try SSHing into your PA account: https://help.pythonanywhere.com/pages/SSHAccess/ (`ssh Fall2023@ssh.pythonanywhere.com`)
1. 
