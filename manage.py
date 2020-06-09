import os
import unittest
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS
from app import create_app, db
from app.api import api_blueprint
from app.main import main_blueprint
from app.stream import stream_blueprint

app = create_app(os.getenv('STOCK_PROJ') or 'dev')
app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(stream_blueprint)
app.app_context().push()
CORS(app, resources={r"/api/*": {"origins": "*"}})
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()