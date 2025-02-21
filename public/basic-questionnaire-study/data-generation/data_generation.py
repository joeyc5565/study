import json
import random

def generate_experiment_data(num_trials=60, num_points=10):
    """
    Generate a dataset with random values between 0-100 for each trial.
    The fifth data point will be the correct answer.
    Assigns names in three categories (vertical, horizontal, reverse).
    Ensures the correct file paths for each category.
    """
    experiment_data = {}
    #loop

    for trial in range(1, num_trials + 1):
        # Generate a list of 10 random values (sorted for consistency)
        data_points = sorted([random.randint(0, 100) for _ in range(num_points)])

        # Select the fifth data point (index 4) as the correct answer
        correct_value = data_points[4]

        # Determine the category based on trial number
        if trial <= 20:
            bar_type = "vertical_bar"
            file_path = "basic-questionnaire-study/assets/vertical-bar.html"
        elif trial <= 40:
            bar_type = "horizontal_bar"
            file_path = "basic-questionnaire-study/assets/horizontal.html"
        else:
            bar_type = "reverse_bar"
            file_path = "basic-questionnaire-study/assets/reverse-bar.html"

        question_id = f"{bar_type}_{(trial - 1) % 20 + 1}"
        question_key = f"{trial}-question"

        # Structure the trial data in the required format
        experiment_data[question_key] = {
            "type": "website",
            "path": file_path,
            "parameters": {
                "barData": data_points
            },
            "response": [
                {
                    "id": question_id,
                    "prompt": "What is the value of the selected bar?",
                    "location": "sidebar",
                    "type": "numerical",
                    "placeholder": "0-100",
                    "min": 0,
                    "max": 100
                }
            ],
            "correctAnswer": [
                {
                    "id": question_id,
                    "answer": correct_value
                }
            ]
        }

    return experiment_data

# Generate the dataset
generated_data = generate_experiment_data()

# Save the data to JSON
with open("generated_config.json", "w") as f:
    json.dump({"components": generated_data}, f, indent=4)

print("✅ Data generation complete. File saved as generated_config.json")
