from datetime import datetime


# ===== ГЕНЕРАТОР ID =====
class ID:
    n = 1
    @classmethod
    def get(cls):
        cls.n += 1
        return cls.n - 1


# ===== МОДЕЛІ =====
class Doctor:
    def __init__(self, name, spec):
        self.id = ID.get()
        self.name = name
        self.spec = spec


class Patient:
    def __init__(self, name, age):
        self.id = ID.get()
        self.name = name
        self.age = age


class Appointment:
    def __init__(self, doctor, patient, dt):
        self.id = ID.get()
        self.doctor = doctor
        self.patient = patient
        self.dt = dt
        self.status = "Scheduled"

    def complete(self):
        self.status = "Completed"

    def cancel(self):
        self.status = "Cancelled"


# ===== СЕРВІСИ =====
class Clinic:
    def __init__(self):
        self.doctors = []
        self.patients = []

    def add_doctor(self, name, spec):
        d = Doctor(name, spec)
        self.doctors.append(d)
        return d

    def add_patient(self, name, age):
        p = Patient(name, age)
        self.patients.append(p)
        return p


class Appointments:
    def __init__(self):
        self.items = []

    def create(self, doctor, patient, dt):
        a = Appointment(doctor, patient, dt)
        self.items.append(a)
        return a

    def complete(self, id):
        for a in self.items:
            if a.id == id:
                a.complete()

    def cancel(self, id):
        for a in self.items:
            if a.id == id:
                a.cancel()

    def get_next(self):
        if not self.items:
            raise IndexError("Черга порожня! Немає записів на прийом.")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


# ===== MAIN =====
def main():
    clinic = Clinic()
    apps = Appointments()

    # Додаємо лікаря та пацієнта
    d1 = clinic.add_doctor("Іван Петров", "Терапевт")
    p1 = clinic.add_patient("Роман Іванченко", 19)

    # Створюємо один запис
    apps.create(d1, p1, datetime(2026, 1, 15, 10, 30))

    print("=== Обробка записів ===")
    try:
        while True:
            a = apps.get_next()
            print(f"{a.id}: {a.doctor.name} → {a.patient.name} @ {a.dt} [{a.status}]")
    except IndexError as e:
        print("Виключення:", e)


if __name__ == "__main__":
    main()
