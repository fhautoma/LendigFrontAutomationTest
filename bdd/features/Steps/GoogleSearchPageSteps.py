from behave import Given, When, Then
from bdd.pages.google.GoogleSearchPage import GoogleSearchPage


@Given('a browser is used to load the URL "{url}"')
def step_impl(context, url):
    context.current_page = GoogleSearchPage(context)
    context.current_page.search_url(url)


@When('searching the word "{word}" on the google search page')
def step_impl(context, word):
    context.current_page.search_word(word)


@Then('fail if not found or pass if found the word "{searched_word}" on the google search page')
def step_impl(context, searched_word):
    assert context.does_the_word_exist_on_the_google_search_page is True, f'Expected found "{searched_word}" word on ' \
        f'the google search page but not found'
