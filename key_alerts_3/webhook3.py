import requests, json, time, os

def send_webhook():
    headers = {
        'accept': 'application/json, text/plain, */*',
        'authorization': 'Token 2cd4f02171217c7049f1237c9b6485f317c48d87',
        'api-key': '7c625c136abaac5fb5aa6f98b3a9196a0ef80c47',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; KIW-L24 Build/HONORKIW-L24; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36',
        'origin': 'http://localhost',
        'x-requested-with': 'com.keycollectorcomics.keycollector',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'http://localhost/',
        'accept-language': 'en-US,en;q=0.9',
        'if-none-match': 'W/"b621-h1kjQQU5EZU/dNKGucjVceR7K4w"',
    }

    params = (
        ('version', '3.1.4'),
        ('search', ''),
        ('segment', '3'),
        ('limit', '1'),  # LIMIT MAX = 20
        ('offset', '0'),
    )

    r = requests.get('https://api.keycollectorcomics.com/search/alerts/', headers=headers, params=params)
    packages_json = r.json()
    packages_str = json.dumps(packages_json)
    parsed_json = json.loads(packages_str)

        ## WRITE JSON FILE ###
    # with open("./results.txt", "a") as file:
    #     file.write(json.dumps(packages_json, indent=4))

    # with open('./test_series.json') as access_json:
    #     parsed_json = json.load(access_json)

    all_urls = []

    for i in parsed_json['results']:
        try:
            title_data = (i['title'])
        except:
            title_data = str("Title = N/A")
        
        try:
            description_data = (i['message'])
        except:
            description_data = str("Description = N/A")

        try:
            categories = (i['categories'])
            for i in categories:
                try:
                    absolute_url = (i['absoluteUrl'])
                    all_urls.append(absolute_url)
                except:
                    absolute_url = str("N/A")
        except:
            pass

        try:
            issues = (i['issues'])
            for i in issues:
                try:
                    absolute_url = (i['absoluteUrl'])
                    all_urls.append(absolute_url)
                except:
                    absolute_url = str("N/A")
        except:
            pass

        try:
            promotions = (i['promotions'])
            for i in promotions:
                try:
                    absolute_url = (i['absoluteUrl'])
                    all_urls.append(absolute_url)
                except:
                    absolute_url = str("N/A")
        except:
            pass

        try:
            characters = (i['characters'])
            for i in characters:
                try:
                    absolute_url = (i['absoluteUrl'])
                    all_urls.append(absolute_url)
                except:
                    absolute_url = str("N/A")
        except:
            pass
            
        try:
            series = (i['series'])
            for i in series:
                try:
                    absolute_url = (i['absoluteUrl'])
                    all_urls.append(absolute_url)                
                except:
                    absolute_url = str("N/A")
        except:
            pass

        url_str = '\n'.join(all_urls)

    ### SEND TO WEBHOOK ###
    # Webhook URL """ Comment out the TEST URL if no URL changes needed for script """
        #IHOF Discord#
        url = "https://discord.com/api/webhooks/805252534578970636/DS_R-6FtQUgEVDgCwW4eR47pNWIMHTZsBRB2f9fX3SBjPV7julFbv8K7nGGlEXmTxyL8"

        #TEST Discord#
        # url = "https://ptb.discord.com/api/webhooks/595473033263841285/i78DFApF19jA7ZnqUe8_1Enilx78999z4RwKhKG1S-ru21BxFMg0tkLZsC3M4n2VnG7i"

        #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
        data = {
        "username": "Key Alerts, News & Updates",
        "avatar_url": "https://cdn.discordapp.com/attachments/597604981193048094/661661086470111243/ihofava.gif",
        "content": "",
        "embeds": [
            {
            "color": 9904533,
            "timestamp": '',
            "image": {},
            "thumbnail": {
                    "url": ("https://cdn.discordapp.com/attachments/476434499903684608/479421537846558738/Screen_Shot_2018-08-15_at_23.49.38.png")
                },
            "footer": {
                "text": "IHOF Comics™",
                "icon_url": "https://cdn.discordapp.com/attachments/597604981193048094/661661086470111243/ihofava.gif"
            },
            "fields": [
                {
                "name": 'New update',
                "value": (title_data),
                "inline": 'false'
                },      
                {
                "name": "info:",
                "value": (description_data),
                "inline": 'false'
                },
                {
                "name": "link(s):",
                "value": (url_str),
                "inline": 'false'
                }
            ]
            }
        ]
        }

        result = requests.post(url, json = data)
        try:
            result.raise_for_status()
            time.sleep(5)
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Webhook successfully sent".format(result.status_code))