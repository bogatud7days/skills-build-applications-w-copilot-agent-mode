from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Cancella dati esistenti
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Team
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True)
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel', is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC', is_superhero=True)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='DC', is_superhero=True)

        # Activities
        Activity.objects.create(user=ironman.name, type='Running', duration=30, date='2025-11-01')
        Activity.objects.create(user=batman.name, type='Cycling', duration=45, date='2025-11-02')
        Activity.objects.create(user=superman.name, type='Swimming', duration=60, date='2025-11-03')
        Activity.objects.create(user=captain.name, type='Walking', duration=20, date='2025-11-04')

        # Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', difficulty='Hard')
        Workout.objects.create(name='Power Yoga', description='Yoga for super strength', difficulty='Medium')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=100, position=1)
        Leaderboard.objects.create(team='DC', points=90, position=2)

        self.stdout.write(self.style.SUCCESS('Database popolato con dati di test!'))
