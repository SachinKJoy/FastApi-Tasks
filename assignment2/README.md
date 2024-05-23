# FastAPI Book Review API

This is a simple FastAPI application for managing books and reviews. It provides endpoints for adding books and reviews, as well as retrieving books and reviews based on various criteria.

## Setup

1. Clone the repository:

 - git clone https://github.com/SachinKJoy/FastApiProject.git


2. Navigate into the project directory:
  
  - To run the FastAPI application without any DB integration, go to no_DB folder and run the main file.
        cd /no_DB

  - To run the FastAPI application with SQLlite DB integration, go to src/main.py


3. Open a virtual environment to run your application and download dependencies 

    for Powershell
    - Run  "python -m venv venv" to create a virtual env named "venv"

    - then run "venv/Scripts/activate" to activate


4. Install dependencies using pip:

    pip install -r requirements.txt


5.  Run the FastAPI application:
  
   uvicorn src.main:app --reload


8. Once the server is running, you can access the API documentation at `http://127.0.0.1:8000/docs`. This documentation provides detailed information about the available endpoints and their usage.


3. You can use tools like `curl`, `Postman`, or any HTTP client to interact with the API endpoints.
