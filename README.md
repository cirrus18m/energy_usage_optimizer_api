# energy_usage_optimizer_api
Suggests when to use energy hungry applications like heat pumps for multiple days in advance. 

## Getting started

### Installation

* On Windows please do once: Activate scripts by running in powershell as admin:
    
    ```
    Set-ExecutionPolicy Unrestricted
    ``` 
When asked: "Möchten Sie die Ausführungsrichtline ändern": nein


* Create virtual environment 

    ```
    python3 -m venv .venv
    ```

* Activate environment 

    * Windows

        ```
        .\.venv\Scripts\activate
        ```
    
    * Linux
    
        ```
        . .venv/bin/activate
        ```


* Install packages into environment

    ```
    pip install .
    ```

### Start API 

* start the uvicorn server, which runs the API

    ```
    uvicorn main:app --reload --port=8000 --host=0.0.0.0
    ```

## Build container and run it with hot reloading

* in development mode including hot reloading:

    ```
    sudo docker-compose up --build
    ```
