class Seat:
    def __init__(self, number: int):
        self.number = number
        self.is_booked = False

class Show:
    def __init__(self, title: str):
        self.title = title
        # Tworzymy 5 miejsc dla tego seansu
        self.seats = [Seat(1), Seat(2), Seat(3), Seat(4), Seat(5)]

    def show_available_seats(self):
        # Pobiera numery tylko tych miejsc, które nie są zajęte
        available = [str(seat.number) for seat in self.seats if not seat.is_booked]
        print(f"Dostępne miejsca na '{self.title}': {', '.join(available)}")

    def book_seat(self, seat_number: int) -> Seat:
        # Szuka miejsca o podanym numerze i je rezerwuje
        for seat in self.seats:
            if seat.number == seat_number:
                if not seat.is_booked:
                    seat.is_booked = True
                    return seat
                else:
                    print(f"Miejsce {seat_number} jest już zajęte!")
                    return None
        print(f"Nie ma miejsca o numerze {seat_number}.")
        return None

class Ticket:
    def __init__(self, show: Show, seat: Seat):
        self.show = show
        self.seat = seat

    def print_ticket(self, customer_name: str):
        print(f"--- BILET --- | Film: {self.show.title} | Klient: {customer_name} | Miejsce: {self.seat.number}")

class Customer:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.tickets = []  # Odpowiednik pustego koszyka (ShoppingCart)

    def add_ticket(self, ticket: Ticket):
        if ticket is not None:
            self.tickets.append(ticket)

    def print_all_tickets(self):
        print(f"\nWydruk biletów dla: {self.name} ({self.email})")
        for ticket in self.tickets:
            ticket.print_ticket(self.name)

# ---------- Testy w bloku głównym ----------
if __name__ == "__main__":
    # 1. Tworzymy seans
    matrix = Show("Matrix Reaktywacja")
    
    # 2. Tworzymy klienta
    cust = Customer("Jan Kowalski", "jan.kowalski@example.com")

    # 3. Sprawdzamy dostępność miejsc
    print("Przed rezerwacją:")
    matrix.show_available_seats()

    # 4. Klient rezerwuje miejsca (jak dodawanie do koszyka)
    miejsce_1 = matrix.book_seat(2)
    miejsce_2 = matrix.book_seat(5)
    
    # 5. Tworzymy bilety z zarezerwowanych miejsc i dodajemy klientowi
    cust.add_ticket(Ticket(matrix, miejsce_1))
    cust.add_ticket(Ticket(matrix, miejsce_2))

    # Próba zajęcia tego samego miejsca:
    matrix.book_seat(2)

    # 6. Sprawdzamy dostępność po rezerwacjach
    print("\nPo rezerwacji:")
    matrix.show_available_seats()

    # 7. Drukujemy wszystkie bilety klienta (jak calculate_total w koszyku)
    cust.print_all_tickets()
