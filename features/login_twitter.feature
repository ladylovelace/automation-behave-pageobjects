Feature: Login into twitter

    Allow valid users
    To login on twitter
    To be able to use the plataform

    # Scenario: Invalid login
    #     Given "invalid" user navigates to page "landing-page"
    #     When the "invalid" user logs in
    #     Then a login error message should display
    
    Scenario: Valid login
        Given "valid" user navigates to page "landing-page"
        When the "valid" user logs in
        Then the user should be redirected to homepage