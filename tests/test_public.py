"""Public tests for Lab 04. Hidden tests are harder!"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import lab04 as lab  # noqa: E402

BN = {"Rain": ([], {(): 0.2}), "Wet": (["Rain"], {(True,): 0.9, (False,): 0.1})}

def test_rain_given_wet():
    d = lab.enumeration_ask("Rain", {"Wet": True}, BN)
    assert abs(d[True] - 0.18 / 0.26) < 1e-6
