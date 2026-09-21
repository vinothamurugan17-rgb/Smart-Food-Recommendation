import numpy as np
import skfuzzy as fuzz


def calculate_food_score(
    hunger,
    health_preference,
    calorie_preference,
    food_healthiness,
    food_calories,
    food_filling
):
    # Input ranges
    hunger_range = np.arange(0, 101, 1)
    health_range = np.arange(0, 101, 1)
    calorie_range = np.arange(0, 101, 1)
    score_range = np.arange(0, 101, 1)

    # Hunger membership functions
    hunger_low = fuzz.trimf(hunger_range, [0, 0, 50])
    hunger_medium = fuzz.trimf(hunger_range, [25, 50, 75])
    hunger_high = fuzz.trimf(hunger_range, [50, 100, 100])

    # Health preference membership functions
    health_low = fuzz.trimf(health_range, [0, 0, 50])
    health_medium = fuzz.trimf(health_range, [25, 50, 75])
    health_high = fuzz.trimf(health_range, [50, 100, 100])

    # Calorie preference membership functions
    calorie_low = fuzz.trimf(calorie_range, [0, 0, 50])
    calorie_medium = fuzz.trimf(calorie_range, [25, 50, 75])
    calorie_high = fuzz.trimf(calorie_range, [50, 100, 100])

    # Output membership functions
    score_low = fuzz.trimf(score_range, [0, 0, 50])
    score_medium = fuzz.trimf(score_range, [25, 50, 75])
    score_high = fuzz.trimf(score_range, [50, 100, 100])

    # Fuzzification
    h_low = fuzz.interp_membership(
        hunger_range, hunger_low, hunger
    )
    h_medium = fuzz.interp_membership(
        hunger_range, hunger_medium, hunger
    )
    h_high = fuzz.interp_membership(
        hunger_range, hunger_high, hunger
    )

    health_l = fuzz.interp_membership(
        health_range, health_low, health_preference
    )
    health_m = fuzz.interp_membership(
        health_range, health_medium, health_preference
    )
    health_h = fuzz.interp_membership(
        health_range, health_high, health_preference
    )

    calorie_l = fuzz.interp_membership(
        calorie_range, calorie_low, calorie_preference
    )
    calorie_m = fuzz.interp_membership(
        calorie_range, calorie_medium, calorie_preference
    )
    calorie_h = fuzz.interp_membership(
        calorie_range, calorie_high, calorie_preference
    )

    # Food fuzzy values
    food_health = fuzz.interp_membership(
        health_range, health_high, food_healthiness
    )

    food_filling = fuzz.interp_membership(
        hunger_range, hunger_high, food_filling
    )

    # Convert calories into a 0-100 scale
    calorie_value = min(food_calories / 4, 100)

    food_low_calorie = 1 - fuzz.interp_membership(
        calorie_range, calorie_high, calorie_value
    )

    # Fuzzy rules

    # Rule 1: High hunger + high health preference + healthy food
    rule1 = min(
        h_high,
        health_h,
        food_health
    )

    # Rule 2: High hunger + filling food
    rule2 = min(
        h_high,
        food_filling
    )

    # Rule 3: Low calorie preference + low calorie food
    rule3 = min(
        calorie_l,
        food_low_calorie
    )

    # Rule 4: Medium hunger + medium health preference
    rule4 = min(
        h_medium,
        health_m
    )

    # Rule 5: Low hunger + low calorie preference
    rule5 = min(
        h_low,
        calorie_l
    )

    # Aggregate rules
    high_activation = max(
        rule1,
        rule2,
        rule3
    )

    medium_activation = max(
        rule4,
        rule5
    )

    low_activation = min(
        h_low,
        calorie_h
    )

    # Apply output membership functions
    activated_low = np.fmin(
        low_activation,
        score_low
    )

    activated_medium = np.fmin(
        medium_activation,
        score_medium
    )

    activated_high = np.fmin(
        high_activation,
        score_high
    )

    # Combine outputs
    aggregated = np.fmax(
        activated_low,
        np.fmax(
            activated_medium,
            activated_high
        )
    )

    # Defuzzification
    if np.sum(aggregated) == 0:
        return 0.0

    final_score = fuzz.defuzz(
        score_range,
        aggregated,
        "centroid"
    )

    return round(float(final_score), 2)