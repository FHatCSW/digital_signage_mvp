# Digital Signage App

## Overview

**Digital Signage** is a Flask-based web application designed to provide an interactive display for our Campus digital signage. It allows users to navigate through multiple pages with buttons, showcase embedded content via iframes, and provide access to various sections such as Events, News, About Us, Services, and more. Social media links with QR codes and a sitemap are also integrated for enhanced usability.

## Features

- **Multi-page navigation**: Navigate through various pages.
- **Embedded content**: Some pages display external websites via iframes.
- **Social media**: LinkedIn and Instagram buttons open modals displaying QR codes for easy access.
- **Sitemap**: A sitemap is available to explore the site structure.

## Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Templating**: Jinja2
- **Icons**: Font Awesome

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.x installed
- Virtual environment tools such as `venv`

### Clone the Repository

Clone the project from the repository:

```bash
git clone https://github.com/FHatCSW/digital_signage_mvp.git
cd digital-signage_mvp
```

### Set up a Virtual Environment
Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate 
```

### Install Dependencies
Install all required dependencies by running:

```bash
pip install -r requirements.txt
```

### Running the App
Run the app with the following command:

```
python app.py
```
