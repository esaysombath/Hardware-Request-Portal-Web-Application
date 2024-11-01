from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'uhcq blff edwc opna'  # Change this to a secure key in production

# Email notification settings
ADMIN_EMAIL = 'esaysombath@gmail.com'  # Replace with your email
EMAIL_HOST = 'smtp.gmail.com'           # Gmail SMTP server
EMAIL_PORT = 587                        # TLS port
EMAIL_USER = 'esaysombath@gmail.com'
EMAIL_PASS = 'uhcq blff edwc opna'  # Use your app-specific password here

# Function to send email notifications
# Function to send email notifications
def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = ADMIN_EMAIL
    msg['Subject'] = subject
    
    # Format the body text for improved readability
    formatted_body = f"""
    New Hardware Request Submitted

    Mechanic Name: {body['mechanic_name']}
    Hardware Item: {body['hardware_item']}
    Quantity: {body['quantity']}
    Location: {body['location']}
    Date of Request: {body['request_date']}

    Please review this request in the admin portal.
    """
    msg.attach(MIMEText(formatted_body, 'plain'))
    
    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, ADMIN_EMAIL, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", e)


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
        
        # Insert data into the database
        conn = sqlite3.connect('hardware_requests.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO requests (mechanic_name, hardware_item, quantity, request_date, location, status) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (mechanic_name, hardware_item, quantity, request_date, location, 'Pending'))
        conn.commit()
        conn.close()

        # Send email notification
        subject = "New Hardware Request Submitted"
        body = {
            'mechanic_name': mechanic_name,
            'hardware_item': hardware_item,
            'quantity': quantity,
            'location': location,
            'request_date': request_date
        }
        send_email(subject, body)

        # Flash success message and redirect to form
        flash("Request submitted successfully!", "success")
        return redirect(url_for('submit_request'))

    return render_template('index.html')


# Route to view all requests for admins
@app.route('/admin')
def view_requests():
    conn = sqlite3.connect('hardware_requests.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM requests')
    requests = cursor.fetchall()
    conn.close()
    return render_template('requests.html', requests=requests)

# Route to update request status
@app.route('/update/<int:request_id>', methods=['POST'])
def update_status(request_id):
    new_status = request.form['status']
    conn = sqlite3.connect('hardware_requests.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE requests SET status = ? WHERE id = ?', (new_status, request_id))
    conn.commit()
    conn.close()
    flash("Request status updated successfully!", "success")
    return redirect(url_for('view_requests'))

if __name__ == "__main__":
    app.run(debug=True)
