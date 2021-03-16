from bdd.pages.Base import Base


class GoogleSearchPage(Base):

    def __init__(self, context):
        Base.__init__(self, context=context)

    def search_url(self, url):
        self.context.browser.get(url)

    def search_word(self, word):
        self.context.does_the_word_exist_on_the_google_search_page = True if word in self.context.browser.page_source \
            else False
        return self.context.does_the_word_exist_on_the_google_search_page

