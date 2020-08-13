"""cc_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from monkey_island.cc.resources.root import Root
from monkey_island.cc.resources.auth.auth import Authenticate, init_jwt
from monkey_island.cc.resources.auth.registration import Registration

urlpatterns = [
    path('admin/', admin.site.urls),

    path(Root, '/api'),
    path(Registration, '/api/registration'),
    path(Authenticate, '/api/auth'),
    # path(Environment, '/api/environment'),
    # path(Monkey, '/api/monkey', '/api/monkey/', '/api/monkey/<string:guid>'),
    # path(Bootloader, '/api/bootloader/<string:os>'),
    # path(LocalRun, '/api/local-monkey', '/api/local-monkey/'),
    # path(ClientRun, '/api/client-monkey', '/api/client-monkey/'),
    # path(Telemetry, '/api/telemetry', '/api/telemetry/', '/api/telemetry/<string:monkey_guid>'),
    # path(MonkeyConfiguration, '/api/configuration', '/api/configuration/'),
    # path(IslandConfiguration, '/api/configuration/island', '/api/configuration/island/'),
    # path(MonkeyDownload, '/api/monkey/download', '/api/monkey/download/','/api/monkey/download/<string:path>'),
    # path(NetMap, '/api/netmap', '/api/netmap/'),
    # path(Edge, '/api/netmap/edge', '/api/netmap/edge/'),
    # path(Node, '/api/netmap/node', '/api/netmap/node/'),
    # path(NodeStates, '/api/netmap/nodeStates'),
    #
    # # report_type: zero_trust or security
    # path(
    #     Report,
    #     '/api/report/<string:report_type>',
    #     '/api/report/<string:report_type>/<string:report_data>'),
    # path(ZeroTrustFindingEvent, '/api/zero-trust/finding-event/<string:finding_id>'),
    # path(TelemetryFeed, '/api/telemetry-feed', '/api/telemetry-feed/'),
    # path(Log, '/api/log', '/api/log/'),
    # path(IslandLog, '/api/log/island/download', '/api/log/island/download/'),
    # path(PBAFileDownload, '/api/pba/download/<string:path>'),
    # path(FileUpload, '/api/fileUpload/<string:file_type>',
    #                  '/api/fileUpload/<string:file_type>?load=<string:filename>',
    #                  '/api/fileUpload/<string:file_type>?restore=<string:filename>'),
    # path(RemoteRun, '/api/remote-monkey', '/api/remote-monkey/'),
    # path(AttackConfiguration, '/api/attack'),
    # path(AttackReport, '/api/attack/report'),
    # path(VersionUpdate, '/api/version-update', '/api/version-update/'),
    # path(RemotePortCheck, '/api/monkey_control/check_remote_port/<string:port>'),
    # path(StartedOnIsland, '/api/monkey_control/started_on_island'),
    # path(MonkeyTest, '/api/test/monkey'),
    # path(ClearCaches, '/api/test/clear_caches'),
    # path(LogTest, '/api/test/log'),

]
