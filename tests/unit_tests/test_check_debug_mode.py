import pytest

# Example of test by function
@pytest.mark.options(debug=False)
def test_check_debug_mode(app):
  assert not app.debug, 'Ensure the app not in debug mode'
