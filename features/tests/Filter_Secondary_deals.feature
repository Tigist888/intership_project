
Feature:  Filter Secondary deals

  Scenario:  User can filter the Secondary deals by the “want to buy” option

    Given  Open the main page
    When  Log in to the page
    And Click on the “Secondary” option on the left side menu
    Then Verify that the right page opens
    When Click on Filters
    And Filter the products by “want to buy
    And Click on Apply Filter
    Then Verify all cards have a “Want to buy” tag