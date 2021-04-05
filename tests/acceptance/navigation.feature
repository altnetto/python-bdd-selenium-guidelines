Feature: Test navigation between pages
    We can have a longer Description
    That can span a few lines

    Scenario: Homepage can go to Blog
        Given I am on the Homepage
        When I click on the link id "blog-link"
        Then I am on the blog page