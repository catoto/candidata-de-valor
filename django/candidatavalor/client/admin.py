from django.contrib import admin
from client.models import Client, Evaluate, PoliticalParty


class EvaluateAdmin(admin.ModelAdmin):
    pass


class PoliticalPartyAdmin(admin.ModelAdmin):
    pass


class ClientAdmin(admin.ModelAdmin):

    class Meta:
        model = Client
    
    raw_id_fields = [
        'user',
    ]


admin.site.register(Evaluate, EvaluateAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(PoliticalParty, PoliticalPartyAdmin)