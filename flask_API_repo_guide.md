<h2>A guide to creating a Flask API project from a sample project</h2>





1. Create a new GitHub repo with the flask API repo as a template as follows:

   - Go to https://github.com/gcallah/flask-api

   - Click on *Use this template* option

   - Choose your *Repository name* 

   - Select *Public* or *Private* option, depending on whether you want your repo to be visible to everyone or not

   - Select *Include all branches* option.

2. Clone the repository to your computer as follows:

   - Click on *Code*
   - Choose either *HTTPS*, *SSH*, or *GitHub CLI* 
     	- *HTTPS* option is the simplest, you just need to generate the *Personal access token*
     	- To generate a token go to *Settings* -> *Developer settings* -> *Personal access token* -> *Generate new token*
     	- Copy the generated token and save it somewhere. You won't be able to retrieve it from GitHub in the future and will need to generate a new token if you lose this one.
     	- You'll need to use your access token in place of GitHub password 
     	- Run ```git clone your_repo_link``` command from your shell
     	- Further GitHub setup steps might need to be taken depending on your Operating System and existing configurations. Google the errors you are getting, often you'll find the answer very quickly in this way. 

3. Once you've cloned the repo do the following:

   - Run ```make dev_env```, this will install some project dependencies on your computer 
   - Make sure that all the dependencies were installed successfully without any errors. To see the list of dependencies you can refer to ```requirements.txt``` and ```requirements-dev.txt``` files
   - To test the setup ```cd``` into ```API``` directory and run ```./local.sh``` command from your shell 
   - You should see a message saying *Running on http://127.0.0.1:8000/*
   - Open the given URL in your browser, there you should see a swagger interface with some basic endpoints
   - Click on *default* option and select *hello* endpoint. Click on *Try it out* -> *Execute*
   - At this point you should see a message saying "hello world" being returned to you in the repose body with the repose code 200
   - To stop the server type ```control + c``` in your shell. 

