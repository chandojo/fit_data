import factory
from .fakes import *
from .. import models


class MuscleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Muscle

    name = fake.random_muscle()

class MuscleGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.MuscleGroup

    name = fake.random_muscle_group()

    @factory.post_generation
    def muscles(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for muscles in extracted:
                self.muscles.add(muscle)

class ExerciseDifficultyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ExerciseDifficulty

    name = fake.random_exercise_difficulty()

class MovementPlaneProvider(factory.django.DjangoModelFactory):
    class Meta:
        model = models.MovementPlane

    name = fake.random_movement_plane()

class JointTypeProvider(factory.django.DjangoModelFactory):
    class Meta:
        model = models.JointType

    name = fake.random_joint_type()

class JointProvider(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Joint

    name = fake.random_joint()
    joint_type = factory.SubFactory(JointTypeProvider)

class MovementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Movement

    name = fake.random_movement()
    movement_plane = factory.SubFactory(MovementPlaneProvider)
    agonist_muscle_group = factory.SubFactory(MuscleGroupFactory)
    agonist = factory.SubFactory(MuscleFactory)
    synergist = factory.SubFactory(MuscleFactory)
    antagonist = factory.SubFactory(MuscleFactory)
    # Write many-to-many field for 'joints' 
