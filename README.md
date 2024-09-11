# **Security Picker Website**

## **Overview**

This project aims to develop a simple website using docker to create containers for each of the key components. The website will display a set of possible securities on which to find more information about them.

## **Project Structure**
```plaintext
Security_Picker_Website/
│
├── mongo-express/                  # Used for debugging purposes
│   └── .env                        # Defines environmental variables for mongo-express
│       
├── mongodb/                        # Used as a database for the backend
│   └── .env                        # Defines environmental variables for mongodb
│       
├── security_picker_app/            # Used to define the security_picker_app_image and it execution
│   ├── src/                        # Stores src for the security_picker_app
│   │   └── app/                    # Stores all executable code
│   │        ├── main.py            # Defines the main operation of the security picker app
│   │        └── templates/         # Stores all static contents for the app
│   │            └── index.html     # HTML for the index page
│   │
│   ├── .env                        # Defines environmental variables for security_picker_app
│   ├── Dockerfile                  # Specifies how the docker should create the security_picker_app_image
│   ├── pyproject.toml              # Used to setup security_picker_app wheel
│   └── requirements.txt            # stores the installment requirements for Docker to install
│
├── .gitignore                      # Indicates the files that should be ignored by git
├── docker-compose.yml              # Specifies how "docker compose up" should run
├── LICENSE                         # The project's license
└── README.md                       # Project overview and setup instructions
```

## **License**
This project is licensed under the MIT License. See the LICENSE file for more details.
