from production import IF, AND, THEN, FAIL, OR

jew_rule1 = IF( AND( '(?x) wears kipa',
                '(?x) speaks Jewish',
                '(?x) has height 160',
                '(?x) has Judaism religion',
                '(?x) has yellow skin',
                '(?x) is medium familiar with Luna-City'
                ), THEN('(?x) is jew'))

jew_rule2 = IF( AND( '(?x) wears kipa',
                '(?x) speaks Jewish',
                '(?x) has Judaism religion'
                ), THEN('(?x) is jew'))

jew_rules = [jew_rule1, jew_rule2]

american_rule1 = IF( AND( '(?x) wears suit',
                '(?x) speaks English',
                '(?x) has height 165',
                '(?x) has Catholic religion',
                '(?x) has white skin',
                '(?x) is high familiar with Luna-City'
                ), THEN('(?x) is american'))

american_rule2 = IF( AND( '(?x) speaks English',
                '(?x) has white skin'
                ), THEN('(?x) is american'))

american_rules = [american_rule1, american_rule2]

buddhist_rule1 = IF( AND( '(?x) wears chiwon',
                '(?x) speaks Thai',
                '(?x) has height 155',
                '(?x) has Buddhism religion',
                '(?x) has yellow skin',
                '(?x) is medium familiar with Luna-City'
                ), THEN('(?x) is buddhist'))

buddhist_rule2 = IF( AND('(?x) wears chiwon',
                '(?x) speaks Thai',
                '(?x) has Buddhism religion'
                ), THEN('(?x) is buddhist'))

buddhist_rules = [buddhist_rule1, buddhist_rule2]

romanian_rule1 = IF( AND('(?x) wears ie',
                '(?x) speaks Romanian',
                '(?x) has height 165',
                '(?x) has Orthodox religion',
                '(?x) has white skin',
                '(?x) is high familiar with Luna-City'
                ), THEN('(?x) is romanian'))

romanian_rule2 = IF( AND('(?x) wears ie',
                '(?x) speaks Romanian',
                '(?x) has Orthodox religion'
                ), THEN('(?x) is romanian'))

romanian_rules = [romanian_rule1, romanian_rule2]

australian_rule1 = IF( AND('(?x) wears sunglasses',
                '(?x) speaks English',
                '(?x) has height 165',
                '(?x) has Catholic religion',
                '(?x) has red skin',
                '(?x) is low familiar with Luna-City'
                ), THEN('(?x) is australian'))

australian_rule2 = IF( AND('(?x) wears sunglasses',
                '(?x) has red skin',
                '(?x) is low familiar with Luna-City'
                ), THEN('(?x) is australian'))

australian_rules = [australian_rule1, australian_rule2]

lunian_rule1 = IF( AND('(?x) wears luna',
                '(?x) speaks Lunish',
                '(?x) has height 160',
                '(?x) has Lunism religion',
                '(?x) has white skin',
                '(?x) is high familiar with Luna-City'
                ), THEN('(?x) is lunian'))

lunian_rule2 = IF( AND('(?x) wears luna',
                '(?x) speaks Lunish',
                '(?x) has Lunism religion'
                ), THEN('(?x) is lunian'))

lunian_rules = [lunian_rule1, lunian_rule2]

rules = []
rules.extend(jew_rules)
rules.extend(american_rules)
rules.extend(buddhist_rules)
rules.extend(romanian_rules)
rules.extend(australian_rules)
rules.extend(lunian_rules)