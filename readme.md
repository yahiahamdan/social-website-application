![Social  application](screenshots/social.png)

 :brain: social application support OAuth 2.0 allow users to share content from other sites in the form of 
 javascript bookmarks  and contain all authentication and authroization features 
## Table of Contents 
- [Features](#features)
- [Installation](#installation)
- [Images](#images)

## Features
* OAuth 2.0 autentication google
* running the development server using HTTPS django.expression
* django build in authentication (login-register-logout)
* create profile Image for users that register 
* reset password /change password
* edit profile 
* JavaScript bookmarklet code that can be executed on any website. This code will find images
across the page and allow users to select the image they want to bookmark and save it in the database 

## Installation
1. **Clone the repository:**
```bash
git clone https://github.com/yahiahamdan/social-website-application.git
```
2. **Navigate to the bookmarks directory:**
```bash
cd bookmarks
```  
3. **Create and activate a virtual environment:**
```bash
    python -m venv env
    .\env\bookmarks\Scripts\activate  # On Windows use `env\Scripts\activate`
 ```
4. **Install the required packages:**
 ```bash
    pip install -r requirements.txt
 ```

5. **Apply migrations:**
```bash
    python manage.py migrate
```
6. **Create a superuser:**
```bash
    python manage.py createsuperuser
```
7. **Run the development server:**
```bash
  python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
```

8. **Open your browser and visit:**
    ```
    https://myapp.com:8000/
    ```
## Images
click [here](./screenshots/) to see all the screenshots of the applications