from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from django.urls import path,include

urlpatterns = [ 
    path("",include_docs_urls(title="Leads application",description="Leads application Docs")),
    path("schemas/",get_schema_view(title="Leads application",description="Leads application Docs",version="1.0.0")),
    path("leads/",include("leads.api.urls")),
    path("users/",include("users.api.urls")),
]