from behave.__main__ import main as run_test_case
from bdd.configurations import globalconfigurations as config


feature = f"{config.project_path}/features/GoogleSearch.feature"
scenario = "Searching a word on the google search page"
run_test_case([feature, '-n', scenario])
