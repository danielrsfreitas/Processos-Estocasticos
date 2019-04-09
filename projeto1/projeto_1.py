import numpy as np
import matplotlib.pyplot as plt
"""
Plote um gráfico cujo eixo x seja a rodada e cujo 
eixo y seja a probabilidade de vencer o jogo naquela rodada.


Plote um gráfico cujo eixo x seja a rodada e cujo 
eixo y seja a probabilidade de o jogo acabar ou 
já ter acabado naquela rodada.

"""

"""
Function: UpdateSnakesNLadders(square_prob_new)

Description: Function to apply rules regarding Snakes and Ladders feature
"""
def UpdateSnakesNLadders(square_prob_new):

	s_arr = square_prob_new

# Ladders

	if (s_arr[1] > 0):
		s_arr[38] += s_arr[1]
		s_arr[1] = 0

	if (s_arr[4] > 0):
		s_arr[14] += s_arr[4]
		s_arr[4] = 0

	if (s_arr[9] > 0):
		s_arr[31] += s_arr[9]
		s_arr[9] = 0

	if (s_arr[21] > 0):
		s_arr[42] += s_arr[21]
		s_arr[21] = 0

	if (s_arr[28] > 0):
		s_arr[84] += s_arr[28]
		s_arr[28] = 0

	if (s_arr[36] > 0):
		s_arr[44] += s_arr[36]
		s_arr[36] = 0

	if (s_arr[51] > 0):
		s_arr[67] += s_arr[51]
		s_arr[51] = 0

	if (s_arr[71] > 0):
		s_arr[91] += s_arr[71]
		s_arr[71] = 0

	if (s_arr[80] > 0):
		s_arr[100] += s_arr[80]
		s_arr[80] = 0

# Snakes

	if (s_arr[16] > 0):
		s_arr[6] += s_arr[16]
		s_arr[16] = 0

	if (s_arr[48] > 0):
		s_arr[26] += s_arr[44]
		s_arr[44] = 0

	if (s_arr[49] > 0):
		s_arr[11] += s_arr[49]
		s_arr[49] = 0

	if (s_arr[56] > 0):
		s_arr[53] += s_arr[56]
		s_arr[56] = 0

	if (s_arr[62] > 0):
		s_arr[19] += s_arr[62]
		s_arr[62] = 0

	if (s_arr[64] > 0):
		s_arr[60] += s_arr[64]
		s_arr[64] = 0

	if (s_arr[87] > 0):
		s_arr[24] += s_arr[87]
		s_arr[87] = 0

	if (s_arr[93] > 0):
		s_arr[73] += s_arr[93]
		s_arr[93] = 0

	if (s_arr[95] > 0):
		s_arr[75] += s_arr[95]
		s_arr[95] = 0

	if (s_arr[98] > 0):
		s_arr[78] += s_arr[98]
		s_arr[98] = 0
	
	return s_arr

"""
Function: CalculateProbSquare(square, last_prob)

Description: function to calculate the single probability of matrix position based on past squares
"""
def CalculateProbSquare(square, last_prob):

	dice_prob = 6
	weighted_prob = 0
	count = 1

	# Square 100 has a different way to be calculated.
	# Need to consider when dice gets higher than what is needed to win.
	if (square != 100):
		for i in range(square - dice_prob, square):

			if (i >= 0):

				weighted_prob += last_prob[i] * 1/dice_prob
	else:
		for j in range(square - dice_prob, square):

			weighted_prob += last_prob[j] * (count / dice_prob)
			count += 1

	return weighted_prob 

"""
Function: UpdateArray(int square_prob[])

Description: Function to update probabilities of matrix for each round
"""
def UpdateArray(square_prob_old):

	num_of_squares = 101

	square_prob_new = np.zeros(num_of_squares)
	
	for i in range(num_of_squares):
			# matrix position 100 will carry the cumulative probability of winning 
			if(i != 100):
				square_prob_new[i] = CalculateProbSquare(i, square_prob_old)
			else:
				square_prob_new[i] = square_prob_old[100] + CalculateProbSquare(i, square_prob_old)
	
	square_prob_new = UpdateSnakesNLadders(square_prob_new)

	return square_prob_new


"""

	Main

"""

# square_prob: game matrix
square_prob = np.zeros(101)

# first set of probabilities after first roll
square_prob[38]= 1/6
square_prob[2] = 1/6
square_prob[3] = 1/6
square_prob[14]= 1/6
square_prob[5] = 1/6
square_prob[6] = 1/6

# number of rounds
game_round = 100

# arrays to plot charts
win_in_round = np.zeros(game_round)
win_after_round = np.zeros(game_round)


for i in range(game_round):
	square_prob = UpdateArray(square_prob)
	win_in_round[i] = square_prob[100]
	
	
	# sum up all probabilities of the matrix and this should add to 1
	try:
		assert np.allclose(square_prob.sum(),1), f"[INFO] sum of probs: {square_prob.sum()}"
	except AssertionError:
		print(f"[INFO] sum of probs: {square_prob.sum()}")

for j in range(1, game_round):
	win_after_round[j] = win_in_round[j] - win_in_round[j-1]


plt.figure(1)
plt.title("Probabilidade de vencer na rodada")
plt.xlabel("Jogada")
plt.ylabel("Chance de vencer")
plt.plot(win_after_round)

plt.figure(2)
plt.title("Probabilidade cumulativa de já ter vencido")
plt.xlabel("Jogada")
plt.ylabel("Chance de ter vencido")
plt.plot(win_in_round)

plt.show()
