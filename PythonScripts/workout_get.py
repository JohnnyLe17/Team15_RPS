import requests
import json
import httpx
from bs4 import BeautifulSoup

def getGroups():
    return {"Abdominals", "Abductors", "Adductors", "Biceps", "Calves", "Chest", "Forearms", "Glutes", "Hamstrings", "Lats", "Lower Back", "Middle Back", "Neck", "Quadriceps", "Traps", "Triceps"}

def getExersise(muscle):
    api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
    response = requests.get(api_url, headers={'X-Api-Key': 'UQ2Yik3ehsLPHsxxAWCH1w==eisXGbJaZOjddRb5'})
    results = json.loads(response.text)
    if results:
        print (results[0]["name"])

def getImage(pic):
    image_links = []
    # Scrape the first 4 pages
    for page in range(1):
        url = f"https://www.google.com/search?q="+ pic +"+stock+image"
        response = httpx.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        for image_box in soup.select("div.row.product"):
            result = {
                "link": image_box.select_one("img").attrs["src"],
                "title": image_box.select_one("h3").text,
            }
            # Append each image and title to the result array
            image_links.append(result)
            print(result)
    # 2. Download image objects
    for image_object in image_links:
        # Create a new .png image file
        with open(f"./images/{pic}.png", "wb") as file:
            image = httpx.get(image_object["link"])
            # Save the image binary data into the file
            file.write(image.content)
            print(f"Image {image_object['title']} has been scraped")    


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