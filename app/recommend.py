def generate_recommendations(area, floors, workers, delay_days, weather_risk):
    recommendations = []

    if weather_risk.lower() == "high":
        recommendations.append("High weather risk. Add safety protocols or reschedule.")

    if workers < (area * floors) / 100:
        recommendations.append("Increase number of workers to reduce risk and time.")

    if delay_days > 10:
        recommendations.append("High delay. Try sourcing materials from new vendors.")

    if floors >= 5 and area > 1000:
        recommendations.append("Consider reducing area/floors to control cost.")

    if not recommendations:
        recommendations.append("Project setup looks optimal!")

    return recommendations
