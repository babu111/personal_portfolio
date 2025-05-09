# Personal Portfolio Website

A beautiful, responsive personal portfolio website built with Flask, featuring a modern UI and comprehensive sections to showcase your professional skills, projects, and contact information.

## Features

- Modern, responsive design
- Home page with hero section, skills, and featured projects
- Detailed About page with personal information, experience timeline, and testimonials
- Projects page with filtering capability
- Contact page with form validation and Google Maps integration
- Smooth animations and interactions

## Demo

![Portfolio Demo](https://via.placeholder.com/800x400)

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Heroku (optional)
- **Dependencies**: See requirements.txt

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/portfolio-website.git
   cd portfolio-website
   ```

2. Create a virtual environment (recommended)
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application
   ```bash
   python app.py
   ```

6. Open your browser and navigate to
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
portfolio-website/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
│
├── static/                # Static files
│   ├── css/               # CSS stylesheets
│   ├── js/                # JavaScript files
│   └── images/            # Image files
│
└── templates/             # HTML templates
    ├── base.html          # Base template with common elements
    ├── index.html         # Home page
    ├── about.html         # About page
    ├── projects.html      # Projects showcase
    └── contact.html       # Contact page
```

## Customization

1. **Personal Information**: Update your personal information in the HTML templates.
2. **Projects**: Add your own projects in the projects.html file.
3. **Styling**: Modify the CSS in static/css/style.css to match your preferences.
4. **Images**: Replace placeholder images with your own in the static/images directory.

## Deployment

### Heroku Deployment

1. Create a Heroku account and install the Heroku CLI
2. Create a Procfile in the root directory:
   ```
   web: gunicorn app:app
   ```
3. Add gunicorn to requirements.txt
4. Deploy to Heroku:
   ```bash
   heroku login
   heroku create your-portfolio-name
   git push heroku main
   ```

### Other Deployment Options

- GitHub Pages (static export)
- Netlify
- Vercel

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Font Awesome for the icons
- Google Fonts for the typography
- Unsplash for placeholder images

---

Created with ❤️ by [babu111](https://github.com/babu111) 