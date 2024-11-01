"""
Library reservation system views.
"""
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from reservations.models import Book, Reservation
from reservations.forms import UserProfileForm


class UserProfileView(LoginRequiredMixin, DetailView):
    """
    View for displaying the user's profile.
    """
    model = get_user_model()
    template_name = "user_profile.html"
    context_object_name = "user"

    def get_object(self):
        # Display only the profile of the logged-in user
        return self.request.user


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating the user's profile.
    """
    model = get_user_model()
    form_class = UserProfileForm
    template_name = "user_profile_update.html"
    success_url = reverse_lazy("user-profile")

    def get_object(self):
        # Allow only the logged-in user to update their profile
        return self.request.user


class BookListView(ListView):
    """
    View for listing all available books in the catalog.
    """
    model = Book
    template_name = "reservations/book_list.html"
    context_object_name = "books"
    paginate_by = 10  # Optional pagination


class BookDetailView(DetailView):
    """
    View for displaying details of a specific book.
    """
    model = Book
    template_name = "reservations/book_detail.html"
    context_object_name = "book"


class ReservationListView(LoginRequiredMixin, ListView):
    """
    View for listing the user's reservations.
    """
    model = Reservation
    template_name = "reservations/reservation_list.html"
    context_object_name = "reservations"

    def get_queryset(self):
        # Filter reservations by the logged-in user
        if self.request.GET["status"]:
            return Reservation.objects.filter(
                user=self.request.user,
                status=self.request.GET["status"]
            )
        return Reservation.objects.filter(user=self.request.user)


class ReservationDetailView(LoginRequiredMixin, DetailView):
    """
    View for displaying details of a specific reservation.
    """
    model = Reservation
    template_name = "reservations/reservation_detail.html"
    context_object_name = "reservation"

    def get_queryset(self):
        # Allow users to see only their own reservations
        return Reservation.objects.filter(user=self.request.user)


@login_required
def reserve_book(request):
    book_id = request.POST['book_id']
    book = get_object_or_404(Book, pk=book_id)

    # Attempt to reserve the book using the Reservation manager's method
    reservation = Reservation.objects.reserve_book(request.user, book)

    if reservation:
        # Success message and redirect to reservation list
        messages.success(
            request, f"You have successfully reserved '{book.title}'.")
        return redirect('reservations:reservation-list')
    else:
        # Error message if the book is not available
        messages.error(
            request, "This book is currently unavailable for reservation.")
        return redirect('reservations:book-detail', pk=book.id)


@login_required
def cancel_reservation(request):
    reservation_id = request.POST['reservation_id']
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    reservation.cancel()

    messages.success(
        request, "Reservation successfully cancelled. The book is now available again.")
    return redirect('reservations:reservation-list')
