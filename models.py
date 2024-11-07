from django.db import models

# Create your models here.

class election(models.Model):
    STATUS_OPTION =[
        ("R","RUNNING"),
        ("C","COMPLETE")
    ]
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now=False)
    status = models.CharField(max_length = 1,choices = STATUS_OPTION)

class position(models.Model):
    title = models.CharField(max_length=45)   

class voter(models.Model):
    GENDER_OPTIONS = [
        ("M","MALE"),
        ("F","FEMALE")
    ]
    Reg_no = models.CharField(max_length=15)
    Voter_name = models.CharField(max_length=35) 
    Gender = models.CharField(max_length=5,choices=GENDER_OPTIONS)   
    Contact = models.CharField(max_length=12)
    Course = models.CharField(max_length=15)
    Election = models.ForeignKey(election, on_delete=models.CASCADE) 

class candidate(models.Model):
    GENDER_OPTIONS = [
        ("F","FEMALE"),
        ("M","MALE")
    ]
    Candidate_name = models.CharField(max_length=35)
    Address = models.CharField(max_length=20)
    Gender = models.CharField(max_length=5,choices=GENDER_OPTIONS)
    Contact = models.CharField(max_length=12)
    Election = models.ForeignKey(election, on_delete=models.CASCADE) 
    position = models.ForeignKey(position, on_delete=models.CASCADE) 

class Ballot(models.Model):
    Election = models.ForeignKey(election, on_delete=models.CASCADE)
    position = models.ForeignKey(position, on_delete=models.CASCADE)
    Voter = models.ForeignKey(voter, on_delete=models.CASCADE)
    Candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)

    
