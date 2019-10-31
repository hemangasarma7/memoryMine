from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .decorators import logout_required

app_name = 'pictureQ'


urlpatterns = [

    # register/
    url(r'^register/$', logout_required(views.RegisterUserView.as_view()), name='register'),

    # pictureQ/
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),

    # pictureQ/photos/
    url(r'^pictureQ/photos/$', login_required(views.AllPhotosView.as_view()), name='all-photos'),

    # pictureQ/album/add/
    url(r'^album/add/$', login_required(views.CreateAlbum.as_view()), name='add-album'),

    # picture/<album.id>/
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.AlbumDetailView.as_view()), name='album-detail'),

    # pictureQ/album/edit/<album.id>
    url(r'^album/edit/(?P<pk>[0-9]+)/$', login_required(views.EditAlbum.as_view()), name='edit-album'),

    # pictureQ/album/delete/<album.id>
    url(r'^album/delete/(?P<pk>[0-9]+)/$', login_required(views.DeleteAlbum.as_view()), name='delete-album'),

    # pictureQ/upload/<album.id>/
    url(r'^upload/(?P<pk>[0-9]+)/$', login_required(views.upload_photos), name='upload-photos'),

    # pictureQ/photo/<photo.id>/
    url(r'^photo/(?P<pk>[0-9]+)/$', login_required(views.PhotoDetailView.as_view()), name='photo-detail'),

    # pictureQ/photo/add/
    url(r'^photo/add/$', login_required(views.CreatePhoto.as_view()), name='add-photo'),

    # pictureQ/photo/edit/<photo.id>
    url(r'^photo/edit/(?P<pk>[0-9]+)/$', login_required(views.EditPhoto.as_view()), name='edit-photo'),

    # pictureQ/photo/delete/<photo.id>
    url(r'^photo/delete/(?P<pk>[0-9]+)/$', login_required(views.DeletePhoto.as_view()), name='delete-photo'),

    # pictureQ/photo/<photo.id>/favorite/
    url(r'^photo/(?P<pk>[0-9]+)/favorite/$', login_required(views.favorite), name='favorite'),

]
