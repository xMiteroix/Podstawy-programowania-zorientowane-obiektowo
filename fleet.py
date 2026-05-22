from abc import ABC, abstractmethod
from datetime import datetime

# 1. ABSTRAKCJA (Klasa abstrakcyjna)
class Vehicle(ABC):
    def __init__(self, brand: str, model: str, rental_rate: float):
        self.brand = brand
        self.model = model
        self.is_available = True
        # 2. ENKAPSULACJA (Prywatne pole i walidacja w setterze)
        self._rental_rate = 0
        self.rental_rate = rental_rate 

    @property
    def rental_rate(self):
        return self._rental_rate

    @rental_rate.setter
    def rental_rate(self, value):
        if value < 0:
            raise ValueError("Stawka wynajmu nie może być ujemna!")
        self._rental_rate = value

    @abstractmethod
    def vehicle_type(self) -> str:
        pass

    # Przeciążenie metody (w Pythonie robimy to domyślnymi argumentami)
    def rent(self, date: str = None):
        self.is_available = False
        rent_date = date if date else datetime.now().strftime("%Y-%m-%d")
        print(f"Pojazd {self.brand} {self.model} wypożyczony od: {rent_date}")

    def return_vehicle(self):
        self.is_available = True

# 3. DZIEDZICZENIE
class Car(Vehicle):
    def __init__(self, brand: str, model: str, rental_rate: float, fuel_type: str):
        super().__init__(brand, model, rental_rate)
        self.fuel_type = fuel_type

    # 4. POLIMORFIZM
    def vehicle_type(self) -> str:
        return f"Samochód spalinowy ({self.fuel_type})"

# INTERFEJS (W Pythonie klasa czysto abstrakcyjna)
class ElectricVehicle(ABC):
    @abstractmethod
    def charge(self):
        pass

# ROZSZERZENIE: WIELOKROTNE DZIEDZICZENIE
class HybridCar(Car, ElectricVehicle):
    def __init__(self, brand: str, model: str, rental_rate: float):
        super().__init__(brand, model, rental_rate, "Hybryda")

    def charge(self):
        print(f"Ładowanie baterii w {self.brand} {self.model}...")

    def vehicle_type(self) -> str:
        return "Samochód Hybrydowy (Spalinowo-Elektryczny)"

class User:
    def __init__(self, first_name: str, last_name: str):
        # Enkapsulacja danych użytkownika
        self.__first_name = first_name
        self.__last_name = last_name

    def get_full_name(self) -> str:
        return f"{self.__first_name} {self.__last_name}"

# KOMPOZYCJA (Wypożyczenie zawiera User i Vehicle)
class Rental:
    def __init__(self, user: User, vehicle: Vehicle):
        self.user = user
        self.vehicle = vehicle
        self.date = datetime.now().strftime("%Y-%m-%d")

# METODY I WŁAŚCIWOŚCI STATYCZNE
class RentalManager:
    active_rentals = []

    @staticmethod
    def rent_vehicle(user: User, vehicle: Vehicle):
        if vehicle.is_available:
            vehicle.rent()
            RentalManager.active_rentals.append(Rental(user, vehicle))
            print(f"Sukces: {user.get_full_name()} wypożyczył {vehicle.brand}.")
        else:
            print("Pojazd jest niedostępny.")

    @staticmethod
    def show_rentals():
        print("\n--- Aktualne Wypożyczenia ---")
        for r in RentalManager.active_rentals:
            print(f"{r.user.get_full_name()} -> {r.vehicle.brand} {r.vehicle.model}")
        print("-----------------------------\n")


# === TESTY (Zaliczające zadanie) ===
if __name__ == "__main__":
    # Tworzenie pojazdów i przeciążenie (różne konstrukcje)
    car1 = Car("Peugeot", "308 GT", 150.0, "Diesel")
    car2 = Car("Volvo", "V60", 200.0, "Diesel")
    hybrid = HybridCar("Volvo", "XC90 Recharge", 300.0)

    # Tworzenie klienta
    klient = User("Jan", "Kowalski")

    print(f"Typ pojazdu 1: {car1.vehicle_type()}")
    print(f"Typ pojazdu 3: {hybrid.vehicle_type()}")
    
    hybrid.charge()

    # Zarządzanie (Static) i Kompozycja
    RentalManager.rent_vehicle(klient, car1)
    RentalManager.rent_vehicle(klient, hybrid)
    
    # Próba wypożyczenia zajętego auta
    RentalManager.rent_vehicle(klient, car1)

    RentalManager.show_rentals()
