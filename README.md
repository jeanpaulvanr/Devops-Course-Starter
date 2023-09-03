# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## Project Requirements

## Part A: Create a MongoDB Database for your Source Data

### Step 1: Set up a Microsoft Azure Account

### Step 2: MongoDB

Create a MongoDB database as a Source for Data

Using the portal, log into Azure and create a new CosmosDB instance:

New → CosmosDB Database

Select "Azure Cosmos DB"

Name: jp_todoapp

Choose "Serverless" for Capacity mode

You can also configure secure firewall connections here, but for now you should permit
access from "All Networks" to enable easier testing of the integration with the app.

```
Encryption at rest for Azure Cosmos DB is implemented by using a number of security technologies, including secure key storage systems, encrypted networks, and cryptographic APIs. There is no additional cost.
```

### Step 3: Collection

Now you've set up a database, go ahead and create a new collection:

Name: jp_todoapp_collection

### Step 4: Posts

Now you've created a collection, you need to add some posts to it to work with as test data...

First copy the “PRIMARY CONNECTION STRING” for your CosmosDB cluster,
available under Settings → Connection String from your CosmosDB account
page in the Azure portal

From a terminal, run the following, substituting in your
connection string:

```
>>> import pymongo
>>> client = pymongo.MongoClient("mongodb://your-cosmoscluster:
abcpassword123==@your-cosmos-cluster.mongo.cosmos.azure.com:10255")
>>> client.list_database_names()
[]
```

Assuming the above runs successfully, create some new posts using the code example below...

```
>>> post = {"item name": "First Item on the List",
        "status": "To Do",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

>>> posts = db.posts
>>> post_id = posts.insert_one(post).inserted_id
```
We have now sucessfully created our source data for the project.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

## Party A: Poetry

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

### Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

Locate the .env file you've just created in the root directory.

Open it and locate the Azure Cosmos DB section.

Enter your values  as follows:

```
#Azure Cosmos DB
CONNECTION_STRING="PRIMARY CONNECTION STRING" (see Step 4 under 'Part A: Create a MongoDB Database for your Source Data')
```
Save and close the file.
## Part B: Running the App

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


## Part C: Testing the App
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

## Part D: Using Docker to Run Your To-Do App 


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
```
$ docker run todo-app:test
```
### Step 4: Test the To-Do App is working

Irrespective of whether you've run the development or production container, navigate to [here](http:\\localhost:5000)

You should see your app and be able to use it.

## Part E: Steps to Migrate the Application into Microsoft Azure

### Preliminary Steps to Build and Push Image to DockerHub:

```
docker build --tag <docker login name>/<app name>:<tag> .
docker push docker.io/<docker login name>/<app name>:<tag>
```
### Step 1: Installations

Install both [Terraform](https://developer.hashicorp.com/terraform/tutorials/azure-get-started/install-cli?in=terraform%2Fazure-get-started) and the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli) locally.

Once installed, login to the Azure portal.

```
az login
```

Then  run...

```
az account list
```

If that command listed more than one Subscription, tell the Azure CLI which to use by running 

```
az account set --subscription="SUBSCRIPTION_ID"
```

### Step 2: Environment Variables

Ensure  the environment variables in terraform.tfvars file are set correctly. Example below:

```
websites_port = 5000
```
### Step 3: Terraform Commands

Run the following commands.
Take note to add your secret key variable value.

```
terraform init
terraform apply -var secret_key=<"secret key">
```

### Step 4: Push Application to Infrastructure

```
curl -dH -X POST "$(terraform output -raw cd_webhook)"
```
### Step 5: Start your Application

Your app should now be visible under the domain specified in the terminal output. Example below:

```
https://jp-todo-app.azurewebsites.net/
```

## Note on Security
### Encryption at Rest

Encryption at rest for Azure Cosmos DB  is implemented by using a number of security technologies, including secure key storage systems, encrypted networks, and cryptographic APIs.

#### End of ReadMe