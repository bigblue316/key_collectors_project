import requests, json, time, os

def send_webhook():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': 'Token_here',
        'api-key': 'api_key_here',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; KIW-L24 Build/HONORKIW-L24; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36',
        'origin': 'http://localhost',
        'x-requested-with': 'com.keycollectorcomics.keycollector',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'http://localhost/',
        'accept-language': 'en-US,en;q=0.9',
        'if-none-match': 'W/"e250-l+WwY+u8VVjxyKoeAm/rbZI/prI"',
    }

    params = (
        ('version', '3.1.4'),
        ('search', ''),
        ('category', 80),
        ('limit', '1'),
        ('offset', '0'),
    )

    r = requests.get('https://api.keycollectorcomics.com/search/issues/', headers=headers, params=params)
    packages_json = r.json()
    packages_str = json.dumps(packages_json)
    parsed_json = json.loads(packages_str)

    for i in parsed_json['results']:
        try:
            title_data = (i['title'])
        except:
            title_data = str("N/A")
        
        try:
            description_data = (i['description'])
        except:
            description_data = str("N/A")

        try:
            pub_name = (i['publisher']['name'])
        except:
            pub_name = str("N/A")

        try:
            pub_date = (i['published_date'])
        except:
            pub_date = str("N/A")

        try:
            artist = (i['artist']['fullName'])
        except:
            artist = str("N/A")

        try:
            writer = (i['writer']['fullName'])
        except:
            writer = str("N/A")

        try:
            sold_low = (i['priceLow'])
        except:
            sold_low = str("N/A")

        try:
            sold_mid = (i['priceMedium'])
        except:
            sold_mid = str("N/A")

        try:
            sold_high = (i['priceHigh'])
        except:
            sold_high = str("N/A")

        try:
            image_url = (i['image_url'])
        except:
            image_url = str("N/A")

        try:
            ebay_link = (i['ebayReferral'].split('&')[0])
        except:
            ebay_link = str("N/A")
        

    ### SEND TO WEBHOOK ###
    # Webhook URL 
        url = "discord_url_here"
        #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
        data = {
    "username": "Hot Keys",
    "avatar_url": "https://cdn.discordapp.com/attachments/597604981193048094/661661086470111243/ihofava.gif",
    "content": "",
    "embeds": [
        {
        "color": 9904533,
        "timestamp": '',
        "image": {},
        "thumbnail": {
                "url": (image_url)
            },
        "footer": {
            "text": "IHOF Comics™",
            "icon_url": "https://cdn.discordapp.com/attachments/597604981193048094/661661086470111243/ihofava.gif"
        },
        "fields": [
            {
            "name": "Title",
            "value": (title_data),
            "inline": 'false'
            },      
            {
            "name": "Details",
            "value": (description_data),
            "inline": 'false'
            },  
            {
            "name": "Publisher/Published Date",
            "value": (pub_name) + " " + (pub_date),
            "inline": 'false'
            },                 
            {
            "name": "Writer",
            "value": (writer),
            "inline": 'true'
            },
            {
            "name": "Artist",
            "value": (artist),
            "inline": 'true'
            },  
            {
            "name": "Search Ebay",
            "value": "[Click here](" + ebay_link + ")",          
            "inline": 'true'
            },            
            {
            "name": "Average Ebay Sales",
            "value": "Low: $" + (sold_low) + "\n" + "Mid: $" + (sold_mid) + "\n" + "High: $" + (sold_high),
            "inline": 'true'
            }       
        ]
        }
    ]
    }

        result = requests.post(url, json = data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Webhook successfully sent".format(result.status_code))
