from typing import TYPE_CHECKING, ClassVar

from django.db import models

if TYPE_CHECKING:
    from . import Session, SessionEntry


class Race(models.Model):
    """Race event information relevent to all sessions"""

    id = models.BigAutoField(primary_key=True)
    season = models.ForeignKey("Season", on_delete=models.CASCADE, related_name="races")
    circuit = models.ForeignKey("Circuit", on_delete=models.CASCADE, related_name="races")
    team_drivers = models.ManyToManyField(
        "formula_one.TeamDriver", through="formula_one.RoundEntry", related_name="races"
    )
    round_entries: models.QuerySet["RoundEntry"]
    sessions: models.QuerySet["Session"]

    number = models.PositiveSmallIntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    race_number = models.PositiveSmallIntegerField(null=True, blank=True)
    wikipedia = models.URLField(null=True, blank=True)
    is_cancelled = models.BooleanField(default=False)

    class Meta:
        constraints: ClassVar = [models.UniqueConstraint(fields=["season", "number"], name="race_unique_season_number")]

    def __str__(self) -> str:
        return f"{self.season.year} {self.name}"


class RoundEntry(models.Model):
    """All data relating to a driver racing for a specific team for a race"""

    id = models.BigAutoField(primary_key=True)
    race = models.ForeignKey("Race", on_delete=models.CASCADE, related_name="round_entries")
    team_driver = models.ForeignKey("TeamDriver", on_delete=models.CASCADE, related_name="round_entries")
    sessions: models.QuerySet["Session"]
    session_entries: models.QuerySet["SessionEntry"]

    car_number = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        constraints: ClassVar = [
            models.UniqueConstraint(fields=["race", "team_driver", "car_number"], name="round_entry_unique")
        ]

    def __str__(self) -> str:
        return f"{self.team_driver} - {self.race}"
