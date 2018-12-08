Feature: Tweet

    Allow valid users
    Post 280 characters per tweet
    To have a better day

@rainy
    Scenario: Unable to tweet > 280 chars
        Given the "valid" user is logged in on the homepage
        When user post the tweet "-Restart não presta mais porque eu cheguei aqui 8 horas da manhã e eles não vieram falar com a gente.- vc não vai perdoar ?- não, nao vou perdoar vou xingar muito no Twitter, sério.#xingandomuito #devconfpocket #precisoestourarolimitdissopelamordedeus #heauheauheauheauheauheauaehuaehueahuaehuaehuea"
        Then the tweet button should be disabled

@sunny @sanity
    Scenario: Enable to tweet <= 280 chars
        Given the "valid" user is logged in on the homepage
        When user post the tweet "        We can neither confirm nor deny that this is our first tweet.        - by CIA       #selenium #python #behave #opensanca #devconfpocket"
        Then the tweet button should be enabled
            And the user should be able to tweet
