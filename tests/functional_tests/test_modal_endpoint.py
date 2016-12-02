import pytest
from flask import url_for

@pytest.mark.usefixtures('live_server')
@pytest.mark.nondestructive
def test_render_modal_title(selenium):
    selenium.get(url_for('modal', _external=True))
    selenium.find_element_by_id('modal-title')
