from pytrackmate import trackmate_peak_import


def test_import():
    fname = "Notebooks/FakeTracks.xml"
    spots = trackmate_peak_import(fname)
    assert spots.shape == (12, 17)