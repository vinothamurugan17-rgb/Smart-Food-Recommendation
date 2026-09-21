from food_data import FOODS
from fuzzy_logic import calculate_food_score


def get_recommendations(
    hunger,
    health_preference,
    calorie_preference,
    meal="breakfast",
    diet="vegetarian"
):
    recommendations = []

    for food in FOODS:

        # Filter according to meal and diet
        if food["meal"] != meal:
            continue

        if food["diet"] != diet:
            continue

        # Calculate fuzzy suitability score
        score = calculate_food_score(
            hunger,
            health_preference,
            calorie_preference,
            food["healthiness"],
            food["calories"],
            food["filling"]
        )

        recommendations.append({
            "name": food["name"],
            "score": score,
            "calories": food["calories"],
            "healthiness": food["healthiness"],
            "filling": food["filling"]
        })

    # Sort highest score first
    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations