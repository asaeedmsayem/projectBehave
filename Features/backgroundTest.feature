Feature: Multiple Scenarios with Background

  Background: Common Steps
    Given I will Launch browser
    When I will Visit OrangeHRM Website

  Scenario: Logo should be present on OrangeHRM Homepage
    Then I will Verify the logo on the Homepage
    And I will Close browser

  Scenario Outline: Login to OrangeHRM with Multiple Parameters
    And Enter username "<user>" and Password "<pass>"
    And Click on Login button
    Then User should successfully login to Dashboard

    Examples:
      | user     | pass     |
      | Admin    | admin123 |
      | admin    | admin213 |
      | admin123 | admin    |