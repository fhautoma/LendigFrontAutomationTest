from behave.__main__ import main as run_test_case
from pathlib import Path

project_path = Path(__file__).parent.parent.parent

feature = f"{project_path}/LendingFrontAutomationTest/bdd/features/GoogleSearch.feature"
scenario = "Searching a word on the google search page"
run_test_case([feature, '-n', scenario])
