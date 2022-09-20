# The 4x4 board is represented by a list with 16 positions.
# Each position holds a list that contains the pieces
# that have been placed on that particular position.
# An empty board representation looks like:
# [
#   [], [], [], [],
#   [], [], [], [],
#   [], [], [], [],
#   [], [], [], []
# ]
#
# There are 4 possible pieces
# "WF" - White flat
# "WS" - White standing
# "BF" - Black flat
# "BS" - Black standing
#
# A board representation with 3 pieces could look like:
# [
#   ["WF", "BF"], ["WF"], [], [],
#   []          , []    , [], [],
#   []          , []    , [], [],
#   []          , []    , [], []
# ]
#
# The last piece in each list is the piece that controlls that particular square.
# The square represented by ["WF", "BF"] in the above example is therefore controlled by
# the piece "BF".
#

import utils

# returns true if "board" contains a valid road created by "player"
def roadExists(board, player):

	# reursively determines if "player" has a valid road from "currentIndex" to "targetIndex"
	def roadExistsRecursive(currentIndex, targetIndex, visited = []):
		if currentIndex in visited: return False

		currentPiece = utils.controllingPiece(board, currentIndex)
		if currentPiece == None: return False
		if utils.pieceColor(currentPiece) != player: return False
		if len(visited):
			lastPiece = utils.controllingPiece(board, visited.copy().pop())
			if currentPiece != lastPiece: return False

		if currentIndex == targetIndex:
			return True

		for adjacentIndex in utils.adjacentIndices(currentIndex):
			road = roadExistsRecursive(adjacentIndex, targetIndex, [y for x in [visited, [currentIndex]] for y in x])
			if road: return True

		return False


	return (# corner to corner
			roadExistsRecursive(0, 15) or
			roadExistsRecursive(3, 12) or

			# North to South
			roadExistsRecursive(0, 12) or
			roadExistsRecursive(0, 13) or
			roadExistsRecursive(0, 14) or
			roadExistsRecursive(1, 12) or
			roadExistsRecursive(1, 13) or
			roadExistsRecursive(1, 14) or
			roadExistsRecursive(1, 15) or
			roadExistsRecursive(2, 12) or
			roadExistsRecursive(2, 13) or
			roadExistsRecursive(2, 14) or
			roadExistsRecursive(2, 15) or
			roadExistsRecursive(3, 13) or
			roadExistsRecursive(3, 14) or
			roadExistsRecursive(3, 15) or

			# West to East
			roadExistsRecursive(0, 3) or
			roadExistsRecursive(0, 7) or
			roadExistsRecursive(0, 11) or
			roadExistsRecursive(4, 3) or
			roadExistsRecursive(4, 7) or
			roadExistsRecursive(4, 11) or
			roadExistsRecursive(4, 15) or
			roadExistsRecursive(8, 3) or
			roadExistsRecursive(8, 7) or
			roadExistsRecursive(8, 11) or
			roadExistsRecursive(8, 15) or
			roadExistsRecursive(12, 7) or
			roadExistsRecursive(12, 11) or
			roadExistsRecursive(12, 15))

testBoard = [
	["WF"],["WF"],["WF"],["WF"],
	["WF"],["WF"],["WF"],["WF"],
	["WF"],["WF"],["WF"],["WF"],
	["WF"],["WF"],["WF"],["WF"]
]

testBoard2 = [
	["WF"],["BF"],["BS"],["WS"],
	["BF"],["WF"],["WF"],["WF"],
	["BS"],["WF"],["WF"],["WF"],
	["WS"],["WF"],["WF"],["WF"]
]

testBoard3 = [
	[],["WF", "WS"],[],[],
	[],["WF"]      ,[],[],
	[],["WF"]      ,[],[],
	[],["WF"]      ,[],[]
]

testBoard4 = [
	[],["WF"],[],[],
	[],["WF"],[],[],
	[],["WF"],[],[],
	[],["WF"],[],[]
]

print(roadExists(testBoard, "W") == True)
print(roadExists(testBoard2, "W") == False)
print(roadExists(testBoard2, "B") == False)
print(roadExists(testBoard3, "W") == False)
print(roadExists(testBoard3, "B") == False)
print(roadExists(testBoard4, "W") == True)
print(roadExists(testBoard4, "B") == False)
