Test.describe("Step",function() {
    Test.it("Basic tests",function() {    
        Test.assertSimilar(step(2,100,110), [101, 103])
        Test.assertSimilar(step(4,100,110), [103, 107])
        Test.assertSimilar(step(6,100,110), [101, 107])
        Test.assertSimilar(step(8,300,400), [359, 367])
        Test.assertSimilar(step(10,300,400), [307, 317])
    
    })})