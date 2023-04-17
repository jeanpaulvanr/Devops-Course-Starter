# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## Project Requirements

### Create a Trello Account and API Key

We're going to be using Trello's API to fetch and save our To Do app's tasks. 

In order to call their
API, you need to first [create an account](https://trello.com/signup), then generate an API key and token by following the instructions [here](https://trello.com/app-key).

Make sure you make a note of these. We will need them again shortly.

### Our To Do App's Trello Board ID

Now you've set up an account and signed in, go ahead and create a new board.

Name the board 'To_Do_App'.

Select the board and in the browser, inspect the url.
It should look similar to https://trello.com/b/sb0NVnTP/todoapp
But not identical. 

You need to take note of the sub-directory before the 'todoapp' sub-directory in the url.  In the example above, this would be sb0NVnTP

This is your board id. Note it down as we will need it later on in our set up.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

Remember I asked you to take a note of the API key, Token and Board ID in the Project Requirements section above? Well, now we're going to need them.

Locate the .env file you've just created in the root directory.

Open it and located the #Trello section.

Enter your values  as follows:

```
#Trello
API_KEY=your-api-key-pasted-here-instead
API_TOKEN=your-api-token-pasted-here-instead
BOARD_ID=your-board-id-pasted-here-instead
```
Save and close the file.
## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.


## Testing the App
### Unit or Integration Testing

To run the Unit or Integration Tests on their own:

```bash
$ poetry run pytest <filepath> 
```
### Running All Tests

To run the all the tests together:

```bash
$ poetry run pytest 
```

## Provision a New Virtual Machine to Host Your To-Do App

### Prerequisites

You will need:

A Control Node: any machine with Ansible installed.

A Managed Node(s): the servers you manage with Ansible.

### Preparing Your Inventory File

Open the file: todoapp-ansible-inventory

Remove any existing IPs and add the IP (or IPs) of the managed node(s) underneath the [webservers] section:

```
[webservers]
18.132.144.249
```
Save and close.

### Preparing Your Control Node

Copy the following files to a directory on your Control Node:

```

todoapp-ansible-inventory

todoapp-ansible-playbook.yml

```
### Running the Playbook

On the control node, navigate to the directory you copied the files above to.

Run the following command:

```
ansible-playbook todoapp-ansible-playbook.yml -i todoapp-ansible-inventory
```
The app should now be accessible from your remote nodes!

Test it by opening a browser and entering:

```
host_ip:5000
```

You should see the To Do App

## Using Docker to Run Your To-Do App 


### Step 1: Install Docker
If you haven't already, you'll need to install [Docker Desktop](https://www.docker.com/products/docker-desktop/). Installation instructions for Windows can be found [here](https://docs.docker.com/desktop/install/windows-install/). If prompted to choose between using Linux orWindows containers during setup, make sure you choose Linux containers.

### Step 2: Build the Containers

With Docker installed on you local environment, you can now build both a development and a production container by running the following commands from a bash terminal.
Ensure you are in the Devops Course Starter directory.

```
$ docker build --target development --tag todo-app:dev .
$ docker build --target production --tag todo-app:prod .
$ docker build --target test --tag todo-app:test .
```

### Step 3: Run the Containers

With the containers built, you can now run them with the following commands:

### Production
```
$ docker run --env-file .env -p 5000:5000 todo-app:prod
```

### Development
```
$ docker run --env-file ./.env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/opt/todoapp/todo_app todo-app:dev
```
### Test

$ docker run todo-app:test

### Step 4: Test the To-Do App is working

Irrespective of whether you've run the development or production container, navigate to [here](http:\\localhost:5000)

You should see your app and be able to use it.

## Steps to Migrate the Application into Microsoft Azure

### Step 1: Set up a Microsoft Azure Account

### Step 2: Creat a Resource Group (to run your app in)

### Step 3: Create a Resource -> Web App

In the “Publish” field, select “Docker Container”

Choose an appropriate “App Service Plan”

Select "Docker Hub" in the "Image Source" field. Enter the details of the image hosted on Docker Hub:

```
jeanpaulvanr/todoapp:jp
```

### Step 4: Set up environment variables (Settings/Configuration - New Application Setting)
NB By default, App Services assume your app is listening on either port 80 or 8080. Set the WEBSITES_PORT app setting to match your container’s behaviour.

### Step 5: Start your app.

Your app should now be visible under the domain you specified. Example provided below:

```
https://jp-todoapp.azurewebsites.net/
```

#### End of ReadMe