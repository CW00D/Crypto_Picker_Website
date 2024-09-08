# **Security Picker Website**

## **Overview**

This project aims to develop a simple website using docker to create containers for each of the key components. The website will display a set of possible securities on which to find more information about them.

## **Project Structure**
```plaintext
Crypto_Picker_Website/
├── backend/                   #
│   ├── src/                   #
│   │   └── mysite/            #
│   │       ├── __init__.py    # 
│   │       └── main.py        # 
│   ├── .env                   # 
│   ├── Dockerfile             #
│   ├── pyproject.toml         #
│   └── requirements.txt       #
│
├── frontend/                  #
│   ├── static/                # 
│   │   └── mysite/            #
│   └── Dockerfile             #
│
├── mongo-express/             #
│   └── .env                   # 
│
├── mongodb/                   #
│   └── .env                   #
│
├── .gitignore                 # 
├── docker-compose.yml         # 
├── LICENSE                    #
└── README.md                  # Project overview and setup instructions
```

## **License**
This project is licensed under the MIT License. See the LICENSE file for more details.
