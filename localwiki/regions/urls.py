from django.conf.urls import *

from regions.views import (RegionCreateView, RegionPostSaveLogInView, RegionExploreView,
    RegionListView, RegionListMapView, RegionSettingsView, RegionAdminsUpdate, RegionBannedUpdate)


urlpatterns = patterns('',
    url(r'^regions/?$', RegionExploreView.as_view(), name="list"),
    url(r'^regions/_map', RegionListMapView.as_view(), name="as-map"),
    url(r'^regions/_as_list', RegionListView.as_view(), name="as-list"),
    url(r'^_region/_add', RegionCreateView.as_view(), name="add"),
    url(r'^_region/_post_save_log_in', RegionPostSaveLogInView.as_view(), name='post-save-log-in'),
    url(r'^(?P<region>[^/]+?)/_settings/?$', RegionSettingsView.as_view(), name="settings"),
    url(r'^(?P<region>[^/]+?)/_settings/admins/?$', RegionAdminsUpdate.as_view(), name="edit-admins"),
    url(r'^(?P<region>[^/]+?)/_settings/banned/?$', RegionBannedUpdate.as_view(), name="edit-banned"),
)
