from django.contrib import admin
from accounts.models import User
from charitable_organization.models import CharitableOrg
from inventory.models import Inventory
from .models import Marathon,Checkpoint,Runners,Route
from sponsorship.models import Sponsorship

admin.site.register(User)
admin.site.register(CharitableOrg)
admin.site.register(Inventory)
admin.site.register(Marathon)
admin.site.register(Checkpoint)
admin.site.register(Runners)
admin.site.register(Route)
admin.site.register(Sponsorship)
