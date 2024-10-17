from scipy.stats import ttest_ind

def test_actual_vs_osrm_distance(df):
    actual_distance = df["actual_distance_to_destination"].values
    osrm_distance = df["osrm_distance"].values
    t_stat, p_value = ttest_ind(actual_distance, osrm_distance, alternative="two-sided")
    
    result = {
        "t_statistic": t_stat,
        "p_value": p_value,
        "conclusion": "Reject Null Hypothesis" if p_value < 0.05 else "Fail to reject Null Hypothesis"
    }
    return result

def test_actual_vs_osrm_time(df):
    actual_time = df["actual_time"].values
    osrm_time = df["osrm_time"].values
    t_stat, p_value = ttest_ind(actual_time, osrm_time, alternative="two-sided")
    
    result = {
        "t_statistic": t_stat,
        "p_value": p_value,
        "conclusion": "Reject Null Hypothesis" if p_value < 0.05 else "Fail to reject Null Hypothesis"
    }
    return result


def test_monthly_delivery_counts(df):
    # Get trip counts for each month
    ninth_month_count = df[df["month"] == 9]["trip_uuid"].count()
    tenth_month_count = df[df["month"] == 10]["trip_uuid"].count()

    # Perform the t-test on the counts
    t_stat, p_value = ttest_ind(
        [ninth_month_count], 
        [tenth_month_count], 
        alternative="two-sided"
    )

    # Prepare the result
    result = {
        "t_statistic": t_stat,
        "p_value": p_value,
        "conclusion": "Reject Null Hypothesis" if p_value < 0.05 else "Fail to reject Null Hypothesis"
    }
    
    return result
