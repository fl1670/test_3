import os

if __name__ == '__main__':

    python = 'py'

    tests_folder = os.path.dirname(os.path.abspath(__file__))
    os.chdir(tests_folder)

    tmpIF = True
    if tmpIF:
        allure_log = f" --alluredir={tests_folder}\\allure-results"
    else:
        allure_log = ''

    os.system(f'{python} -m pytest {tests_folder} {allure_log}')
