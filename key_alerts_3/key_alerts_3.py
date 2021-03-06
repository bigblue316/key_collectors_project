import requests, json, time, os
from webhook3 import send_webhook

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
    'if-none-match': 'W/"b621-h1kjQQU5EZU/dNKGucjVceR7K4w"',
}

params = (
    ('version', '3.1.4'),
    ('search', ''),
    ('segment', '3'),    #   USE "2" or "3"
    ('limit', '1'),
    ('offset', '0'),
)

r = requests.get('https://api.keycollectorcomics.com/search/alerts/', headers=headers, params=params)
packages_json = r.json()
packages_str = json.dumps(packages_json)
parsed_json = json.loads(packages_str)

try:    #  get id's  #
    for new_id_list in parsed_json['results']:
        new_id = (new_id_list['id'])

    with open('./key_collectors_project/key_alerts_3/latest3.json') as access_json:
        old_json = json.load(access_json)

    for old_id_list in old_json['results']:
        old_id = (old_id_list['id'])

        #  compare id's  #
    if new_id != old_id:
        print('Found update')
        send_webhook()
        with open("./key_collectors_project/key_alerts_3/latest3.json", "w") as file:            ## WRITE JSON FILE ##
            file.write(json.dumps(parsed_json))

    else:
        print('No update')

except:
    with open("./key_collectors_project/key_alerts_3/latest3.json", "w") as file:        ## WRITE old JSON FILE ##
        file.write(json.dumps(parsed_json))
    print('First file created')
