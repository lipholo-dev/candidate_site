# candidate_site

## Setup Instructions

1. **Install dependencies**:
   - Create a virtual environment and activate it:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On MacOS/Linux
     venv\Scripts\activate  # On Windows
     ```

   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the Application**:
   - Run the Django server:
     ```bash
     python manage.py runserver
     ```

3. **Docker Setup**:
   - Build the Docker image:
     ```bash
     docker build -t your_project_name .
     ```

   - Run the Docker container:
     ```bash
     docker run -p 8000:8000 your_project_name
     ```

4. **Environment Variables**:
   - Ensure you set up any necessary environment variables, such as database credentials, as needed.

5. **Sensitive Information**:
   - Do not include sensitive information like passwords in this repository. Follow the instructions to acquire and set them up yourself.
