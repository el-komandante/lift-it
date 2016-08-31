import factory
from faker import Factory as FakerFactory
from models import User, Workout, LiftForm

faker = FakerFactory.create()

class UserFactory(factory.factory):
    class Meta:
        model = User
    username = 
class WorkoutFactory(factory.factory):
    class Meta:
        model = Workout
