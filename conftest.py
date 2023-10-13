# import pytest
# from selene.support.shared import browser
#
#
# @pytest.fixture(scope='function', autouse=True)
# def config_browser():
#     browser.driver.set_window_size(1920, 1280)


import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def config_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1280

    yield

    browser.close()
