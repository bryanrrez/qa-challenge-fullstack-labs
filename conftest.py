
import json

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


SUPPORTED_ENVIRONMENTS = ['localhost']  # 'qa', 'staging' and 'production'
SUPPORTED_BROWSERS = ['chrome', 'firefox']
CONFIG_FILE_PATH = 'config.json'
APPOINTMENTS_FILE_PATH = 'data/appointments.json'
DEFAULT_WAIT_TIME = 10
URL = 'http://localhost:3000/'


@pytest.fixture(scope='session')
def config():
    with open(CONFIG_FILE_PATH, encoding='utf-8') as config_file:
        return json.load(config_file)

@pytest.fixture(scope='session')
def appointments():
    with open(APPOINTMENTS_FILE_PATH, encoding='utf-8') as config_file:
        return json.load(config_file)

@pytest.fixture(scope='session')
def config_wait_time(config):
    if 'wait_time' in config:
        return DEFAULT_WAIT_TIME

    return config['wait_time']

@pytest.fixture(scope='session')
def config_environment(config):
    if 'environment' not in config:
        raise Exception('The config file does not have an "environment" key.')
    elif config['environment'] not in SUPPORTED_ENVIRONMENTS:
        raise Exception('{environment} is not a supported environment'.format(environment=config['environment']))

@pytest.fixture(scope='session')
def config_url(config_environment):
    if config_environment == 'localhost':
        return URL
    # elif config_environment == 'qa':
    #     return 'qa url'
    # elif config_environment == 'staging':
    #     return 'qa url'

@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The config file a "browser" key.')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception('{browser} is not a supported browser.'.format(browser=config['browser']))

@pytest.fixture(scope='session')
def driver(config_browser, config_wait_time, config_url):
    if config_browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif config_browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.implicitly_wait(config_wait_time)
    driver.maximize_window()
    driver.get(URL)

    yield driver

    driver.quit()