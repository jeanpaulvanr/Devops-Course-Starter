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

You'll then need to run 'poetry add requests' (as it's not currently tracked by Poetry):

```bash
$ poetry add requests  # (first time only)
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

### How to Set Up for Testing

You need to add pytest as a dependency of our project.

```bash
$ poetry add pytest --dev
```
This should download it and also update pyproject.toml for you.

You can now run either the Unit Tests or the Integration Tests or both. Please see below.

### Unit Testing

To run the Unit Tests on their own:

```bash
$ poetry run pytest todo_app\data\test_view_model.py 
```
Note: Ensure your terminal is in the root todo_app directory!

You should see output similar to the following:

```bash
(.venv) C:\DevOps\DevOps-Course-Starter>poetry run pytest todo_app\data\test_view_model.py
============================================================== test session starts ===============================================================
platform win32 -- Python 3.10.5, pytest-7.1.3, pluggy-1.0.0
rootdir: C:\DevOps\DevOps-Course-Starter
collected 3 items

todo_app\data\test_view_model.py ...                                                                                                        [100%] 

=============================================================== 3 passed in 0.11s ================================================================ 
```

### Integration Testing

To run the Integration Tests on their own:

```bash
$ poetry run pytest todo_app\data\test_client.py 
```

Note: Ensure your terminal is in the root todo_app directory!

You should see output similar to the following:

```bash
(.venv) C:\DevOps\DevOps-Course-Starter>poetry run pytest todo_app\data\test_client.py    
============================================================== test session starts ===============================================================
platform win32 -- Python 3.10.5, pytest-7.1.3, pluggy-1.0.0
rootdir: C:\DevOps\DevOps-Course-Starter
collected 1 item

todo_app\data\test_client.py .                                                                                                              [100%]

=============================================================== 1 passed in 1.22s ================================================================ 
```

### Running All Tests

To run the all the tests together:

```bash
$ poetry run pytest 
```

Note: Ensure your terminal is in the root todo_app directory!

You should see output similar to the following:

```bash
(.venv) C:\DevOps\DevOps-Course-Starter>poetry run pytest
============================================================== test session starts ===============================================================
platform win32 -- Python 3.10.5, pytest-7.1.3, pluggy-1.0.0
rootdir: C:\DevOps\DevOps-Course-Starter
collected 4 items

todo_app\data\test_client.py .                                                                                                              [ 25%]
todo_app\data\test_view_model.py ...                                                                                                        [100%] 

=============================================================== 4 passed in 0.63s ================================================================ 
```
#### End of ReadMe