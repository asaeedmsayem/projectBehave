Feature: OrangeHRM Logo

  Scenario: Logo should be present on OrangeHRM Homepage
    Given Launch browser
    When Open OrangeHRM Website
    Then Verify the logo on the Homepage
    And Close browser