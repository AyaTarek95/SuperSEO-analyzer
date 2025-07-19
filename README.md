# Super Simple SEO Analyzer


# SuperSEO Analyzer Frontend

This is the frontend for the SuperSEO Analyzer, providing a user interface for analyzing SEO performance, managing URLs, and extracting keywords.

## Project Structure

```plaintext
.
├── App.js
├── assets
│   ├── brand
│   │   ├── logo.js
│   │   └── sygnet.js
│   └── images
│       ├── angular.jpg
│       ├── avatars
│       ├── icon.png
│       ├── logo.png
│       ├── react.jpg
│       └── vue.jpg
├── components
│   ├── AppBreadcrumb.js
│   ├── AppContent.js
│   ├── AppFooter.js
│   ├── AppHeader.js
│   ├── AppSidebar.js
│   ├── AppSidebarNav.js
│   ├── DocsCallout.js
│   ├── DocsExample.js
│   ├── DocsLink.js
│   ├── header
│   ├── Navbar.js
│   └── PrivateRoute.js
├── config.js
├── context
│   └── AuthContext.js
├── index.js
├── layout
│   └── DefaultLayout.js
├── _nav.js
├── routes.js
├── scss
│   ├── _custom.scss
│   ├── examples.scss
│   ├── style.scss
│   ├── _theme.scss
│   ├── _variables.scss
│   └── vendors
│       └── simplebar.scss
├── services
│   └── api.js
├── store.js
└── views
    ├── base
    ├── buttons
    ├── charts
    ├── dashboard
    ├── forms
    ├── icons
    ├── KeywordsResult.js
    ├── notifications
    ├── pages
    ├── theme
    ├── WebCrawler.js
    └── widgets

## Key Components

- **App.js**: Main application component.
- **assets/**: Contains images and branding assets.
- **components/**: Shared components like navigation, header, sidebar, etc.
- **context/**: Context for managing global state (e.g., authentication).
- **scss/**: Stylesheets and theme configurations.
- **services/**: API service for making HTTP requests.
- **views/**: Page components and UI views.


## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/SuperSEO-analyzer.git
cd SuperSEO-analyzer/frontend
```
### 2- install

```
npm install
```
### run it
```
npm start
```


## Available Scripts

- **`npm start`**: Runs the app in development mode.
- **`npm build`**: Builds the app for production.
- **`npm test`**: Launches the test runner.
- **`npm eject`**: Ejects the configuration (not recommended).


## Contributing

Contributions are welcome! Please submit a pull request or open an issue for suggestions.



# SuperSEO Analyzer Backend

This is the backend API for the SuperSEO Analyzer, a tool designed to help users analyze SEO performance by extracting keywords, managing URLs, and providing user management features.

## Features

- **Keyword Extraction**: Analyze text and extract keywords.
- **URL Management**: Add and manage URLs for SEO analysis.
- **User Authentication**: Register and authenticate users.

## Project Structure

```plaintext
.
├── base
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── keywords_extractor
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── utils.py
│   └── ...
├── urls
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── utils.py
│   └── ...
├── users
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── ...
├── manage.py
├── README.md
└── requirements.txt


## Getting Started
### Prerequisites
    Python 3.10+
    Django
    Django REST Framework

# Installation

1- clone the repo
```
git clone https://github.com/yourusername/SuperSEO-analyzer.git
cd SuperSEO-analyzer/backend
```


2- Install the dependencies:
```
pip install -r requirements.txt

```

3- Apply migrations:

```
python manage.py migrate

```

4- Run the server:

```
python manage.py runserver
```


## Testing
```
python manage.py test
```


## API Endpoints


### Keywords Extractor

- **GET /api/keywords/**: Retrieve extracted keywords.
- **POST /api/keywords/**: Submit text for keyword extraction.


### URLs

- **GET /api/urls/**: List all URLs.
- **POST /api/urls/**: Add a new URL for analysis.
- **GET /api/urls/{id}/**: Retrieve details of a specific URL.


### Users

- **POST /api/users/register/**: Register a new user.
- **POST /api/users/login/**: Authenticate a user.
- **GET /api/users/profile/**: Retrieve the authenticated user's profile.


## Contributing

Contributions are welcome! Please submit a pull request or open an issue for suggestions.

