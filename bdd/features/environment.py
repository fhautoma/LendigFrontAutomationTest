from behave import use_fixture
from bdd.fixtures.fixtures import use_chrome_browser


def after_all(context):
    pass  # Not Implemented Yet


def before_tag(context, tags):
    if 'use.chrome.browser' in tags:
        use_fixture(use_chrome_browser, context)
