from flask import Blueprint, render_template

def Index():
    site_config = {
        'title': 'Stock Analyzer | Home'
    }
    return render_template('index.html', config=site_config)

def APIIndex():
    site_config = {
        'title': 'Stock Analyzer API | Home'
    }
    return render_template('api_index.html', config=site_config)