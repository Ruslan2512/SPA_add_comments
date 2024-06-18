# Django Comments Application

This is a Django application that allows users to add comments with optional image or text file attachments. The application includes features like CAPTCHA validation, file upload handling, XSS protection, and pagination.

## Features

1. **Add Comments**: Users can add comments with optional image or text file attachments.
2. **File Uploads**: Supported image formats are JPG, GIF, and PNG with automatic resizing to 320x240 pixels if the image is larger. Supported text file format is TXT with a maximum size of 100 KB.
3. **CAPTCHA Validation**: CAPTCHA to ensure the user is human.
4. **HTML Tags Support**: Users can use specific HTML tags in their comments.
5. **Pagination**: Comments are paginated with 25 comments per page.
6. **Sorting**: Comments can be sorted by user name, email, and date.
7. **XSS and SQL Injection Protection**: The application is protected against common web vulnerabilities.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Ruslan2512/SPA_add_comments.git
    cd comments_project
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv myenv
    source myenv/bin/activate   (On Windows: `myenv\Scripts\activate`)
    ```
   To Poetry:
    ```bash
    pip install poetry (poetry environment install);
    poetry new myproject (create you poetry venv);
    poetry shell (activate poetry).
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your browser and go to `http://127.0.0.1:8000`.

## Usage

1. **Add a Comment**:
    - Go to the comments page.
    - Click on "Add Comment".
    - Fill out the form and optionally upload an image or a text file.
    - Complete the CAPTCHA.
    - Submit the form.

2. **Sorting and Pagination**:
    - Comments can be sorted by user_name, email, and date.
    - Use the pagination controls to navigate through pages.

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
