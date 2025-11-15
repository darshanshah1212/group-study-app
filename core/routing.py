from django.urls import path
from . import consumers

websocket_patterns = [
    path("ws/stdy_grp/<str:room_name>/",consumers.MyStudyGrp.as_asgi())
]