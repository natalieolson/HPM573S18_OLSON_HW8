import HW8_Parameters as P
import HW8_Classes as Cls
import HW8_Support_TransientState as Support

# create multiple cohorts for when the coin is fair

multiCohortFair = Cls.MultipleGameSets(
    ids = range(P.NUM_SIM_GAMES),
    n_games_in_a_set= P.REAL_NUM_GAMES,
    prob_head = P.HEADS_PROB_FAIR)

# simulate all cohorts
multiCohortFair.simulation()

# create multiple cohorts for when the coin is unfair

multiCohortUnfair = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_GAMES),
    n_games_in_a_set = P.REAL_NUM_GAMES,
    prob_head = P.HEADS_PROB_UNFAIR)

# simulate all cohorts
multiCohortUnfair.simulation()

# print outcomes of each cohort
print Support.print_outcomes(multiCohortFair, 'When coin is fair:')
print Support.print_outcomes(multiCohortUnfair, 'When coin is unfair:'),

# print comparative outcomes

print Support.print_comparative_outcomes(multiCohortFair, multiCohortUnfair)

print ("The change in reward from the gambler's perspective is $203")

