from __future__ import unicode_literals
from django.db import models, migrations
import datetime

def add_data(apps, schema_editor):
    Campaign = apps.get_model("agency", "Campaign")

    CampaignTitles = ["Send-A-Cookie", "Glitter Bombs!", 'Adopt-a-Gerbil']
    CampaignDescription = ["Send a Cookie to a friend by filling out the form in regards to their location. Once "
                           "completed, your friend will get an Oatmeal Raisin cookie labeled a Chocolate Chip! Way to "
                           "be tricky.", "Ever wanted to get back at someone but just did not know how?  Send them a "
                                         "glitter bomb!  A tube of glitter will be sent to an address of your choosing "
                                         "and when it is opened someone will be in for a surprise!", "Responsibility can"
                                         "be difficult to gauge. Luckily, there's an easy way to find out if your friend "
                                        "is responsible or not. Send a gerbil! It could go wonderfully or ... let's just "
                                                                                            "find out! "]
    CampaignBegin = ["2015-02-15", "2015-02-15","2015-09-12", "2015-12-01"]
    CampaignEnd = ["2015-05-23", "2015-08-30","2015-12-15", "2015-02-20"]
    CampId = [1, 2, 3]

    for i in range(0,3):
        data = Campaign(title = CampaignTitles[i], description = CampaignDescription[i], BeginDate = CampaignBegin[i], EndDate = CampaignEnd[i], id = CampId[i])
        data.save()


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0002_initial'),
    ]

    operations = [
        migrations.RunPython(add_data)
    ]
