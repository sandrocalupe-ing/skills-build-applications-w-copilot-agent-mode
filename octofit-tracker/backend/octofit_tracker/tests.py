"""Unit tests for the OctoFit Tracker backend."""

from django.test import TestCase

from .models import Activity, Team, UserProfile


class DatabasePopulationTest(TestCase):
    def test_create_and_query_test_data(self):
        # Create a user profile
        user = UserProfile.objects.create(username='testuser', display_name='Test User', email='test@example.com')

        # Create some activities for that user
        Activity.objects.create(user=user, name='Morning Run', duration_minutes=30, notes='Felt great.')
        Activity.objects.create(user=user, name='Evening Yoga', duration_minutes=45, notes='Relaxing.')

        # Create a team and add this user to it
        team = Team.objects.create(name='Test Team', member_ids=[user.id])

        # Verify objects are persisted and queryable
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(Activity.objects.count(), 2)
        self.assertEqual(Team.objects.count(), 1)
        self.assertIn(str(user.id), [str(mid) for mid in team.member_ids])


    class WorkoutTest(TestCase):
        def test_create_and_query_workout(self):
            from .models import Workout
            workout = Workout.objects.create(name='Pushups', description='Upper body exercise', difficulty='Easy')
            self.assertEqual(Workout.objects.count(), 1)
            self.assertEqual(workout.name, 'Pushups')


        class LeaderboardEntryTest(TestCase):
            def test_create_and_query_leaderboard_entry(self):
                from .models import LeaderboardEntry, UserProfile
                user = UserProfile.objects.create(username='hero', display_name='Hero', email='hero@example.com')
                entry = LeaderboardEntry.objects.create(user=user, score=100, rank=1)
                self.assertEqual(LeaderboardEntry.objects.count(), 1)
                self.assertEqual(entry.score, 100)
                self.assertEqual(entry.rank, 1)
