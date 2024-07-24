class EarleyItem:
    def __init__(self, production, dot_position, start_column):
        self.production = production
        self.dot_position = dot_position
        self.start_column = start_column

    def __eq__(self, other):
        return (self.production == other.production and 
                self.dot_position == other.dot_position and 
                self.start_column == other.start_column)

    def __hash__(self):
        return hash((tuple(self.production), self.dot_position, self.start_column))

def predict(grammar, column, item):
    non_terminal = item.production[item.dot_position]
    for rule in grammar.get(non_terminal, []):
        new_item = EarleyItem((non_terminal, rule), 0, column)
        if new_item not in column:
            column.append(new_item)

def scan(tokens, column, item):
    if item.dot_position < len(item.production[1]) and \
       item.production[1][item.dot_position] == tokens[column]:
        new_item = EarleyItem(item.production, item.dot_position + 1, item.start_column)
        if new_item not in chart[column + 1]:
            chart[column + 1].append(new_item)

def complete(chart, column, item):
    for entry in chart[item.start_column]:
        if entry.dot_position < len(entry.production[1]) and \
           entry.production[1][entry.dot_position] == item.production[0]:
            new_item = EarleyItem(entry.production, entry.dot_position + 1, entry.start_column)
            if new_item not in chart[column]:
                chart[column].append(new_item)

def earley_parse(tokens, grammar):
    global chart
    chart = {i: [] for i in range(len(tokens) + 1)}
    start_rule = list(grammar.keys())[0]
    chart[0].append(EarleyItem((start_rule, grammar[start_rule][0]), 0, 0))
    
    for column in range(len(tokens) + 1):
        for item in chart[column]:
            if item.dot_position < len(item.production[1]):
                if item.production[1][item.dot_position] in grammar:
                    predict(grammar, column, item)
                else:
                    scan(tokens, column, item)
            else:
                complete(chart, column, item)
    
    for item in chart[len(tokens)]:
        if item.production[0] == start_rule and item.dot_position == len(item.production[1]) and item.start_column == 0:
            return True
    return False

example_grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': ['the', 'a'],
    'N': ['cat', 'dog'],
    'V': ['chased', 'ate']
}

example_tokens = ['the', 'dog', 'chased', 'a', 'cat']
result = earley_parse(example_tokens, example_grammar)
print("Parsing successful:", result)
