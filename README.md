# **Word Counting App with Django on AWS**

## 📌 **Overview**

The **Word Counting App** is a web-based application developed using **Django**, designed to count the number of words in a given text. The application is deployed on **AWS EC2**, utilizing **PuTTY** for secure SSH access to the cloud instance. This project provides practical experience with **Django web development** and **cloud deployment** on **AWS**.

## ✨ **Features**

- **Text Input**: Users can input text through a simple web form.
- **Word Count Calculation**: The app calculates and displays the total word count of the entered text.
- **Web Interface**: A clean and straightforward user interface built with Django templates.
- **Cloud Deployment**: Hosted on an **AWS EC2** instance for public access.
- **Secure Access**: SSH access to the EC2 instance via **PuTTY**.
- **Persistent Setup**: Ensures that all configuration changes and app setups are saved and easily reproducible.

## 🧱 **Architecture**

### Django Project Structure:
- `wordCountApp`: The main application directory that houses settings and configurations.
- `wordcount`: Contains the core logic for the word counting functionality.
  
### AWS EC2:
- The cloud-based server hosting the Django application.

### PuTTY:
- Used for secure SSH access to the EC2 instance.

### Ubuntu:
- The operating system installed on the EC2 instance.

## 🖥 **Installation and Setup**

### 1. **Launch an EC2 Instance on AWS**
- Choose an **Ubuntu AMI**.
- Configure SSH access and security rules (open port 22 for SSH and port 8000 for HTTP).
- Create a new key pair with the `.ppk` file format for SSH access.

### 2. **Connect to EC2 Using PuTTY**
- Use **PuTTY** to connect to the EC2 instance with the public DNS and the key pair you created:
  ```bash
  ubuntu@<your-ec2-public-dns>

### 3. **Install Required Software**
- SSH into your EC2 instance and install Python and Django:

sudo apt update
sudo apt install python3
sudo apt install python3-pip
sudo pip3 install Django

### 4. **Set Up the Django Project**
- On the EC2 instance, create the project directory and initialize the Django project:

mkdir ~/wordCountApp
cd ~/wordCountApp
django-admin startproject wordCountApp
python3 manage.py startapp wordcount

- Modify settings.py to include the new app and configure the allowed hosts:

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '<your-ec2-public-dns>', '0.0.0.0']

### 5. **Set Up the Django Project**
- Start the Django development server:

python3 manage.py runserver 0.0.0.0:8000

### 6. **Access the Application**
- Open a web browser and navigate to:

http://<your-ec2-public-dns>:8000

## 📝 **Example Usage**
- Text Input: Enter any text in the input field.
- Word Count Output: The application will process the input and display the word count.

## 🧰 **Requirements**
- **Python 3**: The backend of the app is built with Python 3.
- **Django**: A high-level Python web framework for building the web application.
- **AWS EC2**: Used for hosting the application on the cloud.
- **PuTTY**: For secure SSH access to the EC2 instance.
- **Ubuntu**: The operating system installed on the EC2 instance.

## 📊 **Configuration Details**
### Key Files:
`wordCountApp/settings.py`: Contains configuration for the Django app, including allowed hosts and installed apps.
`wordcount/views.py`: Contains the view logic for the word counting functionality.
`wordcount/templates/wordcount/wordcount.html`: The HTML form for inputting text.
`wordcount/templates/wordcount/result.html`: Displays the result of the word count.

### AWS Configuration:
`Security Groups`: Ensure the correct ports (22 for SSH and 8000 for HTTP) are open for access.
`Instance Type`: A small EC2 instance should suffice for the basic requirements of this app.

### 📄 License
This project is for educational purposes and is shared as part of a student project. It is open-source and can be freely used, modified, and distributed.

## 👥 Team Members

- [@x3rtioN](https://github.com/x3rtioN)
- [@Engin-Yedirmez](https://github.com/Engin-Yedirmez)