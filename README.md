# Natural SQL
This tool empowers individuals to perform queries on databases through natural language processing (NLP). 
It only requires a SQL URL to execute any query and get the results in natural languaje.

Our application is in a trial phase, exploring the capabilities of Large Language Models in conducting SQL database queries via Langchain's SQL Agents. It necessitates possession of an OPENAI_API_KEY for operation.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
* Python 3.9
* Open AI API Key
* SQL URL database

### Installing

A step by step series of examples that tell you how to get a development env running

Clone the repository:
``` bash
git clone https://github.com/TierOneOS/natural-sql.git
```

Install dependencies:
``` python
pip install -r requirements.txt
```

### Running Locally

To run the application locally, execute: \
``` python
python main.py
```

This will start a Uvicorn server hosting the application on `http://localhost:3000`.

### Running with Docker

To run the application using Docker, you need to build the Docker image and then run a container based on it.

Build the Docker image:
``` bash
docker build -t natural-sql .
```

Run the Docker container:
``` bash
docker run -p 3000:3000 natural-sql
```

This will start a Uvicorn server inside a Docker container, which will be accessible on `http://localhost:3000`.


## Authors

* **Mariano Ravinale**  - [GitHub](https://github.com/mravinale)

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details

