import os
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options

from paths import apk_file


def to_driver_options(context):
    options = UiAutomator2Options()
    load_dotenv()

    if context == 'local_emulator':
        print('выбран local_emulator')
        options.set_capability('remote_url', os.getenv('REMOTE_URL_LOCAL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME_EMU'))
        options.set_capability('appWaitActivity', os.getenv(
            'APP_WAIT_ACTIVITY'))
        options.set_capability('app', apk_file(os.getenv('APP')))

    if context == 'bstack':
        options.set_capability('remote_url', os.getenv('REMOTE_URL_BS'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME_BS'))
        options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
        options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', os.getenv('BS_APP'))
        options.set_capability(
            'bstack:options', {
                'projectName': 'Git Tutor project',
                'buildName': 'browserstack-build-2',
                'sessionName': 'BStack test',
                'userName': os.getenv('BROWSERSTACK_USER'),
                'accessKey': os.getenv('BROWSERSTACK_KEY'),
            },

        )

    return options
