from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User, Musician

#@receiver(post_save, sender=Musician)
def createMusician(sender, instance, created, **kwargs):
    if created:
        user = instance
        musician = Musician.objects.create(
            user=user, 
            instruments=instruments,
            genres=genres,
            experience=experience,
            location=location,
            demo=demo,
        )

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createMusician, sender=User)
post_delete.connect(deleteUser, sender=Musician)