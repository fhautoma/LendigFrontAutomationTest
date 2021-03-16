@use.chrome.browser

Feature: GoogleSearch
  the purpose of this test is to validate if a specific word exists on the google search page


  Background: have at least browser installed

  Scenario: Searching a word on the google search page
    Given a browser is used to load the URL "https://www.google.com/"
    When searching the word "automation" on the google search page
    Then fail if not found or pass if found the word "automation" on the google search page
