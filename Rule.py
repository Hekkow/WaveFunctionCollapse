class Rule:
    def __init__(self, from_piece, to_piece, direction):
        self.from_piece = from_piece
        self.to_piece = to_piece
        self.direction = direction
    def __eq__(self, other):
        return (self.from_piece, self.to_piece, self.direction.value) == (other.from_piece, other.to_piece, other.direction.value)
    def __hash__(self):
        return hash((self.from_piece, self.to_piece))
    def __repr__(self):
        return "From " + str(self.from_piece) + " to " + str(self.to_piece) + ". " + str(self.direction)