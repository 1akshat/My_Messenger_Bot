from django.conf.urls import include, url
from .views import ChatBotView

urlpatterns = [
			       url(r'^2e858a5cbd84c4100b35bfcb354e0a8728de8ece0c5b5442e7/$', ChatBotView.as_view())
]