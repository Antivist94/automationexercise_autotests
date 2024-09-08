import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.tag("mobile")
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Git Tutor tutorial")
@allure.story("Tutorial screens check")
def test_git_tutor_welcome_tutorial(mobile_management):
    with step('Open app and accept tutorial'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("Yes, go!")).click()
    with step('Assert: Opened 1st screen of tutorial - Primer'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element(1).should(have.text("Primer"))

    with step('Tap on "Core concepts"'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("Core concepts »")).click()
    with step('Assert: Opened 2nd screen of tutorial - Core concepts'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element(1).should(have.text("Core concepts"))

    with step('Tap on "Getting started"'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("Getting started »")).click()
    with step('Assert: Opened 3nd screen of tutorial - Getting started'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element(1).should(have.text("Getting started"))

    with step('Tap on "New repository"'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("New repository »")).click()
    with step('Assert: Opened 4th screen of tutorial - New repository'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element(1).should(have.text("New repository"))

    with step('Tap on "Work and save"'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(
            have.text("Work and save »")).click()
    with step('Assert: Opened 5th screen of tutorial - Work and save'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element(1).should(have.text("Work and save"))

    with step('Tap on "Final words"'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(
            have.text("Final words »")).click()
    with step('Assert: Opened 6th screen of tutorial - Final words'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element(1).should(have.text("Final words"))

    with step('Tap on "Finish"'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Finish"]')).click()
    with step('Assert: Opened Start page'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element(0).should(have.text("Git Tutor"))


@allure.tag("mobile")
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Git Tutor lessons")
@allure.story("Git command check")
def test_git_tutor_git_init_check(mobile_management):
    with step('Open app and skip tutorial'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("Maybe later")).click()

    with step('Open Starting up section'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("Starting up")).click()

    with step('Open "git init" command info'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("init")).click()

    with step('Assert: "git init" description is correct'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element(9).should(
            have.text("Create an empty Git repository or reinitialize an existing one"))


@allure.tag("mobile")
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Git Tutor lessons")
@allure.story("Git command check")
def test_git_tutor_git_add_check(mobile_management):
    with step('Open app and skip tutorial'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("Maybe later")).click()

    with step('Open Saving your work section'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("Saving your work")).click()

    with step('Open "git add" command info'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("add")).click()

    with step('Assert: "git add" description is correct'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element(9).should(
            have.text("Add file contents to the index"))


@allure.tag("mobile")
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Git Tutor lessons")
@allure.story("Git command check")
def test_git_tutor_git_commit_check(mobile_management):
    with step('Open app and skip tutorial'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("Maybe later")).click()

    with step('Open Saving your work section'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("Saving your work")).click()

    with step('Open "git commit" command info'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("commit")).click()

    with step('Assert: "git commit" description is correct'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element(9).should(
            have.text("Record changes to the repository"))


@allure.tag("mobile")
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Git Tutor lessons")
@allure.story("Git command check")
def test_git_tutor_git_push_check(mobile_management):
    with step('Open app and skip tutorial'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("Maybe later")).click()

    with step('Open Saving your work section'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(
            have.text("External repositories")).click()

    with step('Open "git push" command info'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("push")).click()

    with step('Assert: "git push" description is correct'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element(9).should(
            have.text("Update remote refs along with associated objects"))
