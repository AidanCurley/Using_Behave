Feature: Water Level Checker
  As a user
  I want to make sure that the machine doesn't break if it is empty of water

  Scenario: No Water 
      Given the machine has no water
       When I switch it on
       Then the menu should be inaccessible
        And a warning should be displayed

  Scenario: Water
      Given the machine has water
       When I switch it on
       Then the menu should be accessible
