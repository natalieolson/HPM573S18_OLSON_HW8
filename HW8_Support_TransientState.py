import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat
import HW8_Parameters as P


def print_outcomes(sim_output, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected coin
    """

    # mean and confidence interval text of rewards
    reward_mean_PI_text = Format.format_estimate_interval(
        estimate= sim_output.get_mean_total_reward(),
        interval=sim_output.get_PI_total_reward(alpha=P.ALPHA),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print("  Estimate of mean reward ($) and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          reward_mean_PI_text)


def print_comparative_outcomes(multiCohortFair, multiCohortUnfair):
    """ prints expected and percentage increase in average reward when coin is unfair
    :param multiCohortFair: multiple cohorts simulated when coin is fair
    :param multiCohortUnfair: multiple cohorts simulated when coin is unfair
    """

    # increase in reward
    increase = Stat.DifferenceStatIndp(
        name='Increase in Reward',
        x = multiCohortUnfair.get_mean_total_reward(),
        y_ref = multiCohortFair.get_mean_total_reward())


    # estimate and PI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI(alpha=P.ALPHA),
        deci=1
    )

    print("Expected increase in mean reward ($) and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

