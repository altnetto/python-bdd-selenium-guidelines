Feature: Test navigation between pages
    We can have a longer Description
    That can span a few lines

    Scenario: Homepage can go to Blog
        Given I am on the Homepage
        When I click on the "Go to blog" link
        Then I am on the blog page
        And Close the window

    Scenario: Blog can go to Homepage
        Given I am on the blog page
        When I click on the "Go to home" link
        Then I am on the Homepage
        And Close the window