#!/usr/bin/python3

from unittest import TestCase
from vehiculo import Vehicle

class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(6)

    def test_default_fare_60(self):
        self.assertEqual(self.vehicle.fare(), 60)