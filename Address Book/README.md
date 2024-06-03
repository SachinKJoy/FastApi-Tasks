
This is a simple FastAPI application for managing Address Book. It provides endpoints for creating,updating and deleting addresses as well as retrieving addresses based on given distance.

## Setup

1. Clone the repository:

 - git clone https://github.com/SachinKJoy/FastApi-Tasks


2. Open a Powershell terminal and create a virtual environment to run your application and download dependencies 

    - Run  "python -m venv venv" to create a virtual env named "venv"

    - then run "venv/Scripts/activate" to activate


3. Install dependencies using pip:

    pip install -r requirements.txt


4. Run the FastAPI application:
  
   uvicorn main:app --reload  


5. Once the server is running, you can access the API documentation at `http://127.0.0.1:8000/docs`. This documentation provides detailed information about the available endpoints and their usage.
