from django.conf import settings
from django.db import models
from uuid import uuid4
from commanders.models import User


class SpaceShip(models.Model):
    """
    The bones of greatness are what you make it,
    choose your vessel wisely.
    """
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True)
    classification = models.CharField(max_length=50)
    armament = models.TextField(max_length=300)
    engine_type = models.TextField(max_length=60)
    description = models.TextField()


    def __str__(self):
        return self.name


class Crew(models.Model):
    """
    Those who choose to go into the darkness and 
    inhospitable vacuum of space...don't like Earth.
    """

    class StaffLevel(models.TextChoices):
        UNASSIGNED = 'unassigned', 'UNASSIGNED'
        ADMIRAL = 'admiral', 'ADMIRAL'
        CAPTAIN = 'captain', 'CAPTAIN'
        EXECUTIVE_OFFICER = 'XO', 'XO'
        #put more choices here after testing


    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=100, default='no nicknames known')
    origin = models.CharField(max_length=50, default='unknown origin')
    description = models.TextField(max_length=400)
    staff_level = models.CharField(
        max_length=20, 
        choices=StaffLevel.choices, 
        default=StaffLevel.UNASSIGNED
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



# Going to hold off on this, want to get the SpaceShip and 
# Crew models working with some Templates first

# class Commander(models.Model):
#     """
#     Based off the User Model in the Commanders app
#     Choose your sides wisely and command your crew boldly!
#     """

#     class Alliance(models.TextChoices):
#         UNAFFILIATED = 'Unaffiliated', 'UNAFFILIATED'
#         OUTER_PLANETS_ALLIANCE = 'OPA', 'OPA'
#         MARS_CONGRESSIONAL_REPUBLIC = 'MCR', 'MCR'
#         UNITED_NATIONS = 'United Nations', 'UNITED NATIONS'


#     # user = models.OneToOneField(
#     #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     alliance = models.CharField(
#         max_length=25,
#         choices=Alliance.choices,
#         default=Alliance.UNAFFILIATED
#     )



# undecided how to make the docked ship:
# contained in one model that has all attributes 
# of the ship, or break it out as Mosh did
# with his Cart and CartItems


# class MyDock(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4)
#     commander = models.ForeignKey(
#         Commander, on_delete=models.PROTECT) # I think PROTECT is what I want, research further
#     spaceship = models.ForeignKey(
#         SpaceShip, on_delete=models.PROTECT,
#         related_name='dockedship')
#     captain = models.ForeignKey(
#         Crew, on_delete=models.PROTECT,
#         related_name='dockedcaptain')
#     xo = models.ForeignKey(
#         Crew, on_delete=models.PROTECT,
#         related_name='dockedxo')

    
#     def __str__(self):
#         return f'{self.commander} {self.id}'


# class MyDock(models.Model):
#     """
#     This is where you bring together your ship and crew!
#     Much like a Cart model.
#     """
#     id = models.UUIDField(primary_key=True, default=uuid4)
#     created_at = models.DateTimeField(auto_now_add=True)
#     commander = models.ForeignKey(Commander, on_delete=models.CASCADE)


# class MyDockSpaceShip(models.Model):
#     my_dock = models.ForeignKey(
#         MyDock, on_delete=models.PROTECT, 
#         related_name='myship')
#     spaceship = models.ForeignKey(
#         SpaceShip, on_delete=models.CASCADE,
#         related_name='dockedship')

#     def __str__(self):
#         return self.spaceship

#     # class Meta:
#     #     unique_together = [['my_dock', 'spaceship']]


# class MyDockCaptain(models.Model):
#     my_dock = models.ForeignKey(
#         MyDock, on_delete=models.PROTECT, 
#         related_name='mycaptain')
#     captain = models.ForeignKey(
#         Crew, on_delete=models.CASCADE,
#         related_name='dockedcaptain')

#     def __str__(self):
#         return self.captain


# class MyDockXO(models.Model):
#     my_dock = models.ForeignKey(
#         MyDock, on_delete=models.PROTECT, 
#         related_name='myxo')
#     xo = models.ForeignKey(
#         Crew, on_delete=models.CASCADE,
#         related_name='dockedxo')

#     def __str__(self):
#         return self.xo
