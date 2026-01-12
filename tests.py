import unittest
from datetime import datetime
from clinic import Doctor, Patient, Appointment, Clinic, Appointments


class TestAll(unittest.TestCase):

    def test_doctor_creation(self):
        d = Doctor("Іван", "Терапевт")
        self.assertEqual(d.name, "Іван")
        self.assertEqual(d.spec, "Терапевт")

    def test_patient_creation(self):
        p = Patient("Марія", 30)
        self.assertEqual(p.name, "Марія")
        self.assertEqual(p.age, 30)

    def test_appointment_creation(self):
        d = Doctor("Іван", "Терапевт")
        p = Patient("Марія", 30)
        dt = datetime(2026, 1, 15, 10, 30)
        a = Appointment(d, p, dt)

        self.assertEqual(a.doctor, d)
        self.assertEqual(a.patient, p)
        self.assertEqual(a.dt, dt)
        self.assertEqual(a.status, "Scheduled")

    def test_get_next_empty_queue(self):
        apps = Appointments()
        with self.assertRaises(IndexError):
            apps.get_next()

if __name__ == "__main__":
    unittest.main()
