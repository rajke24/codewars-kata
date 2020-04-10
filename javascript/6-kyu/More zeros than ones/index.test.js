Test.assertDeepEquals(moreZeros('abcde'),['a','b','d'])
Test.assertDeepEquals(moreZeros('Great job!'),['a', ' ', 'b', '!'])
Test.assertDeepEquals(moreZeros('DIGEST'),['D','I','E','T'])
Test.assertDeepEquals(moreZeros('abcdeabcde'),['a','b','d'],'Should not return duplicates values')