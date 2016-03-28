from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# From http://stackoverflow.com/questions/5891555/display-the-date-like-may-5th-using-pythons-strftime
def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


@python_2_unicode_compatible  # only if you need to support Python 2
class Brew(models.Model):
    def __str__(self):
        return "{0} ({1})".format(self.vendor, custom_strftime('%a {S} %B', self.brew_date))

    # Timescales
    brew_date = models.DateTimeField(default=timezone.now)

    # Beans
    bean = models.ForeignKey('Bean', on_delete=models.CASCADE)
    vendor = models.CharField(max_length=200)  # e.g. Pact
    name = models.CharField(max_length=200)  # e.g. Sertaeo Pulped Natural
    grind = models.CharField(max_length=200)  # e.g. aeropress
    country = models.CharField(max_length=200)  # e.g. Brazil
    date_roasted = models.DateField(default=timezone.now)
    date_ground = models.DateField(default=timezone.now)
    ground_by = models.CharField(max_length=200)  # e.g. Eleni
    hints_of = models.CharField(max_length=200)  # e.g. Hazeulnut & Milk Chocolate
    roast_type = models.CharField(max_length=200)  # e.g. Medium Roast
    producer = models.CharField(max_length=200)
    process = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    varietal = models.CharField(max_length=200)
    altitude = models.CharField(max_length=200)
    farmer_question = models.TextField()
    farmer_answer = models.TextField()

    # Vendor's tasting notes
    tasting_notes_flavour = models.CharField(max_length=200)
    tasting_notes_sweetness = models.CharField(max_length=200)
    tasting_notes_acidity = models.CharField(max_length=200)
    tasting_notes_mouthfeel = models.CharField(max_length=200)
    pact_reviewer_name = models.CharField(max_length=200)
    pact_reviewer_says = models.TextField()

    # Water
    water_type = models.CharField(max_length=200)  # e.g. tap water
    kettle_cooldown_time = models.IntegerField(default=0)
    water_temperature = models.IntegerField(default=0)

    # Brew method
    brew_method = models.CharField(max_length=200)  # e.g. Aeropress
    brew_submethod = models.CharField(max_length=200)  # e.g. Standard/Inverted
    inspired_by = models.CharField(max_length=200)
    coffee_amount = models.CharField(max_length=200)  # e.g. 1 level scoop
    initial_water_volume = models.CharField(max_length=200)  # e.g. up to #1
    stir_amount = models.CharField(max_length=200)  # e.g. 5 times
    bloom_time = models.CharField(max_length=200)  # e.g. 25 seconds
    second_water_volume = models.CharField(max_length=200)  # e.g. up to #3
    second_water_time = models.CharField(max_length=200)  # e.g. 20 seconds
    plunge_time = models.CharField(max_length=200)  # e.g. 60 seconds
    plunge_into = models.CharField(max_length=200)  # e.g. cold cup
    repour_into_mug = models.BooleanField(default=False)
    hot_water_added = models.BooleanField(default=False)
    milk_added = models.BooleanField(default=False)
    sugar_added = models.BooleanField(default=False)

    # My tasting notes
    score = models.DecimalField(max_digits=2, decimal_places=1)  # e.g. 3.5 is "good to great"
    comments = models.TextField()


@python_2_unicode_compatible  # only if you need to support Python 2
class Bean(models.Model):
    def __str__(self):
        return "{0}, {1} ({2})".format(self.name, self.vendor, custom_strftime('%a {S} %B', self.date_roasted))

    # Beans
    vendor = models.CharField(max_length=200)  # e.g. Pact
    name = models.CharField(max_length=200)  # e.g. Sertaeo Pulped Natural
    grind = models.CharField(max_length=200)  # e.g. aeropress
    country = models.CharField(max_length=200)  # e.g. Brazil
    date_roasted = models.DateField(default=timezone.now)
    date_ground = models.DateField(default=timezone.now)
    ground_by = models.CharField(max_length=200)  # e.g. Eleni
    hints_of = models.CharField(max_length=200)  # e.g. Hazeulnut & Milk Chocolate
    roast_type = models.CharField(max_length=200)  # e.g. Medium Roast
    producer = models.CharField(max_length=200)
    process = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    varietal = models.CharField(max_length=200)
    altitude = models.CharField(max_length=200)
    farmer_question = models.TextField()
    farmer_answer = models.TextField()

    # Vendor's tasting notes
    tasting_notes_flavour = models.CharField(max_length=200)
    tasting_notes_sweetness = models.CharField(max_length=200)
    tasting_notes_acidity = models.CharField(max_length=200)
    tasting_notes_mouthfeel = models.CharField(max_length=200)
    pact_reviewer_name = models.CharField(max_length=200)
    pact_reviewer_says = models.TextField()


# @python_2_unicode_compatible  # only if you need to support Python 2
# class Choice(models.Model):
#    def __str__(self):
#        return self.choice_text
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
