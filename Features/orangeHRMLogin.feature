Feature: OrangeHRM Login

  Scenario Outline: Login to OrangeHRM with Multiple Parameters
    Given Launch chrome browser
    When Visit OrangeHRM website
    And Enter username "<user>" and Password "<pass>"
    And Click on Login button
    Then User should successfully login to Dashboard

    Examples:
      | user     | pass     |
      | Admin    | admin123 |
      | admin    | admin213 |
      | admin123 | admin    |