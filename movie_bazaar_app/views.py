# from django.shortcuts import render, get_object_or_404, redirect
# from django.views import View
# from .models import Movie, Person, Genre, PersonMovie
#
#
# class HomeView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         ctx = {
#             'movies': movies
#         }
#         return render(request, 'homepage.html', ctx)
#
#
# class MovieDatailsView(View):
#     pass