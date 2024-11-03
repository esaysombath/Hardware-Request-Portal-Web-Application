  # Hardware Request Management Project

## Description
The Hardware Request Management System is a web-based application designed to enhance hardware inventory management in a mechanic workshop. As a kitting clerk at a manufacturing company using the outdated 2012 Microsoft Dynamics AX ERP system, I've faced significant challenges in managing hardware requests and inventory across multiple locations.

In our workshop, mechanics work in ten distinct areas, each with hardware bin towers containing up to 100 items that require regular refill monitoring. Currently, kitting clerks print sheets detailing item locations, check each bin manually, retrieve hardware from separate locations, and handwrite labels for each item, including its quantity, batch number, and tower location. This labor-intensive process is time-consuming and prone to errors, leading to delays in tool availability and decreased productivity.

To tackle these issues, I developed the Hardware Request Management System, enabling mechanics to submit tool and equipment requests easily through a user-friendly interface. The admin panel facilitates efficient request management, allowing administrators to view and update statuses and receive email notifications for new submissions. This project highlights my skills in web development, database management, and email integration, significantly improving our workshop's workflow.

## Table of Contents
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Contact Information](#contact-information)
- [Screenshots/Demos](#screenshotsdemos)

## Installation Instructions
To set up the Hardware Request Management System locally, follow these steps:

1. **Clone the repository**: 
   Open your terminal and run the following command to clone the project repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/hardware-request-management.git
   ```

2. **Navigate to the project directory**: 
   Change your working directory to the project folder:
   ```bash
   cd hardware-request-management
   ```

3. **Install the required dependencies**: 
   This project uses several Python packages. Install them using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**: 
   Initialize the SQLite database that will store the request data:
   ```bash
   python create_db.py
   ```

5. **Run the application**: 
   Start the Flask web server to launch the application:
   ```bash
   python app.py
   ```

6. **Access the application**: 
   Open your web browser and navigate to `http://127.0.0.1:5000` to access the Hardware Request Management System.

## Usage
Once the application is running, you can use it as follows:

- **Submitting a hardware request**: Mechanics can access the request form from the homepage, fill in the necessary details such as their name, hardware item, quantity requested, and the location where they need it to be refilled, and submit the request for processing.
  
- **Admin functionalities**: Administrators can log in to the admin panel to view all submitted requests, update their statuses (e.g., "Pending", "Approved", "Denied"), and receive email notifications for any new requests that come in.

### Example Code
Here’s a snippet demonstrating how a mechanic might submit a request:
```python
# Route for home page to submit a request
@app.route('/', methods=['GET', 'POST'])
def submit_request():
    if request.method == 'POST':
        # Capture form data
        mechanic_name = request.form['mechanic_name']
        hardware_item = request.form['hardware_item']
        quantity = request.form['quantity']
        location = request.form['location']
        request_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
```

## Features
The Hardware Request Management System includes several key features:
- **User-friendly interface**: The application is designed with mechanics in mind, ensuring an intuitive experience when submitting requests.
- **Admin dashboard**: A dedicated space for administrators to manage and oversee all hardware requests, complete with options to update statuses and manage notifications.
- **Email notifications**: Administrators receive timely alerts when new requests are submitted, ensuring that no request is overlooked.
- **SQLite database integration**: The application uses SQLite for efficient data storage and management, allowing for quick access and updates to request records.

## Technologies Used
The following technologies were utilized in the development of this project:
- **Python**: The programming language used to develop the application logic.
- **Flask**: A lightweight web framework for Python that facilitates the creation of web applications.
- **SQLite**: A simple, serverless database engine used for data storage.
- **HTML/CSS**: Standard technologies for creating and styling web pages.
- **JavaScript**: Used to enhance interactivity on the front end.
- **Bootstrap**: A front-end framework that helps design responsive and visually appealing web applications.

## Contact Information
For inquiries, collaboration opportunities, or further information about this project, please feel free to contact me:
- Email: esaysombath@gmail.com
- LinkedIn [Elbie Saysombath Profile](https://www.linkedin.com/in/elbie-s/)

## Screenshots & Demo
Explore the main features of the Hardware Request Management System through the screenshots and demo video below.

### Admin Portal
The Admin Portal allows administrators to manage requests, track statuses, and view details in a streamlined interface.
<img src="https://github.com/user-attachments/assets/a9b45e86-7624-4a09-a48d-b1431e61bd3b" alt="Admin Portal" width="500px">

### Request Form
The Request Form lets mechanics submit hardware requests easily, ensuring clear communication with the kitting team.
<img src="https://github.com/user-attachments/assets/905e415e-80b0-44e2-b871-3a07ac9e501d" alt="Request Form" width="500px">

### Demo Video
Watch this video to see the system in action:
<a href="https://youtu.be/vvfwtcKblw8">
    <img src="https://github.com/user-attachments/assets/e1cdd1ea-f50b-4fa9-9745-68e699687770" alt="Demo Screenshot" width="500px">
</a>

[![Demo Screenshot](https://github.com/user-attachments/assets/e1cdd1ea-f50b-4fa9-9745-68e699687770)](https://youtu.be/vvfwtcKblw8)
[![Demo Video](https://youtu.be/vvfwtcKblw8)]
![THUMBNAIL](https://github.com/user-attachments/assets/e1cdd1ea-f50b-4fa9-9745-68e699687770)
