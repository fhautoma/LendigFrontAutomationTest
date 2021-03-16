from behave.__main__ import main as run_test_case


feature = "../bdd/features/GoogleSearch.feature"
scenario = ""
run_test_case([feature, '-n', scenario])
