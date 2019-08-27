from django.test import TestCase
from workouts.models import *
from . import factories

# TODO: Integration Tests on models

class MuscleModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fake_muscle = factories.MuscleFactory()
        cls.muscle_name = Muscle.objects.get(pk=1)
        super(MuscleModelTestCase, cls).setUpClass()

    def test_muscle_name_label(self):
        field_label = Muscle._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_muscle_name_max_length(self):
        max_length = Muscle._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_muscle_name_accurate(self):
        self.assertEqual(self.muscle_name.name, self.fake_muscle.name)

    @classmethod
    def tearDownClass(cls):
        cls.fake_muscle = None
        cls.muscle_name = None

class MuscleGroupModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fake_muscle_group = factories.MuscleGroupFactory()
        cls.muscle_group_name = MuscleGroup.objects.get(pk=1)
        super(MuscleGroupModelTestCase, cls).setUpClass()

    def test_muscle_group_name_label(self):
        field_label = MuscleGroup._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_muscle_group_name_max_length(self):
        max_length = MuscleGroup._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_muscles_label(self):
        field_label = MuscleGroup._meta.get_field('muscles').verbose_name
        self.assertEquals(field_label, 'muscles')

    def test_muscle_group_name_accurate(self):
        self.assertEqual(self.muscle_group_name.name, self.fake_muscle_group.name)

    @classmethod
    def tearDownClass(cls):
        cls.fake_muscle_group = None
        cls.muscle_group_name = None


class ExerciseDifficultyModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fake_exercise_difficulty = factories.ExerciseDifficultyFactory()
        cls.exercise_difficulty = ExerciseDifficulty.objects.get(pk=1)
        cls.name_field_label = ExerciseDifficulty._meta.get_field('name')
        super(ExerciseDifficultyModelTestCase, cls).setUpClass()

    def test_exercise_difficulty_name_label(self):
        field_label = self.name_field_label.verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = self.name_field_label.max_length
        self.assertEquals(max_length, 100)

    def test_exercise_name_accurate(self):
        self.assertEqual(self.exercise_difficulty.name, self.fake_exercise_difficulty.name)

    @classmethod
    def tearDownClass(cls):
        cls.fake_exercise_difficulty = None
        cls.exercise_difficulty = None
        cls.name_field_label = None


class MovementModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fake_movement = factories.MovementFactory()
        cls.movement = Movement.objects.get(pk=1)
        super(MovementModelTestCase, cls).setUpClass()

    def test_movement_name_label(self):
        field_label = Movement._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = Movement._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_movement_plane_label(self):
        field_label = Movement._meta.get_field('movement_plane').verbose_name
        self.assertEquals(field_label, 'movement plane')

    def test_agonist_muscle_group_label(self):
        field_label = Movement._meta.get_field('agonist_muscle_group').verbose_name
        self.assertEquals(field_label, 'agonist muscle group')

    def test_agonist_label(self):
        field_label = Movement._meta.get_field('agonist').verbose_name
        self.assertEquals(field_label, 'agonist')

    def test_synergist_label(self):
        field_label = Movement._meta.get_field('synergist').verbose_name
        self.assertEquals(field_label, 'synergist')

    def test_antagonist_label(self):
        field_label = Movement._meta.get_field('antagonist').verbose_name
        self.assertEquals(field_label, 'antagonist')

    def test_joints_label(self):
        field_label = Movement._meta.get_field('joints').verbose_name
        self.assertEquals(field_label, 'joints')

    def test_movement_name_accurate(self):
        self.assertEqual(self.movement.name, self.fake_movement.name)

    def test_movement_movement_plane_accurate(self):
        self.assertEqual(self.movement.movement_plane, self.fake_movement.movement_plane)

    def test_movement_agonist_muscle_group_accurate(self):
        self.assertEqual(self.movement.agonist_muscle_group, self.fake_movement.agonist_muscle_group)

    def test_movement_agonist_accurate(self):
        self.assertEqual(self.movement.agonist, self.fake_movement.agonist)

    def test_movement_synergist_accurate(self):
        self.assertEqual(self.movement.synergist, self.fake_movement.synergist)

    def test_movement_antagonist_accurate(self):
        self.assertEqual(self.movement.antagonist, self.fake_movement.antagonist)

    @classmethod
    def tearDownClass(cls):
        cls.fake_movement = None
        cls.movement = None

class MovementPlaneModelTestCase(TestCase):
    def test_movement_plane_name_label(self):
        field_label = MovementPlane._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = MovementPlane._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_movement_plane_name_accurate(self):
        fake_movement_plane = factories.MovementPlaneFactory()
        movement_plane = MovementPlane.objects.get(pk=1)
        self.assertEqual(movement_plane.name, fake_movement_plane.name)

class JointModelTestCase(TestCase):
    def test_joint_name_label(self):
        field_label = Joint._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = Joint._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_joint_type_label(self):
        field_label = Joint._meta.get_field('joint_type').verbose_name
        self.assertEquals(field_label, 'joint type')

    def test_joint_name_accurate(self):
        fake_joint = factories.JointFactory()
        joint = Joint.objects.get(pk=1)
        self.assertEqual(joint.name, fake_joint.name)

class JointTypeModelTestCase(TestCase):
    def test_joint_type_name_label(self):
        field_label = JointType._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = JointType._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_joint_type_name_accurate(self):
        fake_joint_type = factories.JointTypeFactory()
        joint_type = JointType.objects.get(pk=1)
        self.assertEqual(joint_type.name, fake_joint_type.name)

class JointNumberModelTestCase(TestCase):
    def test_joint_number_number_label(self):
        field_label = JointNumber._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')

    def test_joint_number_accurate(self):
        fake_joint_number = factories.JointNumberFactory()
        joint_number = JointNumber.objects.get(pk=1)
        self.assertEquals(joint_number.number, fake_joint_number.number)

class ContractionTypeModelTestCase(TestCase):
    def test_contraction_name_label(self):
        field_label = ContractionType._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = ContractionType._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_name_contraction_accurate(self):
        fake_contraction_type = factories.ContractionTypeFactory()
        contraction_type = ContractionType.objects.get(pk=1)
        self.assertEquals(contraction_type.name, fake_contraction_type.name)

class SidesModelTestCase(TestCase):
    def test_sides_name_label(self):
        field_label = Sides._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = Sides._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_name_sides_accurate(self):
        fake_sides = factories.SidesFactory()
        sides = Sides.objects.get(pk=1)
        self.assertEquals(sides.name, fake_sides.name)

class EquipmentModelTestCase(TestCase):
    def test_equipment_name_label(self):
        field_label = Equipment._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = Equipment._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_name_sides_accurate(self):
        fake_equipment = factories.EquipmentFactory()
        equipment = Equipment.objects.get(pk=1)
        self.assertEquals(equipment.name, fake_equipment.name)

class ExerciseModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fake_exercise = factories.ExerciseFactory()
        cls.exercise = Exercise.objects.get(pk=1)
        super(ExerciseModelTestCase, cls).setUpClass()

    def test_exercise_name_label(self):
        field_label = Exercise._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = Exercise._meta.get_field('name').max_length
        self.assertEquals(max_length, 150)

    def test_joint_number_label(self):
        field_label = Exercise._meta.get_field('joint_number').verbose_name
        self.assertEquals(field_label, 'joint number')

    def test_sides_label(self):
        field_label = Exercise._meta.get_field('sides').verbose_name
        self.assertEquals(field_label, 'sides')

    def test_movements_label(self):
        field_label = Exercise._meta.get_field('movements').verbose_name
        self.assertEquals(field_label, 'movements')

    def test_equipment_label(self):
        field_label = Exercise._meta.get_field('equipment').verbose_name
        self.assertEquals(field_label, 'equipment')

    def test_cues_label(self):
        field_label = Exercise._meta.get_field('cues').verbose_name
        self.assertEquals(field_label, 'cues')

    def test_video_label(self):
        field_label = Exercise._meta.get_field('video_id').verbose_name
        self.assertEquals(field_label, 'video id')

    def test_name_max_length(self):
        max_length = Exercise._meta.get_field('video_id').max_length
        self.assertEquals(max_length, 50)

    def test_difficulty_label(self):
        field_label = Exercise._meta.get_field('difficulty').verbose_name
        self.assertEquals(field_label, 'difficulty')

    def test_name_exercise_accurate(self):
        self.assertEquals(self.exercise.name, self.fake_exercise.name)

    def test_joint_number_exercise_accurate(self):
        self.assertEquals(self.exercise.joint_number, self.fake_exercise.joint_number)

    def test_sides_exercise_accurate(self):
        self.assertEquals(self.exercise.sides, self.fake_exercise.sides)

    def test_equipment_exercise_accurate(self):
        self.assertEquals(self.exercise.equipment, self.fake_exercise.equipment)

    @classmethod
    def tearDownClass(cls):
        cls.fake_exercise = None
        cls.exercise = None

class WorkoutExercisesModelTestCase(TestCase):
    def test_workout_exercises_name_label(self):
        field_label = WorkoutExercises._meta.get_field('exercise').verbose_name
        self.assertEquals(field_label, 'exercise')

    def test_sets_label(self):
        field_label = WorkoutExercises._meta.get_field('sets').verbose_name
        self.assertEquals(field_label, 'sets')

    def test_reps_label(self):
        field_label = WorkoutExercises._meta.get_field('reps').verbose_name
        self.assertEquals(field_label, 'reps')

    def test_rep_duration_label(self):
        field_label = WorkoutExercises._meta.get_field('rep_duration').verbose_name
        self.assertEquals(field_label, 'rep duration')

    def test_rest_btwn_sets_sec_label(self):
        field_label = WorkoutExercises._meta.get_field('rest_btwn_sets_sec').verbose_name
        self.assertEquals(field_label, 'rest btwn sets sec')

    def test_contraction_type_label(self):
        field_label = WorkoutExercises._meta.get_field('contraction_type').verbose_name
        self.assertEquals(field_label, 'contraction type')

    def test_intensity_label(self):
        field_label = WorkoutExercises._meta.get_field('intensity').verbose_name
        self.assertEquals(field_label, 'intensity')

    def test_intensity_percentage_label(self):
        field_label = WorkoutExercises._meta.get_field('intensity_percentage').verbose_name
        self.assertEquals(field_label, 'intensity percentage')

    def test_workout_plan_label(self):
        field_label = WorkoutExercises._meta.get_field('workout_plan').verbose_name
        self.assertEquals(field_label, 'workout plan')

class WorkoutTypeModelTestCase(TestCase):
    def test_workout_type_name_label(self):
        field_label = WorkoutType._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = WorkoutType._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

class WorkoutDurationModelTestCase(TestCase):
    def test_workout_duration_weeks_label(self):
        field_label = WorkoutDuration._meta.get_field('weeks').verbose_name
        self.assertEquals(field_label, 'weeks')

class WorkoutFrequencyModelTestCase(TestCase):
    def test_workout_frequency_days_per_week_label(self):
        field_label = WorkoutFrequency._meta.get_field('days_per_week').verbose_name
        self.assertEquals(field_label, 'days per week')

class WorkoutPhaseModelTestCase(TestCase):
    def test_workout_phase_name_label(self):
        field_label = WorkoutPhase._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = WorkoutPhase._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

class SeasonPlanDurationModelTestCase(TestCase):
    def test_season_plan_duration_name_label(self):
        field_label = SeasonPlanDuration._meta.get_field('months').verbose_name
        self.assertEquals(field_label, 'months')

class ActivityModelTestCase(TestCase):
    def test_activity_name_label(self):
        field_label = Activity._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = Activity._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

class SeasonPlanModelTestCase(TestCase):
    def test_season_plan_name_label(self):
        field_label = SeasonPlan._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = SeasonPlan._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_activity_label(self):
        field_label = SeasonPlan._meta.get_field('activity').verbose_name
        self.assertEquals(field_label, 'activity')

    def test_season_duration_label(self):
        field_label = SeasonPlan._meta.get_field('season_duration').verbose_name
        self.assertEquals(field_label, 'season duration')

class WorkoutDifficultyModelTestCase(TestCase):
    def test_workout_difficulty_name_label(self):
        field_label = WorkoutDifficulty._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = WorkoutDifficulty._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

class WorkoutModelTestCase(TestCase):
    def test_workout_name_label(self):
        field_label = Workout._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        max_length = Workout._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_workout_type_label(self):
        field_label = Workout._meta.get_field('workout_type').verbose_name
        self.assertEquals(field_label, 'workout type')

    def test_workout_duration_label(self):
        field_label = Workout._meta.get_field('workout_duration').verbose_name
        self.assertEquals(field_label, 'workout duration')

    def test_workout_frequency_label(self):
        field_label = Workout._meta.get_field('workout_frequency').verbose_name
        self.assertEquals(field_label, 'workout frequency')

    def test_workout_phase_label(self):
        field_label = Workout._meta.get_field('workout_phase').verbose_name
        self.assertEquals(field_label, 'workout phase')

    def test_season_plan_label(self):
        field_label = Workout._meta.get_field('season_plan').verbose_name
        self.assertEquals(field_label, 'season plan')

    def test_workout_difficulty_label(self):
        field_label = Workout._meta.get_field('workout_difficulty').verbose_name
        self.assertEquals(field_label, 'workout difficulty')
