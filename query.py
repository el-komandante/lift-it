from app import models

for instance in models.db.session.query(models.User).order_by(models.User.id):
    print(instance.username)
