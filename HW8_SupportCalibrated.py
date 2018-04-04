import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat
import HW8_Parameters as P


def print_outcomes(calibrated_model, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param calibrated_model: calibrated model
    :param strategy_name: the name of the selected therapy
    """

    # print expected mean survival time
    print(strategy_name)
    print("  Expected mean reward ($) and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          calibrated_model.get_mean_reward_proj_interval(alpha=P.ALPHA, deci=1))


def print_comparative_outcomes(calibrated_model_fair, calibrated_model_unfair, increase=None):
    """ prints expected and percentage increase in average reward when coin is unfair
    :param calibrated_model_fair: calibrated model simulated when coin is fair
    :param calibrated_model_unfair: calibrated model simulated when coin is unfair
    """

    # increase in reward
    increase = Stat.DifferenceStatPaired(
        name = "Increase in Reward",
        x=calibrated_model_unfair.get_mean_total_reward(),
        y_ref=calibrated_model_fair.get_mean_total_reward()
    )

    # estimate and CI
    estimate_PI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI(alpha=P.ALPHA),
        deci=1
    )
    print("Expected increase in reward ($) and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_PI)

