from ticker import app, routes, models
from ticker.database import engine


models.Base.metadata.create_all(bind=engine)

