POSTGRE_URI = 'postgresql://user_id:password@127.0.0.1:5432/flask_app'
import app

from flask_migrate import Migrate

application = app.app
migrate = Migrate(app, app.db)

