# tests/conftest.py

import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome", help="Browser to run tests (Chrome, Edge, etc.)")
    parser.addoption("--url", action="store", default="https://the-internet.herokuapp.com/login", help="URL to test")
