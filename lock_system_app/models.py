from django.db import models

class RFIDUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    rfid_tag = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.username}, {self.user_id}"

class AccessLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    rfid_tag = models.CharField(max_length=50, null=True)  
    access_time = models.DateTimeField(auto_now_add=True)  

    def save(self, *args, **kwargs):
        # Fetch the username based on the rfid_tag
        if not self.username:  # If username is not provided (it shouldn't be)
            try:
                user = RFIDUser.objects.get(rfid_tag=self.rfid_tag)  # Look up RFIDUser by rfid_tag
                self.username = user.username  # Set username based on the RFID tag
            except RFIDUser.DoesNotExist:
                self.username = "Unknown"  # If RFID tag doesn't match any user, set "Unknown"
        super(AccessLog, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} accessed at {self.access_time}"
