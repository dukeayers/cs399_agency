# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
import datetime

def add_data(apps, schema_editor):
    Campaign = apps.get_model("agency", "Campaign")

    CampaignTitles = ["Send-A-Cookie", "Glitter Bombs!"]
    CampaignDescription = ["Send a Cookie to a friend by filling out the form in regards to their location. Once completed, your friend will get an Oatmeal Raisin cookie labeled a Chocolate Chip! Way to be tricky.", "Ever wanted to get back at someone but just did not know how?  Send them a glitter bomb!  A tube of glitter will be sent to an address of your choosing and when it is opened someone will be in for a surprise!"]
    CampaignBegin = ["2015-02-15", "2015-02-15"]
    CampaignEnd = ["2015-05-23", "2015-08-30"]

    for i in range(0,2):
        data = Campaign(title = CampaignTitles[i], description = CampaignDescription[i], BeginDate = CampaignBegin[i], EndDate = CampaignEnd[i])
        data.save()


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_data)
    ]
