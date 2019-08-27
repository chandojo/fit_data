import random

from faker import Faker
fake = Faker()

from faker.providers import BaseProvider


class MuscleProvider(BaseProvider):
    fake_muscles = ['Quadratus Lumborum', 'Rectus Femoris', 'Anterior Tibialis', 'Erector Spinae', 'Gluteus Medius', 'Trapezius']

    def random_muscle(self):
        return self.fake_muscles[random.randint(0, len(self.fake_muscles)-1)]

class MuscleGroupProvider(BaseProvider):
    fake_muscle_groups = ['Lower Back', 'Calves', 'Quadriceps', 'Hamstrings', 'Abdominals', 'Chest', 'Shoulder Girdle']

    def random_muscle_group(self):
        return self.fake_muscle_groups[random.randint(0, len(self.fake_muscle_groups)-1)]

class ExerciseDifficultyProvider(BaseProvider):
    fake_exercise_difficulties = ['Easy', 'Medium', 'Hard']

    def random_exercise_difficulty(self):
        return self.fake_exercise_difficulties[random.randint(0, len(self.fake_exercise_difficulties)-1)]

class MovementPlaneProvider(BaseProvider):
    fake_movement_planes = ['Sagittal', 'Transverse', 'Frontal']

    def random_movement_plane(self):
        return self.fake_movement_planes[random.randint(0, len(self.fake_movement_planes)-1)]

class MovementProvider(BaseProvider):
    fake_movements = ['Hip Extension', 'Shoulder Horizontal Abduction', 'Scapular Retraction', 'Wrist Pronation', 'Hip Adduction', 'Shoulder Interal Rotation', 'Knee Flexion']

    def random_movement(self):
        return self.fake_movements[random.randint(0, len(self.fake_movements)-1)]

class JointTypeProvider(BaseProvider):
    fake_joint_type = ['hinge', 'ball-and-socket', 'pivot', 'condyloid' ]

    def random_joint_type(self):
        return self.fake_joint_type[random.randint(0, len(self.fake_joint_type)-1)]

class ContractionTypeProvider(BaseProvider):
    fake_contraction_type = ['eccentric', 'concentric', 'isometric', 'isotonic', 'isokinetic']

    def random_contraction_type(self):
        return self.fake_contraction_type[random.randint(0, len(self.fake_contraction_type)-1)]

class SidesProvider(BaseProvider):
    fake_sides = ['bilateral', 'unilateral', 'left', 'right']

    def random_sides(self):
        return self.fake_sides[random.randint(0, len(self.fake_sides)-1)]

class EquipmentProvider(BaseProvider):
    fake_equipment = ['dumbbell', 'barbell', 'battle ropes', 'bodyweight', 'kettlebell', 'stability ball', 'bosu ball', 'bands']

    def random_equipment(self):
        return self.fake_equipment[random.randint(0, len(self.fake_equipment)-1)]

class ExerciseProvider(BaseProvider):
    fake_exercise = ['glute bridge', 'overhead press', 'goblet squat', 'push up', 'inverted row', 'walking lunge', 'box step-up']

    def random_exercise(self):
        return self.fake_exercise[random.randint(0, len(self.fake_exercise)-1)]

fake.add_provider(MuscleProvider)
fake.add_provider(MuscleGroupProvider)
fake.add_provider(ExerciseDifficultyProvider)
fake.add_provider(MovementProvider)
fake.add_provider(MovementPlaneProvider)
fake.add_provider(JointTypeProvider)
fake.add_provider(ContractionTypeProvider)
fake.add_provider(SidesProvider)
fake.add_provider(EquipmentProvider)
fake.add_provider(ExerciseProvider)
