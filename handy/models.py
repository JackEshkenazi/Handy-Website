from django.db import models

class Contractor(models.Model):
    """Model representing a contractor (but not a specific business card)."""
    name = models.CharField(max_length = 100)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    phone = models.CharField(max_length = 100)
    
    email = models.TextField(max_length=100, help_text='Enter email')
    
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    #city = models.ManyToManyField(City, help_text='Select a city')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this contractor."""
        return reverse('contractor-detail', args=[str(self.id)])
        """for this have to define a URL mapping that has the name contractor-detail, and define an associated view and template"""


