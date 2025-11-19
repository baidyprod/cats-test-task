from django.db import models


class SpyCat(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    breed = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]


class Mission(models.Model):
    cat = models.ForeignKey(SpyCat, on_delete=models.SET_NULL, null=True, blank=True, related_name="missions")
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mission {self.id}"

    def save(self, *args, **kwargs):
        # Auto-complete mission if all targets are complete
        if self.pk:
            if self.targets.exists() and self.targets.filter(is_complete=False).count() == 0:
                self.is_complete = True
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]


class Target(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name="targets")
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True, default="")
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.country}"

    class Meta:
        ordering = ["created_at"]
