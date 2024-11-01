from django.urls import path

from .views import (
    UserProfileView,
    UserProfileUpdateView,
    BookListView,
    BookDetailView,
    ReservationListView,
    ReservationDetailView,
    reserve_book
)


app_name = "reservations"


urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="user-profile"),
    path("profile/update/", UserProfileUpdateView.as_view(),
         name="user-profile-update"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("reservations/", ReservationListView.as_view(), name="reservation-list"),
    path("reservations/<int:pk>/", ReservationDetailView.as_view(),
         name="reservation-detail"),
    path("books/reserve", reserve_book, name="reserve-book")
]
