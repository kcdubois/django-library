from django.db import models
from datetime import date, timedelta


class ReservationManager(models.Manager):
    def reserve_book(self, user, book):
        if book.is_available():
            reservation = self.create(
                user=user,
                book=book,
                due_date=date.today() + timedelta(days=14),  # default to a 2-week loan period
                status='reserved'
            )
            book.status = 'reserved'
            book.save()
            return reservation
        return None

    def cancel_reservation(self, reservation):
        if reservation.status == 'reserved':
            reservation.status = 'cancelled'
            reservation.save()
            reservation.book.status = 'available'
            reservation.book.save()
            return reservation
        return None

    def return_book(self, book):
        reservation = self.get(book=book, status='checked_out')
        reservation.status = 'returned'
        reservation.save()
        book.status = 'available'
        book.save()
        return reservation
