from django.core.management.base import BaseCommand
from octofit_tracker.models import UserProfile, Activity, Team

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Team.objects.all().delete()
        UserProfile.objects.all().delete()

        # Create Marvel team
        marvel = Team.objects.create(name='Marvel', member_ids=[])
        marvel_heroes = [
            {'username': 'ironman', 'display_name': 'Iron Man', 'email': 'ironman@marvel.com'},
            {'username': 'spiderman', 'display_name': 'Spider-Man', 'email': 'spiderman@marvel.com'},
            {'username': 'captainamerica', 'display_name': 'Captain America', 'email': 'cap@marvel.com'},
        ]
        for hero in marvel_heroes:
            user = UserProfile.objects.create(**hero)
            marvel.member_ids.append(str(user.id))
            Activity.objects.create(user=user, name='Save the world', duration_minutes=120, notes='Heroic action')
        marvel.save()

        # Create DC team
        dc = Team.objects.create(name='DC', member_ids=[])
        dc_heroes = [
            {'username': 'batman', 'display_name': 'Batman', 'email': 'batman@dc.com'},
            {'username': 'superman', 'display_name': 'Superman', 'email': 'superman@dc.com'},
            {'username': 'wonderwoman', 'display_name': 'Wonder Woman', 'email': 'wonderwoman@dc.com'},
        ]
        for hero in dc_heroes:
            user = UserProfile.objects.create(**hero)
            dc.member_ids.append(str(user.id))
            Activity.objects.create(user=user, name='Fight crime', duration_minutes=90, notes='Justice served')
        dc.save()

        self.stdout.write(self.style.SUCCESS('octofit_db populated with Marvel and DC superheroes'))
