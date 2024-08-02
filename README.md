
# AD TextUitls
## Description
Welcome to the TextUtils Website project! This web application provides a suite of text manipulation tools built with Django. It offers functionality for removing punctuation, removing lines, trimming extra spaces, converting text to uppercase, and counting characters.

## Features


- **Remove Punctuation**: Strips punctuation from the input text.
  
- **Remove Lines:**:Eliminates empty lines from the input text.

- **Remove Extra Spaces**: Trims extra spaces from the input text.

- **Convert to Uppercase**: Converts all text to uppercase.

- **Character Count**: Automatically counts and displays the total number of characters in the input text.
## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x or above
- pip (Python package installer)

### Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/dharayush7/ad-textutils.git
cd ad-textutils
```
#### 2. Create a Virtual Environment

```bash
python -m venv venv
```
#### 3. Activate the Virtual Environment

- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

#### 4. Install the Required Packages

```bash
pip install -r requirements.txt
```

#### 5. Run Migrations
```bash
python manage.py migrate
```
#### 6. Start the Development Server
```bash
python manage.py runserver
```

application will be available at `http://127.0.0.1:8000/`.

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:8000/`.
2. You will see a text area where you can input your text.
3. Use the provided buttons to apply the different text utilities
 - **Remove Punctuation**: Toggle this switch to strip all punctuation from your text
  - **Remove Lines**: Toggle this switch to remove empty lines.
  - **Remove Extra Spaces**: Toggle this switch to trim extra spaces from your text.
  - **Convert to Uppercase**: Toggle this switch to convert your text to uppercase.

4. The **Character Count** is automatically updated with each request, displaying the total number of characters in the input text.
## 🔗 Links
[portfolio](https://www.ayushdhar.com/)



## License

[MIT]

