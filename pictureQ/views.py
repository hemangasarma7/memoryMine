from django.contrib.auth import login, authenticate
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Album, Photo
from .forms import AlbumCreateForm, PhotoCreateForm, RegistrationForm


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'pictureQ/index.html'

    def get_queryset(self):
        return Album.objects.all()


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'pictureQ/album-detail.html'


class AllPhotosView(generic.ListView):
    template_name = 'pictureQ/photo_list.html'

    def get_queryset(self):
        return Photo.objects.all()


class CreateAlbum(CreateView):
    model = Album
    form_class = AlbumCreateForm


class EditAlbum(UpdateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'pictureQ/edit_album.html'


class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy('pictureQ:index')


def upload_photos(request, pk):

    for file in request.FILES.getlist('images'):
        album = Album.objects.get(id=pk)
        photo = Photo(image=file, album=album)
        photo.save()

    return HttpResponseRedirect(reverse('pictureQ:album-detail', kwargs={'pk': pk}))


class PhotoDetailView(generic.DetailView):
    model = Photo
    template_name = 'pictureQ/photo-detail.html'


class CreatePhoto(CreateView):
    model = Photo
    form_class = PhotoCreateForm


class EditPhoto(UpdateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = 'pictureQ/edit_photo.html'


class DeletePhoto(DeleteView):
    model = Photo

    def get_success_url(self):
        album = self.object.album
        if album:
            return reverse_lazy('pictureQ:album-detail', kwargs={'pk': album.id})
        return reverse_lazy('pictureQ:all-photos')


class RegisterUserView(View):
    form_class = RegistrationForm
    template_name = 'pictureQ/register.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process input form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # clean (normalised) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password,
                                first_name=first_name, last_name=last_name, email=email)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('pictureQ:index')

        return render(request, self.template_name, {'form': form})


def favorite(request, pk):

    selected_photo = get_object_or_404(Photo, pk=pk)
    selected_photo.is_favorite = not selected_photo.is_favorite
    selected_photo.save()
    return render(request, 'pictureQ/album-detail.html', {'album': selected_photo.album})
