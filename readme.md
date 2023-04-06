## Book's Service

### Introduction

This backend service exposes its functionality to frontend clients via API endpoints listed below.

### Installation Guide

- Clone this repository [here](https://github.com/WawinyEdwin/wezacare-challenge.git).
- The `main` branch is the most stable branch at any given time, ensure you're working from it.
- Run `pip install -r requirements.txt` to install dependencies.
- Once the packages are installed preferably on a virtual env( can be created through `python -m venv venv`)

### Usage

- Run `flask run` to start the application.
- Connect to the API using Postman or a web/mobile client on port 8001.
- To get you started in the `/utils` directory we have a `sample_data.json` containing some sample data.

### API Endpoints

| HTTP Verbs | Endpoints        | Action                    |
| ---------- | ---------------- | ------------------------- |
| GET        | /books           | To retrieve all books     |
| POST       | /books           | To create a book          |
| GET        | /books/<book_id> | To retrieve a single book |
| PUT        | /books/<book_id> | To update a single book   |
| DELETE     | /books/<book_id> | To delete a book          |

---

### Technologies Used

- [Python](https://nodejs.org/) is a programming language that lets you work more quickly and integrate your systems
  more effectively.
- [Flask](https://flask.palletsprojects.com/en/2.2.x/) Flask is a web framework that provides libraries to build lightweight web applications in python
- [SQLite](https://www.sqlite.org/) SQLite is an in-process library that implements a self-contained, serverless,
  zero-configuration, transactional SQL database engine
