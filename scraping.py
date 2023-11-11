from lxml import html
import requests

url = 'https://blockspot.io/wallet/'
page = requests.get(url)

if page.status_code == 200:
    tree = html.fromstring(page.content)

    # Modification de l'expression XPath
    names = tree.xpath('//div[@class="d-flex align-items-center"]/a/text()')

    if names:
        print("Noms récupérés avec succès:")
        print(names)
    else:
        print("Aucun nom trouvé. Vérifiez l'expression XPath.")
else:
    print(f"Échec de la requête. Code d'état : {page.status_code}")