import pytest
import app
import sys

print(sys.path)

def test_sanity():
        assert 1==1, "Module succefully imported"