from flask import render_template

def index():
    site_config = {
        'title': 'Stock Analyzer | Home'
    }
    return render_template('index.html', config=site_config)

def apiIndex():
    site_config = {
        'title': 'Stock Analyzer API | Home'
    }
    return render_template('api_index.html', config=site_config)