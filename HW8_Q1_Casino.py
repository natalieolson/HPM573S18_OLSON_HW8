
import HW8_Classes as Cls

# Calculate expected reward of 1000 games with a fair coin
trialFair = Cls.SetOfGames(id = 1, prob_head=0.5, n_games=1000)
testFair=trialFair.simulation()

print("The casino's owner can expect that an average reward with a fair coin is:", testFair.get_ave_reward())
print("The 95% CI of expected reward with a fair coin is:", testFair.get_CI_reward(0.05))

# Calculate expected reward of 1000 games with an unfair coin
trialUnfair = Cls.SetOfGames(id = 2, prob_head=0.45, n_games=1000)
testUnfair=trialUnfair.simulation()


print("The casino's owner can expect than an average reward with an unfair coin is:", testUnfair.get_ave_reward())
print("The 95% CI of expected reward with an unfair coin is:", testUnfair.get_CI_reward(0.05))

print ("The change in reward for the casino owner can be expected to be $24 when using an unfair coin")
