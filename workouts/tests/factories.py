import random

import factory

from faker import providers

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

class MovementPlaneFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.MovementPlane

    name = fake.random_movement_plane()

class JointTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.JointType

    name = fake.random_joint_type()

class JointFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Joint

    name = factory.Sequence(lambda n: 'Joint #%s % n')
    joint_type = factory.SubFactory(JointTypeFactory)

class MovementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Movement

    name = fake.random_movement()
    movement_plane = factory.SubFactory(MovementPlaneFactory)
    agonist_muscle_group = factory.SubFactory(MuscleGroupFactory)
    agonist = factory.SubFactory(MuscleFactory)
    synergist = factory.SubFactory(MuscleFactory)
    antagonist = factory.SubFactory(MuscleFactory)

    @factory.post_generation
    def joints(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for joint in extracted:
                self.joints.add(joint)

class JointNumberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.JointNumber

    number = random.randint(1, 9)

class ContractionTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ContractionType

    name = fake.random_contraction_type()

class SidesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Sides

    name = fake.random_sides()

class EquipmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Equipment

    name = fake.random_equipment()

class ExerciseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Exercise

    name = fake.random_exercise()
    joint_number = factory.SubFactory(JointNumberFactory)
    sides = factory.SubFactory(SidesFactory)
    equipment = factory.SubFactory(EquipmentFactory)
    cues = fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)
    video_id = fake.md5(raw_output=False)
    difficulty = factory.SubFactory(ExerciseDifficultyFactory)

    @factory.post_generation
    def movements(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for movement in extracted:
                self.movements.add(movement)

# TODO: WorkoutExercises, WorkoutType, WorkoutDuration, WorkoutFrequency, WorkoutPhase, SeasonPlanDuration,Activity, WorkoutDifficulty, Workout Factories need to be made
