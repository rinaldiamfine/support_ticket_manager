import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from flask_caching import Cache
from dotenv import load_dotenv
from flask_marshmallow import Marshmallow
from apps.blueprint_loaders import BlueprintLoaders

app = Flask(__name__)

load_dotenv()
app.debug = os.getenv("FLASK_DEBUG")
app.env = os.getenv("FLASK_ENV")

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
SQLALCHEMY_BINDS = {
    os.getenv('DB_NAME'): SQLALCHEMY_DATABASE_URI
}

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

cache = Cache(app, config={
    "CACHE_TYPE": "redis",
    "CACHE_KEY_PREFIX": "backend_",
    "CACHE_REDIS_HOST": "localhost",
    "CACHE_REDIS_PORT": "6377",
    "CACHE_REDIS_URL": "redis://localhost:6377"
})

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=os.getenv("CELERY_BACKEND"),
        broker=os.getenv("CELERY_BROKER_URL"),
    )

    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery = make_celery(app)

failed_imports = []
successful_imports = []
loader = BlueprintLoaders().discover_blueprints_by_pattern()
for blueprint in loader:
    try:
        app.register_blueprint(blueprint)
        successful_imports.append(blueprint)
    except Exception as e:
        failed_imports.append(blueprint)

# from akpusdafil.helpers.campaign_report import CampaignReport
# from akpusdafil.campaigns.collecting import MasterCampaignReports

import apps.models