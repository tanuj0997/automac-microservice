import uuid
from django.db import models


class AbstructBaseModel(models.Model):
    """
    Abstruct model for Manufacturer and CarDetail.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=("Updated At"))

    class Meta:
        abstract = True


class Manufacturer(AbstructBaseModel):
    """
    Model to store the information of car manufacturer.
    """

    class COUNTRY:
        UNITED_STATES = 1
        INDIA = 91
        AFGHANISTAN = 93
        POLAND = 48
        CHINA = 86
        FRANCE = 33
        IRAN = 98
        JAPAN = 81
        PERU = 51
        PAKISTAN = 92
        RASIA = 7

    COUNTRY_CODE_CHOICES = (
        (COUNTRY.UNITED_STATES, "1"),
        (COUNTRY.INDIA, "91"),
        (COUNTRY.AFGHANISTAN, "93"),
        (COUNTRY.POLAND, "48"),
        (COUNTRY.CHINA, "86"),
        (COUNTRY.FRANCE, "33"),
        (COUNTRY.JAPAN, "81"),
        (COUNTRY.PERU, "51"),
        (COUNTRY.PAKISTAN, "92"),
        (COUNTRY.RASIA, "7"),
    )

    country = models.IntegerField(
        choices=COUNTRY_CODE_CHOICES, default=COUNTRY.UNITED_STATES
    )
    name = models.CharField(max_length=52)

    def __str__(self):
        return "{}".format(self.name)


class CarDetail(AbstructBaseModel):
    """
    Cardetails model store the informations related the to car.
    """

    class COLOR:
        RED = "R"
        BLACK = "BL"
        GREEN = "G"
        WHITE = "W"
        BLUE = "BLU"

    class MODEL:
        SEDAN = "SEDAN"
        MPV = "MPV"
        SUV = "SUV"
        COUPE = "COUPE"
        CROSSOVER = "CROSSOVER"

    COLOR_CHOICES = [
        (COLOR.RED, "Red"),
        (COLOR.BLACK, "Black"),
        (COLOR.GREEN, "Green"),
        (COLOR.WHITE, "White"),
        (COLOR.BLUE, "Blue"),
    ]

    MODEL_CHOICES = [
        (MODEL.SEDAN, "SEDAN"),
        (MODEL.MPV, "MPV"),
        (MODEL.SUV, "SUV"),
        (MODEL.COUPE, "COUPE"),
        (MODEL.CROSSOVER, "CROSSOVER"),
    ]

    name = models.CharField(max_length=52, unique=True)
    model = models.CharField(max_length=12, choices=MODEL_CHOICES, null=True)
    color = models.CharField(max_length=3, choices=COLOR_CHOICES, null=True)
    door = models.IntegerField()
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    owner = models.CharField(max_length=26)

    def __str__(self):
        return "{}".format(self.name)
