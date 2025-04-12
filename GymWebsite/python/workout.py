import requests
import json

# Function to get exercise groups (muscle categories)
def getGroups():
    return {"Abdominals", "Abductors", "Adductors", "Biceps", "Calves", "Chest", 
            "Forearms", "Glutes", "Hamstrings", "Lats", "Lower Back", "Middle Back", 
            "Neck", "Quadriceps", "Traps", "Triceps"}

# Function to get exercises for a specific muscle group
def getExersise(muscle):
    api_url = f'https://api.api-ninjas.com/v1/exercises?muscle={muscle}'
    response = requests.get(api_url, headers={'X-Api-Key': 'UQ2Yik3ehsLPHsxxAWCH1w==eisXGbJaZOjddRb5'})
    results = response.json()  # Parse the response directly into a dictionary

    exercises = []
    if results:
        for exercise in results:
            exercises.append({
                "name": exercise["name"],
                "muscle": exercise["muscle"],
                "equipment": exercise["equipment"],
                "difficulty": exercise["difficulty"],
                "instruction": exercise["instruction"]
            })
    return exercises

# Function to download images based on exercise name from Pexels
def getImage(pic):
    api_key = 'YOUR_PEXELS_API_KEY'  # Replace with your Pexels API key
    api_url = f'https://api.pexels.com/v1/search?query={pic}&per_page=5'  # Adjust query parameters as needed

    headers = {'Authorization': api_key}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        results = response.json()
        for image in results['photos']:
            image_url = image['src']['original']
            image_title = image['alt']
            image_data = requests.get(image_url).content

            # Save the image to the local system
            with open(f'./images/{image_title}.jpg', 'wb') as file:
                file.write(image_data)
                print(f"Downloaded: {image_title}")
    else:
        print("Failed to retrieve images")

if __name__ == "__main__":
    # Get exercises for the Biceps muscle
    muscle_group = "Biceps"
    exercises = getExersise(muscle_group)
    if exercises:
        print(f"Exercises for {muscle_group}:")
        for exercise in exercises:
            print(f"- {exercise['name']} (Equipment: {exercise['equipment']}, Difficulty: {exercise['difficulty']})")
        
        # Download images related to the exercise names
        for exercise in exercises:
            getImage(exercise["name"])
    else:
        print(f"No exercises found for {muscle_group}")



#not able to grab all data
# def getGroups():
#     muscleGroup = set()
#     api_url = 'https://api.api-ninjas.com/v1/exercises'
#     response = requests.get(api_url, headers={'X-Api-Key': 'UQ2Yik3ehsLPHsxxAWCH1w==eisXGbJaZOjddRb5'})
#     results = json.loads(response.text)
#     for exercise in results: 
#         muscleGroup.add(exercise["muscle"])
#     if results:
#         print (muscleGroup)


getImage("bicep")