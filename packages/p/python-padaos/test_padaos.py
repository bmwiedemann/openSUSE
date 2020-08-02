from padaos import IntentContainer


class TestIntentContainer:
    def setup(self):
        self.container = IntentContainer()

    def test(self):
        self.container.add_intent('hello', [
            'hello', 'hi', 'how are you', "what's up"
        ])
        self.container.add_intent('buy', [
            'buy {item}', 'purchase {item}', 'get {item}', 'get {item} for me'
        ])
        self.container.add_entity('item', [
            'milk', 'cheese'
        ])
        self.container.add_intent('drive', [
            'drive me to {place}', 'take me to {place}', 'navigate to {place}'
        ])
        self.container.add_intent('eat', [
            'eat {fruit}', 'eat some {fruit}', 'munch on (some|) {fruit}'
        ])
        self.container.compile()
        assert self.container.calc_intent('hello')['name'] == 'hello'
        assert not self.container.calc_intent('bye')['name']
        assert self.container.calc_intent('buy milk') == {
            'name': 'buy', 'entities': {'item': 'milk'}
        }
        assert self.container.calc_intent('eat some bananas') == {
            'name': 'eat', 'entities': {'fruit': 'bananas'}
        }

    def test_case(self):
        self.container.add_intent('test', ['Testing cAPitalizAtion'])
        assert self.container.calc_intent('teStiNg CapitalIzation')['name'] == 'test'

    def test_punctuation(self):
        self.container.add_intent('test', ['Test! Of: Punctuation'])
        assert self.container.calc_intent('test of !punctuation...')['name'] == 'test'

    def test_spaces(self):
        self.container.add_intent('test', ['this is a test'])
        assert self.container.calc_intent('thisisatest')['name'] is None
        self.container.add_intent('test2', ['this has(one|two)options'])
        assert self.container.calc_intent('this has two options')['name'] == 'test2'
        assert self.container.calc_intent('th is is a test')['name'] is None

        self.container.add_intent('test3', ['I see {thing} (in|on) {place}'])
        assert self.container.calc_intent('I see a bin test')['name'] is None
        assert self.container.calc_intent('I see a bin in there') == {
            'name': 'test3', 'entities': {'thing': 'a bin', 'place': 'there'}
        }
