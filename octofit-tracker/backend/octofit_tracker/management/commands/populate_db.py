from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Super Strength', description='Strength workout', suggested_for='Marvel'),
            Workout.objects.create(name='Stealth Training', description='Stealth and agility', suggested_for='DC'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='Web Swinging', duration_minutes=30, date=timezone.now())
        Activity.objects.create(user=users[1], activity_type='Suit Up', duration_minutes=45, date=timezone.now())
        Activity.objects.create(user=users[2], activity_type='Lasso Practice', duration_minutes=40, date=timezone.now())
        Activity.objects.create(user=users[3], activity_type='Detective Work', duration_minutes=50, date=timezone.now())

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[2], score=95, rank=3)
        Leaderboard.objects.create(user=users[3], score=85, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
