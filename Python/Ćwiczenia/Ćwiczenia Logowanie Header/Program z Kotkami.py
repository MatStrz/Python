import requests
import json
import credentials


def get_json_content_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("niepoprawny format", response.text)
    else:
        return (content)


def get_favourite_cats(userId):
    params = {
        "sub_id": userId
    }
    r = requests.get("https://api.thecatapi.com/v1/favourites/",
                     params, headers=credentials.headers)
    return get_json_content_from_response(r)


def get_random_cat():
    r = requests.get("https://api.thecatapi.com/v1/images/search/",
                     headers=credentials.headers)
    return get_json_content_from_response(r)[0]


def add_Favourite_cat(catId, userId):
    catData = {
        "image_id": catId,
        "sub_id": userId
    }

    r = requests.post("https://api.thecatapi.com/v1/favourites/", json=catData,
                      headers=credentials.headers)

    return get_json_content_from_response(r)


def remove_cat_from_favourite(favouriteCatId, userId):
    r = requests.delete("https://api.thecatapi.com/v1/favourites/" + favouriteCatId,
                        headers=credentials.headers)
    return get_json_content_from_response(r)


userId = "JakisUser"
name = "Mateusz"


print("Witaj", name)

print("Twoje ulubine kotki, to:")
favouriteCats = get_favourite_cats(userId)
for cat in favouriteCats:
    print(cat['image']['url'])

randomCat = get_random_cat()
print("Wylosowano kotka:", randomCat['url'])

addToFavourites = (input("Czy chcesz dodać Kotka do ulubionych? T/N"))
justAdedCatInfo = {}
if addToFavourites.upper() == "T":
    resultOfAdding = add_Favourite_cat(randomCat["id"], userId)
    justAdedCatInfo = {resultOfAdding["id"]: randomCat['url']}
    print(resultOfAdding['message'],
          "Dodano kotka o Id:", resultOfAdding['id'])
else:
    print("No to lipa, Kotek bedzie smutny")

favouriteCatsById = {
    favouriteCat['id']: favouriteCat['image']['url']
    for favouriteCat in favouriteCats
}

favouriteCatsById.update(justAdedCatInfo)

print(favouriteCatsById)

idCatToRemoveFromFavourite = input(
    "Podaj id kotka którego chcesz usunąc z ulubionych")

print(remove_cat_from_favourite(idCatToRemoveFromFavourite, userId))
