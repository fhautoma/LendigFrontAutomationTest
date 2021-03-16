from behave import Given, Then

from bdd.pages.google.GoogleSearchPage import GoogleSearchPage


@Given('a browser is used to load the URL "{url}"')
def step_impl(url):
    raise NotImplementedError
